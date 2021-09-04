import yacc
from Analizador_lexico import Lexer
from Sintactic import *

class Parser(object):

    errores = []

    def __init__(self,lexer):

        self.pareser = None
        self.lexer = lexer
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self,start="program")


    def parse(self,data):
        self.errores = []
        return self.parser.parse(data,self.lexer)


    def p_program(self,p):
        '''program : compund_procedure'''
        p[0] = Program(p[1])
        pass

    def p_compound_procedure(self,p):
        '''compund_procedure : procedure_set'''
        p[0] = p[1]
        pass

    def p_procedure_set(self,p):
        '''procedure_set : procedure procedure_set
                        | procedure'''

        try:
            p[0] = [p[1]] + p[2]

        except IndexError:
            p[0] = [p[1]]
        pass


    def p_procedure(self,p):
        '''procedure : function
                     | function_call
                     | variable_def
                     | let
                     | print
                     | move
                     | delay
                     | if
                     | for
                     | while
                     | loop
                     | empty '''

        p[0] = p[1]
        pass

    def p_expression(self,p):
        '''expression : condition
                      | boolean
                      | arithmetic
                      | INTEGER
                      | BOOL
                      | STRING
                      | ID
                      | empty '''
        
        p[0] = p[1]
        pass

    def p_parameters(self,p):
        
        '''parameters : parameters_set'''

        p[0] = p[1]
        pass

    
    def p_parameter_set(self, p):
        """parameter_set : expression COMA parameter_set
                         | expression"""
        try:
            p[0] = [p[1]] + p[3]
        except IndexError:
            p[0] = [p[1]]
        pass

    def p_function(self,p):
        '''function : FN ID LLAVE_IZQ parameters LLAVE_DER compound_procedure'''
        p[0] = Function(p[2],p[4],p[6])
        pass

    def function_call(self,p):
        '''function_call : ID LLAVE_IZQ parameters LLAVE_DER PUNTOCOMA'''
        p[0] = FunctionCall(p[1],p[3])
        pass

    def function_def(self,p):
        '''function_def : LET ID EQUAL expression PUNTOCOMA'''
        p[0] = VariableDef(p[2],p[4])
        pass

    def p_if(self,p):

        '''if : IF condition PARENTESIS_IZQ compund_procedure PARENTESIS_DER PUNTOCOMA'''
        p[0] = If(p[2],p[4])

    def p_while(self,p):
        '''while : WHILE PARENTESIS_IZQ expression PARENTESIS_DER LLAVE_IZQ compound_procedure LLAVE_DER PUNTOCOMA'''
        p[0] = While(p[3],p[6])
        pass

    def p_for(self,p):

        '''for : FOR PARENTESIS_IZQ expression PARENTESIS_DER LLAVE_IZQ compound_procedure LLAVE_DER PUNTOCOMA '''
        p[0] = For(p[3],p[6])
        pass

    def p_condition(self, p):
        """condition : PARENTESIS_IZQ condition PARENTESIS_DER"""
        p[0] = p[2]
        pass

    def p_condition_operator(self, p):
        """condition : condition IGUAL condition
                     | condition MAYOR condition
                     | condition MENOR condition
                     | condition DIFERENTE condition
                     | condition MAYORIGUAL condition
                     | condition MENORIGUAL condition
                     | expression"""
        try:
            if p[2] == "==":
                p[0] = p[1] == p[3]
            elif p[2] == ">":
                p[0] = p[1] > p[3]
            elif p[2] == "<":
                p[0] = p[1] < p[3]
            elif p[2] == "<>":
                p[0] = p[1] != p[3]
            elif p[2] == ">=":
                p[0] = p[1] >= p[3]
            elif p[2] == "<=":
                p[0] = p[1] <= p[3]               
        except IndexError:
            p[0] = p[1]
        pass

    def p_arithmetic(self,p):
        ''' arithmetic : MULTIPLICA PARENTESIS_DER expression COMA expression PARENTESIS_DER
                       | DIVIDE PARENTESIS_DER expression COMA expression PARENTESIS_DER
                       | SUMA PARENTESIS_DER expression COMA expression PARENTESIS_DER
                       | RESTA PARENTESIS_DER expression COMA expression PARENTESIS_DER
                       | POTENCIA PARENTESIS_DER expression COMA expression PARENTESIS_DER '''

        if p[1] == "Multiplica":
            p[0] = Multiply(p[3], p[5])
        elif p[1] == "Divide":
            p[0] = Divide(p[3], p[5])
        elif p[1] == "Potencia":
            p[0] = Power(p[3], p[5])
        elif p[1] == "Suma":
            p[0] = Addition(p[3], p[5])
        elif p[1] == "Resta":
            p[0] = Subtract(p[3], p[5])
        pass

    def p_empty(self, p):
        """empty :"""
        pass

    def p_error(self, p):
        if p:
            self.errors.append(f'Syntax error in line {p.lineno} in {p.value} token')
        else:
            self.errors.append("Syntax error: Invalid EOF\nMissing token at the end of a procedure")

    
                  
    

    

    

parser = Parser(Lexer())
result = parser.parse(data)
if result:
    print(result.solve()) 

    


        
        



