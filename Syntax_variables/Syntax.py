import ply.yacc as yacc
import os
import codecs
import re
from Analizador_lexico import tokens
from Analizador_lexico import lexicalAnalizer
#from Comunicacion import write_read
from sys import stdin
from Semantico import *

variables = []

valores = []

errores = []

prints = []

def p_Start(p):
    '''
    Start : code
    '''

def p_Code(p):
    '''
    code : INICIO cuerpo main FIN
    '''

    p[0] = p[2]

def p_cuerpo(p):
    '''
    cuerpo : variable
           | expresion
    '''

    p[0] = p[1]

def p_main(p):
    '''
    main : MAIN LPAREN RPAREN PUNTOCOMA
'''

def p_Variable(p):
    '''
    variable : variable1 cuerpo
             | empty empty
    '''

    if (p[2] != '$'):
        p[0] = (p[1],p[2])

    else:
        p[0] = p[1]
    

    

def p_Variable1(p):

    '''
    variable1 : LET ID EQUAL expresion PUNTOCOMA
    '''

    p[0] = (p[1],p[2],p[3],p[4])
    
    variables.append(p[2])

    valores.append(p[4])

    #print(len(variables))


    for i in range(len(variables)):
    
        if variables[i-1] == p[2]:
            valores[i-1] = p[4]

            

    print (variables)
    print (valores)

    print( type(valores[0]))

def p_expresion(p):
    '''
    expresion : INTEGER expresion
              | BOOLEAN expresion
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


    if type(p[1]) == int and type(p[3]) == int:    
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False
            
    elif type(p[1]) == str and type(p[3]) == int:

    elif type(p[1]) == int and type(p[3]) == str:

    elif type(p[1]) == str and type(p[3]) == str:

    else:
        

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

    if p[2]:
        print("entró al if")
    else:
        pass

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
    Opera : OPERA LPAREN operador COMA INTEGER COMA INTEGER RPAREN PUNTOCOMA
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
       # write_read("1")
        print("Moviendo pulgar")

    elif p[3] == "i":
        #write_read("2")
        print("Moviendo índice")

    elif p[3] == "c":
        #write_read("3")
        print ("Moviento centro")

    elif p[3] == "a":
       # write_read("4")
        print ("Moviendo anular")

    elif p[3] == "m":
        #write_read("5")
        print ("Moviendo meñique")
    else:
        errores.append(f'Semantic error en función move: el valor no es un dedo')

def p_Delay(p):
    '''
    Delay : DELAY LPAREN INTEGER COMA ID RPAREN PUNTOCOMA
    '''

    if p[5] == "mili":
        print("Delay en milisegundos")
        
    elif p[5] == "seg":
        print("Delay en segundos")
        
    elif p[5] == "min":
        print("Delay en minutos")

    elif type(p[3]) != int:
        errores.append(f'Error semántico: el valor de delay no es un número')


    p[0] = p[3]

    

    

def p_Println(p):
    '''
    Println : PRINTLN LPAREN expresion RPAREN PUNTOCOMA
            
    '''

    p[0] = p[3]
    #print(type(p[3]))

    

    if type(p[3]) == str:

        for i in range(len(variables)):
    
            if variables[i-1] == p[3]:
                prints.append(valores[i-1])
                break
        
                

    elif type(p[3]) == int or bool:

        prints.append(p[3])

    else:
        errores.append(f' Error semántico: tipo de dato no adecuado en println')

        

    print(type(p[3]))

    

    print(prints)


def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'
    
    

def p_error(p):
    if p:
        errores.append(f'Syntax error in line {p.lineno - 29 } in {p.value} token')
    print(p.lineno)


def sintacticAnalizer(cadena):
    variables.clear()
    valores.clear
    parser = yacc.yacc()
    parser.parse(cadena)
