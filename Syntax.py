import ply.yacc as yacc
import os
import codecs
import re
import time
from Analizador_lexico import tokens
from Analizador_lexico import lexicalAnalizer
#from Comunicacion import write_read
from sys import stdin
from Semantico import * 

variables = []

errores = []

valores = []


prints = []

#-------------------------------------------START----------------------------------------

def p_Start(p):


    '''Start : code'''

    p[0] = Start(p[1],"Start")


#-----------------------------------------CODE-------------------------------------------

def p_code(p):

    '''code : INICIO cuerpo FIN'''

    #p[0] = p[2]
    p[0] = code(p[2],"code")


#----------------------------------------CUERPO-----------------------------------------
def p_cuerpo1(p):

    '''cuerpo : variable'''

    p[0] = cuerpo1(p[1],"cuerpo1") 

def p_cuerpo2(p):

    '''cuerpo : expresion'''

    p[0] = cuerpo2(p[1],"cuerpo2") 

def p_cuerpo3(p):

    '''cuerpo : cuerpo_if'''

    p[0] = cuerpo3(p[1],"cuerpo3") 

#---------------------------------------CUERPO_IF---------------------------------------

def p_cuerpo_if1(p):

    '''cuerpo_if : variable'''


def p_cuerpo_if2(p):

    '''cuerpo_if : expresion_if'''

    p[0] = cuerpo_if2(p[1], "cuerpo_if2")



#---------------------------------------Prueba IF---------------------------------------

def p_expresion_if(p):
    '''expresion_if : funcion_if expresion'''

    p[0] = expresion_if(p[1], p[2], "expresion_if")

def p_funcion_if1(p):
    '''funcion_if : Move_if'''

    p[0] = funcion_if1(p[1], "funcion_if1")

def p_funcion_if2(p):
    '''funcion_if : Delay_if'''
    p[0] = funcion_if2(p[1], "funcion_if2")

def p_funcion_if3(p):
    '''funcion_if : Opera_if'''
    p[0] = funcion_if3(p[1], "funcion_if3")

def p_funcion_if4(p):
    '''funcion_if : Println_if'''
    p[0] = funcion_if4(p[1], "funcion_if4")

