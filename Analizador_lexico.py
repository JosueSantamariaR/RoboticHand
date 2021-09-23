import ply.lex as lex
import re
import codecs
import os
import sys
from _ast import keyword

errores = []

reservadas = { 'Inicio': 'INICIO',
               'Fin': 'FIN',
               'let': 'LET',
               'opera': 'OPERA',
               'for': 'FOR',
               'in': 'IN',
               'while': 'WHILE',
               'loop': 'LOOP',
               'if': 'IF',
               'else': 'ELSE',
               'fn': 'FN',
               'println': 'PRINTLN',
               'move': 'MOVE',
               'delay': 'DELAY',
               'main': 'MAIN'
            }


tokens = [
            #Simbolos
    
            'ESPACIO',
            'PUNTOS',
            'COMA',
            'PUNTOCOMA',
            'RPAREN',
            'LPAREN',
            'LLAVER',
            'LLAVEL',
            'EQUAL',

            #Operadores aritméticos

            'SUMA',
            'RESTA',
            'MULTIPLICA',
            'DIVIDE',
            'POTENCIA',

            #Comparadores
            'MAYOR',
            'MENOR',
            'IGUAL',
            'DIFERENTE',
            'MAYORIGUAL',
            'MENORIGUAL',

            #Tipos de datos
            'INTEGER',
            'STRING',
            'BOOLEAN',
            'ID',

            'COMENTARIO' ] + list(reservadas.values())


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLAVEL = r'\{'
t_LLAVER = r'\}'

t_COMA = r'\,'
t_PUNTOCOMA = r'\;'
t_PUNTOS = r'\..'
t_EQUAL = r'\='


t_MAYOR = r'\>'
t_MENOR = r'\<'
t_IGUAL = r'\=='
t_DIFERENTE = r'\<>'
t_MAYORIGUAL = r'\>='
t_MENORIGUAL = r'\<='


t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'\/'
t_POTENCIA = r'\^'

'''
def t_ESPACIO(t):

    r"""[ ]+|[\t]+"""
    pass
'''

def t_INTEGER(t):
    r"""-\d+|\d+"""
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_BOOL(t):
    r"""True|False"""
    try:
        if t.value == "True":
            t.value = True
        else:
            t.value = False
    except ValueError:
        print("Didn't find a boolean")
        t.value = False

    return t

def t_STRING(t):
    r"""["]{1}[^"]*["]{1}"""
    t.value = str(t.value).replace('\n', " ")
    return t


def t_ID(t):
    r"""[a-zA-Z_#?][a-zA-Z0-9_#?]*"""
    temp = reservadas.get(t.value, 'ID')
    if temp == "ID":
        if not t.value[0].islower():
            t_error(t)
    t.type = temp
    return t

def t_COMENTARIO(t):
    r"""\@"""
    pass

def t_newline(t):
    r"""[\n]"""
    t.lexer.lineno += len(t.value) 
    pass


def t_error(t):
    errores.append(f'Found illegal character in line {t.lexer.lineno}: \n"{t.value}"')
    t.lexer.skip(1)
    pass



def lexicalAnalizer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    prints = []
    while True:
            
        tok = analizador.token()
        if not tok: break
        prints.append(tok)
    return prints
     
analizador = lex.lex()