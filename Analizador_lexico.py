import ply.lex as lex

#Definicion de tokens



    
errores = []

    #def __init__(self):
     #   self.lexer = lex.lex(object=self)



reservadas = {

        'Start': 'START',
        'End': 'END',
        'Let': 'LET',
        'If': 'IF',
        'Else': 'ELSE',
        'For': 'FOR',
        'While': 'WHILE',
        'Loop': 'LOOP',
        'break': 'BREAK',
        'fn': 'FN',
        'Opera': 'OPERA',
        'Move': 'MOVE',
        'Delay': 'DELAY',
        'Main': 'MAIN',
        'Println': 'PRINTLN'

        }


tokens = [

        #Símbolos

        'ESPACIO'
        'PUNTO',
        'COMA',
        'PUNTOCOMA',
        'PARENTESIS_IZQ',
        'PARENTESIS_DER',
        'LLAVE_IZQ',
        'LLAVE_DER',
        'EQUAL',

        #Comparadores
        'MAYOR',
        'MENOR',
        'IGUAL',
        'DIFERENTE',
        'MAYORIGUAL',
        'MENORIGUAL',

        #Operadores
        'SUMA',
        'RESTA',
        'MULTIPLICA',
        'DIVIDE',
        'POTENCIA',
        

        #Tipos de datos
        'INTEGER',
        'STRING',
        'BOOLEAN',
        'ID',
        'COMENTARIO'
        ] + list(reservadas.values())


t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'

t_COMA = r'\,'
t_PUNTOCOMA = r'\;'
#t_PUNTO = r'\.'
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



def input(data):
    errors = []
    lexer.input(data)

#def build(**kwargs):
 #   lexer = lex.lex(object=self, **kwargs)


#def token():
  #      return self.lexer.token()
def t_ESPACIO(t):

    r"""[ ]+|[\t]+"""
    pass

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
    r"""[a-zA-Z][a-zA-Z0-9_@&?]*"""
    temp = reservadas.get(t.value, 'ID')
    if temp == "ID":
        if not t.value[0].islower():
            t_error(t)
    t.type = temp
    return t

def t_COMENTARIO(t):
    r"""\--*"""
    pass

    
def t_newline(t):
    r"""[\n]"""
    t.lexer.lineno += len(t.value)
    pass

def t_error(t):
    errores.append(f'Found illegal character in line {t.lexer.lineno}: \n"{t.value}"')
    t.lexer.skip(1)
    pass

def run(data):
    self.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break


cadena= """
let var1 = "Hello";
let var2 = 2;
START procedure []
    let var1 = "Bye";
    Add[var2, 5];
    PosX 20;
END
"""

def lexicalAnalizer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    prints = []
    while True:
            
        tok = analizador.token()
        if not tok: break
        prints.append(tok)
    return prints
     
        
        
    

    

    

    
        
        