def p_Move_if(p):
    '''Move_if : MOVE LPAREN ID RPAREN PUNTOCOMA'''

    if BoolCondicion:
        if p[3] == "p":
            #write_read("1")
            print("Moviendo pulgar")

        elif p[3] == "i":
            #write_read("2")
            print("Moviendo índice")

        elif p[3] == "c":
            #write_read("3")
            print ("Moviento centro")

        elif p[3] == "a":
            #write_read("4")
            print ("Moviendo anular")

        elif p[3] == "m":
            #write_read("5")
            print ("Moviendo meñique")
        else:
            print("Error, no es un dedo " + str(p[2]))

    p[0] = Move(MOVE(p[1]),LPAREN(p[2]),Id(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Move")

def p_Delay_if(p):
    '''
    Delay_if : DELAY LPAREN INTEGER COMA STRING RPAREN PUNTOCOMA
    '''
    if BoolCondicion:
        if p[5] == "mili":
            time.sleep(p[3]/1000)
            print("Delay en milisegundos")
            
        elif p[5] == "seg":
            time.sleep(p[3])
            print("Delay en segundos")
            
        elif p[5] == "min":
            time.sleep(p[3]*60)
            print("Delay en minutos")

        elif type(p[3]) != int:
            errores.append(f'Error semántico: el valor de delay no es un número')
    
    p[0]= Delay(DELAY(p[1]),LPAREN(p[2]),Integer(p[3]),COMA(p[4]),String(p[5]),RPAREN(p[6]),PuntoComa(p[7]),"Delay")

def p_Opera_if(p):
    '''
    Opera_if : OPERA LPAREN operador COMA expresion COMA expresion RPAREN PUNTOCOMA
    '''

    #Programar If's
    if BoolCondicion:
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
    
    #print(resultado)

def p_Println1_if(p):
    '''
    Println_if : PRINTLN LPAREN STRING RPAREN PUNTOCOMA
            
    '''
    if BoolCondicion:
        prints.append(p[3])
        print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),String(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")

def p_Println2_if(p):
    '''
    Println_if : PRINTLN LPAREN INTEGER RPAREN PUNTOCOMA
            
    '''

    if BoolCondicion:
        prints.append(p[3])

        print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),Integer(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")


def p_Println3_if(p):
    '''
    Println_if : PRINTLN LPAREN ID RPAREN PUNTOCOMA
            
    '''

    if BoolCondicion:
        for i in range(len(variables)):
            if variables[i-1] == p[3]:
                prints.append(valores[i-1])      

        print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),Id(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")

def p_Println4_if(p):
    '''
    Println_if : PRINTLN LPAREN BOOLEAN RPAREN PUNTOCOMA
            
    '''
    if BoolCondicion:
        prints.append(p[3])
        print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),Boolean(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")


#-----------------------------VAR DECLARATION----------------------------------------

def p_Variable1(p):

    '''variable : variableDef1 cuerpo'''

    p[0] = Variable1(p[1],p[2],"Variable1")



def p_Variable2(p):

    '''variable : variableDef2 cuerpo'''

    p[0] = Variable2(p[1],p[2],"Variable2")


def p_VariableEmpty(p):

    '''variable : empty empty'''
    p[0] = Null()




def p_VariableDef1(p):

    '''variableDef1 : LET ID PUNTOCOMA'''

    p[0] =VariableDef1(Let(p[1]),Id(p[2]),PuntoComa(p[3]),"VariableDef1")
    
    #print(p[1],p[2])




def p_VariableDef2_1(p):

    '''variableDef2 : LET ID EQUAL INTEGER PUNTOCOMA'''

    variables.append(p[2])

    valores.append(p[4])


    for i in range(len(variables)):

        if variables[i-1] == p[2]:
            valores[i-1] = p[4]




    print (variables)
    print (valores)

    print( type(valores[0]))

    p[0] = VariableDef2_1(Let(p[1]),Id(p[2]),Equal(p[3]),Integer(p[4]),PuntoComa(p[5]),"VariableDef2_1")



def p_VariableDef2_2(p):

    '''variableDef2 : LET ID EQUAL BOOLEAN PUNTOCOMA'''

    variables.append(p[2])

    valores.append(p[4])


    for i in range(len(variables)):

        if variables[i-1] == p[2]:
            valores[i-1] = p[4]

    print (variables)
    print (valores)

    print( type(valores[0]))

    p[0] = VariableDef2_2(Let(p[1]),Id(p[2]),Equal(p[3]),Boolean(p[4]),PuntoComa(p[5]),"VariableDef2_2")



def p_VariableDef2_3(p):

    '''variableDef2 : LET ID EQUAL STRING PUNTOCOMA'''

    variables.append(p[2])
    valores.append(p[4])

    print (variables)
    print (valores)

    p[0] = VariableDef2_3(Let(p[1]),Id(p[2]),Equal(p[3]),String(p[4]),PuntoComa(p[5]),"VariableDef2_3")


#-----------------------------------------EXPRESIONES-----------------------------------

def p_expresion1(p):

    '''expresion : INTEGER expresion'''

    p[0] = expresion1(Integer(p[1]),p[2],"expresion1")

def p_expresion2(p):

    '''expresion : STRING expresion'''

    p[0] = expresion2(String(p[1]),p[2],"expresion2")


def p_expresion3(p):
    
    '''expresion : funcion expresion'''

    p[0] = expresion3(p[1],p[2],"expresion3")


def p_expresion4(p):
    
    '''expresion : ID expresion'''

    p[0] = expresion4(Id(p[1]),p[2],"expresion4")



def p_expresion5(p):
    
    '''expresion : condicion expresion'''

    p[0] = expresion5(p[1],p[2],"expresion5")


def p_expresion6(p):
    
    '''expresion : operador expresion'''

    p[0] = expresion6(p[1],p[2],"expresion6")

def p_expresion7(p):
    
    '''expresion : main'''

    p[0] = expresion7(p[1],"expresion7")

def p_expresionEmpty(p):
    
    '''expresion : empty empty'''

    p[0] = Null()



#----------------------------------------------OPERADORES--------------------------------

def p_operador1(p):

    '''operador : SUMA'''

    p[0] = operador1(Suma(p[1]),"operador1")

def p_operador2(p):

    '''operador : RESTA'''

    p[0] = operador2(Resta(p[1]),"operador2")

def p_operador3(p):

    '''operador : MULTIPLICA'''

    p[0] = operador3(Multiplica(p[1]),"operador3")

def p_operador4(p):

    '''operador : DIVIDE'''

    p[0] = operador4(Divide(p[1]),"operador4")

def p_operador5(p):

    '''operador : POTENCIA'''

    p[0] = operador5(Potencia(p[1]),"operador5")



#-----------------------------------------------FUNCTIONS-------------------------------------

def p_funcion1(p):

    '''funcion : Opera'''

    p[0] = funcion1(p[1],"funcion1")


def p_funcion2(p):

    '''funcion : Move'''

    p[0] = funcion2(p[1],"funcion2")


def p_funcion3(p):

    '''funcion : Delay'''

    p[0] = funcion3(p[1],"funcion3")

def p_funcion4(p):

    '''funcion : If'''

    p[0] = funcion4(p[1],"funcion4")

def p_funcion5(p):

    '''funcion : While'''

    p[0] = funcion5(p[1],"funcion5")


def p_funcion6(p):

    '''funcion : For'''

    p[0] = funcion6(p[1],"funcion6")


def p_funcion7(p):

    '''funcion : Loop'''

    p[0] = funcion7(p[1],"funcion7")


def p_funcion8(p):

    '''funcion : Println'''

    p[0] = funcion8(p[1],"funcion8")

    
def p_funcion9(p):

    '''funcion : Else'''

    p[0] = funcion9(p[1],"funcion9")




#----------------------------------------CONDICIONES-------------------------------------


def p_condicion1(p):

    '''condicion : Igual expresion'''

    p[0] = condicion1(p[1],p[2],"condicion1")
    
def p_condicion2(p):

    '''condicion : Diferente expresion'''

    p[0] = condicion2(p[1],p[2],"condicion2")


def p_condicion3(p):

    '''condicion : Mayor expresion'''

    p[0] = condicion3(p[1],p[2],"condicion3")

def p_condicion4(p):

    '''condicion : Menor expresion'''

    p[0] = condicion4(p[1],p[2],"condicion4")


def p_condicion5(p):

    '''condicion : Mayorigual expresion'''

    p[0] = condicion5(p[1],p[2],"condicion5")

def p_condicion6(p):

    '''condicion : Menorigual expresion'''

    p[0] = condicion6(p[1],p[2],"condicion6")





#----------------------------------- IGUAL-------------------------------------------------

BoolCondicion = False

def p_Igual1(p):

    '''Igual : INTEGER IGUAL INTEGER'''

    global BoolCondicion
    if p[1] == p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Igual1(Integer(p[1]),IGUAL(p[2]),Integer(p[3]),"Igual1")

    #print (p[0])

def p_Igual2(p):

    '''Igual : ID IGUAL ID'''

    global BoolCondicion
    if p[1] == p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Igual2(Id(p[1]),IGUAL(p[2]),Id(p[3]),"Igual2")    

    #print (p[0])

def p_Igual3(p):

    '''Igual : INTEGER IGUAL ID'''

    global BoolCondicion
    if p[1] == p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Igual3(Integer(p[1]),IGUAL(p[2]),Id(p[3]),"Igual3")    

    #print (p[0])

def p_Igual4(p):
    '''Igual : ID IGUAL INTEGER'''

    global BoolCondicion
    if p[1] == p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Igual4(Id(p[1]),IGUAL(p[2]),Integer(p[3]),"Igual4")    

    #print (p[0])
#------------------------------------DIFERENTE------------------------------------------------


def p_Diferente1(p):

    '''Diferente : INTEGER DIFERENTE INTEGER'''

    global BoolCondicion
    if p[1] != p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False
    
    p[0] = Diferente1(Integer(p[1]),DIFERENTE(p[2]),Integer(p[3]),"Diferente1")

def p_Diferente2(p):

    '''Diferente : ID DIFERENTE ID'''

    global BoolCondicion
    if p[1] != p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Diferente2(Id(p[1]),DIFERENTE(p[2]),Id(p[3]),"Diferente2")    

def p_Diferente3(p):

    '''Diferente : INTEGER DIFERENTE ID'''

    global BoolCondicion
    if p[1] != p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Diferente3(Integer(p[1]),DIFERENTE(p[2]),Id(p[3]),"Diferente3")

def p_Diferente4(p):

    '''Diferente : ID DIFERENTE INTEGER'''

    global BoolCondicion
    if p[1] != p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Diferente4(Id(p[1]),DIFERENTE(p[2]),Integer(p[3]),"Diferente4")
#------------------------------------MAYOR------------------------------------------------

def p_Mayor1(p):

    '''Mayor : INTEGER MAYOR INTEGER'''
    
    global BoolCondicion
    if p[1] > p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayor1(Integer(p[1]),MAYOR(p[2]),Integer(p[3]),"Mayor1")

    #print(p[0])

def p_Mayor2(p):

    '''Mayor : ID MAYOR ID'''
    
    global BoolCondicion
    if p[1] > p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False
    
    p[0] = Mayor2(Id(p[1]),MAYOR(p[2]),Id(p[3]),"Mayor2")

    #print(p[0])

def p_Mayor3(p):

    '''Mayor : INTEGER MAYOR ID'''
    
    global BoolCondicion
    if p[1] > p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayor3(Integer(p[1]),MAYOR(p[2]),Id(p[3]),"Mayor3")

    #print(p[0])

def p_Mayor4(p):

    '''Mayor : ID MAYOR INTEGER'''
    
    global BoolCondicion
    if p[1] > p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayor4(Id(p[1]),MAYOR(p[2]),Integer(p[3]),"Mayor4")

    #print(p[0])

#---------------------------------MENOR---------------------------------------------------

def p_Menor1(p):

    '''Menor : INTEGER MENOR INTEGER'''

    global BoolCondicion
    if p[1] < p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menor1(Integer(p[1]),MENOR(p[2]),Integer(p[3]),"Menor1")

    #print(p[0])

def p_Menor2(p):

    '''Menor : ID MENOR ID'''

    global BoolCondicion
    if p[1] < p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menor2(Id(p[1]),MENOR(p[2]),Id(p[3]),"Menor2")

    #print(p[0])

def p_Menor3(p):

    '''Menor : INTEGER MENOR ID'''

    global BoolCondicion
    if p[1] < p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menor3(Integer(p[1]),MENOR(p[2]),Id(p[3]),"Menor3")

    #print(p[0])

def p_Menor4(p):

    '''Menor : ID MENOR INTEGER'''

    global BoolCondicion
    if p[1] < p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menor4(Id(p[1]),MENOR(p[2]),Integer(p[3]),"Menor4")

    #print(p[0])

#-----------------------------------MAYORIGUAL-------------------------------------------------


def p_Mayorigual1(p):

    '''Mayorigual : INTEGER MAYORIGUAL INTEGER'''

    global BoolCondicion
    if p[1] >= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayorigual1(Integer(p[1]),MAYORIGUAL(p[2]),Integer(p[3]),"Mayorigual1")

    #print(p[0])


def p_Mayorigual2(p):

    '''Mayorigual : ID MAYORIGUAL ID'''

    global BoolCondicion
    if p[1] >= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayorigual2(Id(p[1]),MAYORIGUAL(p[2]),Id(p[3]),"Mayorigual2")

    #print(p[0])

def p_Mayorigual3(p):

    '''Mayorigual : INTEGER MAYORIGUAL ID'''

    global BoolCondicion
    if p[1] >= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayorigual3(Integer(p[1]),MAYORIGUAL(p[2]),Id(p[3]),"Mayorigual3")

    #print(p[0])

def p_Mayorigual4(p):

    '''Mayorigual : ID MAYORIGUAL INTEGER'''
    
    global BoolCondicion
    if p[1] >= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Mayorigual4(Id(p[1]),MAYORIGUAL(p[2]),Integer(p[3]),"Mayorigual4")

    #print(p[0])


#----------------------------------------MENORIGUAL--------------------------------------------
def p_Menorigual1(p):

    '''Menorigual : INTEGER MENORIGUAL INTEGER'''

    global BoolCondicion
    if p[1] <= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menorigual1(Integer(p[1]),MENORIGUAL(p[2]),Integer(p[3]),"Menorigual1")

    #print(p[0])



def p_Menorigual2(p):

    '''Menorigual : ID MENORIGUAL ID'''

    global BoolCondicion
    if p[1] <= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menorigual2(Id(p[1]),MENORIGUAL(p[2]),Id(p[3]),"Menorigual2")

    #print(p[0])


def p_Menorigual3(p):

    '''Menorigual : INTEGER MENORIGUAL ID'''

    global BoolCondicion
    if p[1] <= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menorigual3(Integer(p[1]),MENORIGUAL(p[2]),Id(p[3]),"Menorigual3")

    #print(p[0])



def p_Menorigual4(p):

    '''Menorigual : ID MENORIGUAL INTEGER'''

    global BoolCondicion
    if p[1] <= p[3]:
        BoolCondicion = True
    else:
        BoolCondicion = False

    p[0] = Menorigual4(Id(p[1]),MENORIGUAL(p[2]),Integer(p[3]),"Menorigual4")

    #print(p[0])







#------------------------------------FUNCTIONS TYPES------------------------------------------------
def p_Opera(p):
    '''
    Opera : OPERA LPAREN operador COMA expresion COMA expresion RPAREN PUNTOCOMA
    '''

    #Programar If's
    resultado = 0
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

    p[0] = Opera(OPERA(p[1]),LPAREN(p[2]),p[3],COMA(p[4]),p[5],COMA(p[6]),p[7],RPAREN(p[8]),PuntoComa(p[9]),"Opera")
    
    print(resultado)


#--------------------------------------------------------------------------
def p_Move(p):

    '''
    Move : MOVE LPAREN ID RPAREN PUNTOCOMA
    '''

    p[0] = p[3]

    if p[3] == "p":
        #write_read("1")
        print("Moviendo pulgar")

    elif p[3] == "i":
        #write_read("2")
        print("Moviendo índice")

    elif p[3] == "c":
        #write_read("3")
        print ("Moviento centro")

    elif p[3] == "a":
        #write_read("4")
        print ("Moviendo anular")

    elif p[3] == "m":
        #write_read("5")
        print ("Moviendo meñique")
    else:
        print("Error, no es un dedo " + str(p[2]))

    p[0] = Move(MOVE(p[1]),LPAREN(p[2]),Id(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Move")



#--------------------------------------------------------------------------


def p_Delay(p):
    '''
    Delay : DELAY LPAREN INTEGER COMA STRING RPAREN PUNTOCOMA
    '''

    if p[5] == "mili":
        time.sleep(p[3]/1000)
        print("Delay en milisegundos")
        
    elif p[5] == "seg":
        time.sleep(p[3])
        print("Delay en segundos")
        
    elif p[5] == "min":
        time.sleep(p[3]*60)
        print("Delay en minutos")

    elif type(p[3]) != int:
        errores.append(f'Error semántico: el valor de delay no es un número')

    p[0]= Delay(DELAY(p[1]),LPAREN(p[2]),Integer(p[3]),COMA(p[4]),String(p[5]),RPAREN(p[6]),PuntoComa(p[7]),"Delay")

#--------------------------------------------------------------------------


def p_If1(p):

    '''
    If : IF condicion LLAVEL cuerpo_if LLAVER
    '''
    print(type(p[4]))
    print(BoolCondicion)
    if BoolCondicion:
        print("Entro al if")
    else:
        pass

    p[0] = If1(IF(p[1]),p[2],LLAVEL(p[3]),p[4],LLAVER(p[5]),"If1")

#--------------------------------------------------------------------------

def p_Else(p):

    '''
    Else : ELSE LLAVEL cuerpo LLAVER
    '''
    p[0] = Else(ELSE(p[1]),LLAVEL(p[2]),p[3],LLAVER(p[4]),"Else")
    #print(p[2])

#--------------------------------------------------------------------------
def p_While(p):
    '''
    While : WHILE LPAREN  condicion  RPAREN LLAVEL cuerpo LLAVER
    '''
    p[0]= While(WHILE(p[1]),LPAREN(p[2]),p[3],RPAREN(p[4]),LLAVEL(p[5]),p[6],LLAVER(p[7]),"While")
    #Programar if's
    
#--------------------------------------------------------------------------   

def p_For(p):

    '''
    For : FOR ID IN INTEGER PUNTOS INTEGER LLAVEL expresion LLAVER
    '''
    p[0]= For(FOR(p[1]),Id(p[2]),IN(p[3]),Integer(p[4]),PUNTOS(p[5]),Integer(p[6]),LLAVEL(p[7]),p[8],LLAVER(p[9]),"For")
    #Programar if's

#--------------------------------------------------------------------------


def p_Loop(p):
    '''
    Loop : LOOP LLAVEL cuerpo LLAVER
    '''
    p[0] = Loop(LOOP(p[1]),LLAVEL(p[2]),p[3],LLAVER(p[4]),"Loop")
    #Programar if's

#--------------------------------------------------------------------------


def p_Println1(p):
    '''
    Println : PRINTLN LPAREN STRING RPAREN PUNTOCOMA
            
    '''

    prints.append(p[3])

    print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),String(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")

def p_Println2(p):
    '''
    Println : PRINTLN LPAREN INTEGER RPAREN PUNTOCOMA
            
    '''

    prints.append(p[3])

    print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),Integer(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")


def p_Println3(p):
    '''
    Println : PRINTLN LPAREN ID RPAREN PUNTOCOMA
            
    '''

    for i in range(len(variables)):
        if variables[i-1] == p[3]:
            prints.append(valores[i-1])      

    print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),Id(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")

def p_Println4(p):
    '''
    Println : PRINTLN LPAREN BOOLEAN RPAREN PUNTOCOMA
            
    '''

    prints.append(p[3])

    print(prints)

    p[0] = Println(PRINTLN(p[1]),LPAREN(p[2]),Boolean(p[3]),RPAREN(p[4]),PuntoComa(p[5]),"Println")

    
#--------------------------------------------------------------------------


def p_main(p):
    '''
    main : MAIN LPAREN RPAREN PUNTOCOMA
            
    '''

    #p[0] = p[3]

    p[0] = main(MAIN(p[1]),LPAREN(p[2]),RPAREN(p[3]),PuntoComa(p[4]),"main")
    #print(p[3])

#------------------------------------------EMPTY & ERRORS------------------------------------------

def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'
    
    

def p_error(p):
    if p:
        errores.append(f'Syntax error in line {p.lineno} in {p.value} token')
    print(p.lineno)



#---------------------------------------------CALL RUNNER----------------------------------------

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + "." + file)
        cont = cont + 1

    while respuesta == False:
         numArchivo = input('\nNumero del test: ')
         for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]


def traducir(result):
    graphFile = open('graphviztrhee.vz','w')
    graphFile.write(result.traducir())
    graphFile.close()
    print ("El programa traducido se guardo en \"graphviztrhee.vz\"")


def sintacticAnalizer(cadena):
    parser = yacc.yacc()   
    result = parser.parse(cadena)
    result.imprimir(" ")
    #print(result.traducir())
    traducir(result)

def showAst(cadena):
    parser = yacc.yacc()   
    result = parser.parse(cadena)
    show = result.imprimir(" ")
    return show 
