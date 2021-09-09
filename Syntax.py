import ply.yacc as yacc
import os
import codecs
from pip._vendor.distlib.compat import raw_input
from Analizador_lexico import tokens
from Analizador_lexico import lexicalAnalizer
from Semantico import *
import json
import serial
from sys import stdin


nombres = []

errores = []

data = []


def p_Start(p):
    '''
    Start : code
    '''

def p_Code(p):
    '''
    code : START cuerpo END
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
             | variable3 cuerpo
             | empty empty
    '''
    
    if (p[2] != '$'):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_Variable1(p):
    '''
    variable1 : LET ID PUNTOCOMA
    '''
    p[0] = (p[1], p[2])
    print(p[1],p[2])
    
def p_Variable2(p):
    
    '''
    variable2 : LET ID EQUAL INTEGER PUNTOCOMA
              
    '''
    nombres[p[2]] = p[4]
    p[0] = (p[1], p[2], p[3], p[4])
    print(p[2], p[3], p[4])
    print(nombres)

def p_Variable3(p):
    '''
    variable3 : LET ID EQUAL expresion_alge1 PUNTOCOMA
              | LET ID EQUAL expresion_alge2 PUNTOCOMA
              
    '''
    nombres[p[2]] = p[4]
    p[0] = (p[1], p[2], p[3], p[4])
    print(p[2], p[3], p[4])
    print(nombres)

def p_expresion(p):
    '''
    expresion : INTEGER expresion
              | STRING expresion
              | funcion expresion
              | ID expresion
              | condicion expresion
              | expresion_alge1 expresion
              | expresion_alge2 expresion
              | empty empty
                        
    '''

    if (p[2] != '$'):
        p[0] = (p[1], p[2])
    else:
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

def expresion_alge(p):
    '''
    expresion_alge : expresion_alge0
                   | expresion_alge1
                   | expresion_alge2

    '''

def p_expresion_alge0(p):

    '''
    expresion_alge0 : SUMA
                    | RESTA
                    | MULTIPLICA
                    | DIVIDE
                    | POTENCIA
    '''

    p[0] = p[1]

def p_expresion_alge1(p):

    '''
    expresion_alge1 : INTEGER SUMA INTEGER 
                    | INTEGER RESTA INTEGER 
                    | INTEGER MULTIPLICA INTEGER 
                    | INTEGER DIVIDE INTEGER
                    | INTEGER POTENCIA INTEGER
                   
    '''

    if p[2] == '+' : p[0] = p[1]+p[3]
    elif p[2] == '-' : p[0] = p[1]-p[3]
    elif p[2] == '*' : p[0] = p[1]*p[3]
    elif p[2] == '/' : p[0] = p[1]/p[3]
    elif p[2] == '^' : p[0] = p[1]**p[3]

    print(p[0])

def p_expresion_alge2(p):

    '''
    expresion_alge2 : PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER SUMA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER RESTA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER MULTIPLICA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER DIVIDE PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER POTENCIA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   
    '''

    if p[4] == '+' : p[0] = p[2]+p[6]
    elif p[4] == '-' : p[0] = p[2]-p[6]
    elif p[4] == '*' : p[0] = p[2]*p[6]
    elif p[4] == '/' : p[0] = p[2]/p[6]
    elif p[4] == '^' : p[0] = p[2]**p[6]


def p_Igual(p):
    '''
    Igual : INTEGER IGUAL INTEGER
          | ID IGUAL ID
          | INTEGER IGUAL ID
          | ID IGUAL INTEGER
    '''
    if p[1] == p[3]:
        p[0] = True

        print(p[0])

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

    print(p[0])

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

def p_Mayorigual (p):
    '''
    Mayorigual  : INTEGER MAYORIGUAL INTEGER
          | ID MAYORIGUAL ID
          | INTEGER MAYORIGUAL ID
          | ID MAYORIGUAL INTEGER
    '''

    if p[1] >= p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])


def p_Menorigual (p):
    '''
    Menorigual  : INTEGER MENORIGUAL INTEGER
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
    If : IF  condicion  PARENTESIS_IZQ funcion PARENTESIS_DER 
    '''

    print(p[3])

    if(p[3]):
        p[0] = p[6]


def p_For(p):

    '''
    For : FOR  condicion  PARENTESIS_IZQ funcion PARENTESIS_DER 
    '''

    print(p[3])

    if(p[3]):
        p[0] = p[6]

def p_Loop(p):

    '''
    Loop : LOOP  condicion  PARENTESIS_IZQ funcion PARENTESIS_DER 
    '''

    print(p[3])

    if(p[3]):
        p[0] = p[6]


def p_While(p):

    ''' While : WHILE PARENTESIS_IZQ condicion PARENTESIS_DER PARENTESIS_IZQ funcion PARENTESIS_DER '''


    print(p[3])

    while(p[3]):
        p[0] = p[6]

def p_Opera(p):

    ''' Opera : PARENTESIS_IZQ expresion_alge0 COMA INTEGER COMA INTEGER PARENTESIS_DER '''

def p_Move(p):
    '''
    Move : MOVE ID PUNTOCOMA
    '''

    p[0] = p[2]

    if p[2] == "p":
        print("Moviendo pulgar")

    elif p[2] == "i":
        print("Moviendo índice")

    elif p[2] == "c":
        print ("Moviento centro")

    elif p[2] == "a":
        print ("Moviendo anular")

    elif p[2] == "m":
        print ("Moviendo meñique")
    else:
        print("Otro dedo " + str(p[2]))


def p_Delay(p):
    '''
    Delay : DELAY INTEGER PUNTOCOMA
    '''

    p[0] = p[2]
    print("Delay = " + str(p[2]))



def p_Println(p):

    ''' Println : PRINTLN PARENTESIS_IZQ expresion PARENTESIS_DER PUNTOCOMA'''
    p[0] = p[3]
    print(p[3])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'


def p_error(p):
    errores.append("Error de sintáxis en linea "+str(p.lineno))
    #errores.pop[len(errores)]
    print("error de sintaxis " + str(p))
    print("error en la linea " + str(p.lineno))


def sintacticAnalizer(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)
    
'''    
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data,fp)

path = './'
fileName = 'datosJSON'

'''


#################################### tester ############################################

def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    for file in files:
        print(str(cont) + ". " + file)
        cont += 1
    while respuesta == False:
        numArchivo = raw_input('\n')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    return files[int(numArchivo) - 1]


        
        



