from Utilities import *
from random import randint

class Semantic:
    errores = []

    
def analyze(self,program):
    program.output_list = []
    program.errores = []
    program.solve()
    if program.errores:
        self.errores = program.errores
    else:
        return program.output_list


class Procedure:

    table = []
    global_table = []
    program = None

    def __init__(self):
        pass

    def solve(self,program,table):
        pass

class Program:

    errores = []
    output_list = []


    def __init__(self,procedures):

        super().__init__()
        self.procedures = procedures
        self.x = 0
        self.y = 0
        self.table = []
        self.scope_table = []
        self.scope_table.append(self.table)

    def solve(self):

        for i in self.procedures:
            if i:
                i.solve(self,self.scope_table)
            else:
                self.error("Semantic" "main", "Null procedure","It's possible that a null object was found while compiling, check if your file was not empty")
                            
                           
            if self.errores:
                return self.errores[0]
        return self.output_list


    def error(self,error_type,method,title,detail):
        self.errores.append(f'{error_type} Error: {title} in {method} method\n--- {detail}')


    def output(self,instruction):
        self.output_list.appned(instruction)

    
