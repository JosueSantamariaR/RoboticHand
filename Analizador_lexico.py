import ply.lex as lex

#Definicion de tokens


class Lexer(object):
    
    errores = []

    def __init__(self):
        self.lexer = lex.lex(object=self)



    reservadas = {

        
        'let': 'LET',
        'if': 'IF',
        'else': 'ELSE',
        'for': 'FOR',
        'while': 'WHILE',
        'loop': 'LOOP',
        'break': 'BREAK',
        'fn': 'FN',
        'opera': 'OPERA',
        'move': 'MOVE',
        'delay': 'DELAY',
        'main': 'MAIN',
        'println!': 'PRINTLN'

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
    t_PUNTO = r'\.'
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
    t_POTENCIA = r'\**'



    def t_ESPACIO(self, t):

         r"""[ ]+|[\t]+"""
         pass

    def t_INTEGER(self,t):

        r"""-\d+|\d+"""
        
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %d", t.value)
            t.value = 0
        return t

    def t_BOOLEAN(self, t):
        r"""True|False"""
        try:
            if t.value == "True":
                t.value = True
            else:
                t.value = False
        except ValueError:
            print("El valor no es boolean")
            t.value = False

        return t

    def t_STRING(self, t):
        r"""["]{1}[^"]*["]{1}"""
        t.value = str(t.value).replace('\n', " ")
        return t

    def t_ID(self, t):
        r"""[a-zA-Z_#?][a-zA-Z0-9_#?]*"""
        temp = self.reservada.get(t.value, 'ID')
        if temp == "ID":
            if not t.value[0].islower():
                self.t_error(t)
        t.type = temp
        return t

    def t_COMENTARIO(self, t):
        r"""\@*"""
        pass

    def t_newline(self, t):
        r"""[\n]"""
        t.lexer.lineno += len(t.value)
        pass

    def t_error(self, t):
        self.errores.append(f'Found illegal character in line {t.lexer.lineno}: \n"{t.value}"')
        t.lexer.skip(1)
        pass

    
    def run(self, data):
        self.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
    


    analizador = lex.lex()
    analizador.input(cadena)
    prints = []
    while True:
            
        tok = analizador.token()
        if not tok: break
        prints.append(tok)
    return prints
     
        
        
    

    

    

    
        
        
