import ply.yacc as yacc
import os
import codecs
import re
from Analizador_lexico import tokens
from Analizador_lexico import lexicalAnalizer
from Comunicacion import write_read
from sys import stdin

variables = []

errores = []

data = []

def p_Start(p):
    '''
    Start : code
    '''

def p_Code(p):
    '''
    code : INICIO cuerpo FIN
    '''

    p[0] = p[2]

def p_cuerpo(p):
    '''
    cuerpo : variable
           | expresion
    '''

    p[0] = p[1]


def p_Variable(p):
    '''
    variable : variable1 cuerpo
             | variable2 cuerpo
             | empty empty
    '''

    if (p[2] != '$'):
        p[0] = (p[1],p[2])

    else:
        p[0] = p[1]

def p_Variable1(p):
    '''
    variable1 : LET ID PUNTOCOMA
    '''
    p[0] =(p[1],p[2])
    print(p[1],p[2])

def p_Variable2(p):

    '''
    variable2 : LET ID EQUAL INTEGER PUNTOCOMA
              | LET ID EQUAL BOOLEAN PUNTOCOMA
              | LET ID EQUAL funcion PUNTOCOMA
    '''

    p[0] = (p[1],p[2],p[3],p[4])

def p_expresion(p):
    '''
    expresion : INTEGER expresion
              | STRING expresion
              | funcion expresion
              | ID expresion
              | condicion expresion
              | operador expresion
              | empty empty
    '''

    p[0] = p[1]

def p_operador(p):
    '''
    operador : SUMA
             | RESTA
             | MULTIPLICA
             | DIVIDE
             | POTENCIA
    '''

    p[0] = p[1]

    

def p_funcion(p):

    '''
    funcion : Opera
            | Move
            | Delay
            | If
            | While
            | For
            | Loop
            | Println
    '''

    p[0] = p[1]

def p_condicion(p):
    '''
    condicion : Igual expresion
              | Diferente expresion
              | Mayor expresion
              | Menor expresion
              | Mayorigual expresion
              | Menorigual expresion
    '''

    p[0] = p[1]
    

def p_Igual(p):
    '''
    Igual : INTEGER IGUAL INTEGER
          | ID IGUAL ID
          | INTEGER IGUAL ID
          | ID IGUAL INTEGER
    '''
    if p[1] == p[3]:
        p[0] = True
    else:
        p[0] = False

    print (p[0])

def p_Diferente(p):
    '''
    Diferente : INTEGER DIFERENTE INTEGER
          | ID DIFERENTE ID
          | INTEGER DIFERENTE ID
          | ID DIFERENTE INTEGER
    '''
    if p[1] != p[3]:
        p[0] = True
    else:
        p[0] = False

def p_Mayor(p):
    '''
    Mayor : INTEGER MAYOR INTEGER
          | ID MAYOR ID
          | INTEGER MAYOR ID
          | ID MAYOR INTEGER
    '''
    
    if p[1] > p[3]:
        p[0] = True
    else:
        p[0] = False
    print(p[0])

def p_Menor(p):
    '''
    Menor : INTEGER MENOR INTEGER
          | ID MENOR ID
          | INTEGER MENOR ID
          | ID MENOR INTEGER
    '''
    if p[1] < p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_Mayorigual(p):
    '''
    Mayorigual : INTEGER MAYORIGUAL INTEGER
          | ID MAYORIGUAL ID
          | INTEGER MAYORIGUAL ID
          | ID MAYORIGUAL INTEGER
    '''
    if p[1] >= p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_Menorigual(p):
    '''
    Menorigual : INTEGER MENORIGUAL INTEGER
          | ID MENORIGUAL ID
          | INTEGER MENORIGUAL ID
          | ID MENORIGUAL INTEGER
    '''

    if p[1] <= p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_If(p):

    '''
    If : IF condicion LLAVEL cuerpo LLAVER
    '''

    print(p[2])

    
    

def p_For(p):

    '''
    For : FOR ID IN INTEGER PUNTOS INTEGER LLAVEL expresion LLAVER
    '''

    #Programar if's

def p_Loop(p):
    '''
    Loop : LOOP LLAVEL cuerpo LLAVER
    '''

    #Programar if's

def p_While(p):
    '''
    While : WHILE LPAREN  condicion  RPAREN LLAVEL cuerpo LLAVER
    '''

    #Programar if's


def p_Opera(p):
    '''
    Opera : OPERA LPAREN operador COMA expresion COMA expresion RPAREN PUNTOCOMA
    '''

    #Programar If's

    if p[3] == "+":
        resultado = p[5]+p[7]
    elif p[3] == "-":
        resultado = p[5]-p[7]
    elif p[3] == "*":
        resultado = p[5]*p[7]
    elif p[3] == "/":
        resultado = p[5]//p[7]
    elif p[3] == "^":
        resultado = p[5]**p[7]


    print(resultado)
    

def p_Move(p):

    '''
    Move : MOVE LPAREN ID RPAREN PUNTOCOMA
    '''

    p[0] = p[3]

    if p[3] == "p":
        write_read("1")
        print("Moviendo pulgar")

    elif p[3] == "i":
        write_read("2")
        print("Moviendo índice")

    elif p[3] == "c":
        write_read("3")
        print ("Moviento centro")

    elif p[3] == "a":
        write_read("4")
        print ("Moviendo anular")

    elif p[3] == "m":
        write_read("5")
        print ("Moviendo meñique")
    else:
        print("Error, no es un dedo " + str(p[2]))

def p_Delay(p):
    '''
    Delay : DELAY LPAREN INTEGER COMA STRING RPAREN PUNTOCOMA
    '''

    #Programar if's

def p_Println(p):
    '''
    Println : PRINTLN LPAREN STRING RPAREN PUNTOCOMA
            
    '''

    p[0] = p[3]
    print(p[3])


def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'
    
    

def p_error(p):
    if p:
        errores.append(f'Syntax error in line {p.lineno} in {p.value} token')
    print(p.lineno)


    
def sintacticAnalizer(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)    
    
        

