txt = " "
cont = 0
def incrementar_cont():
    global cont
    cont +=1
    return "%d" %cont

class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'void'
        
    def imprimir(self,ident):
        print (ident + "Nodo Nulo") 

    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id +"[label= "+"nodo_nulo"+"]"+"\n\t"
        
        return id


#-------------------------------------Clases de la gramatica---------------------------------



class Start(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)	

    def traducir(self):
        global txt
        id = incrementar_cont()
        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        return "digraph G{\n\t"+txt+"}"
        return id


#--------------------------------------------------------------------------------------------

class code(Nodo):

    def __init__(self,son1,name):

        self.name = name
        self.son1 = son1


    def imprimir(self,ident):

        

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):

        global txt
        id = incrementar_cont()


        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id



#--------------------------------------------------------------------------------------------


class cuerpo1(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class cuerpo2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class cuerpo3(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2


    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class cuerpo4(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class cuerpo5(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

#--------------------------------------------------------------------------------------------

class cuerpo_if2(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class expresion_if1(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class expresion_if(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcion_if1(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcion_if2(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcion_if3(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcion_if4(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

#--------------------------------------------------------------------------------------------

class cuerpo_else(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class expresion_else1(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class expresion_else(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcion_else1(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcion_else2(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
'''
class funcion_else3(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id
'''
class funcion_else4(Nodo):
    def __init__(self,son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        

    def imprimir(self,ident):
        
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else: 
            self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()
        
        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()
            
        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


#--------------------------------------------------------------------------------------------


class Variable1(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

        

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
    
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)



    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class Variable2(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

        

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
    
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)



    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class VariableDef1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
     

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class VariableDef2_1(Nodo):

    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        


    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)

        self.son5.imprimir(" "+ident)


        print (ident + "Nodo: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else: 
            son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"

        return id



class VariableDef2_2(Nodo):

    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        


    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)

        self.son5.imprimir(" "+ident)


        print (ident + "Nodo: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else: 
            son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"

        return id



class VariableDef2_3(Nodo):

    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        


    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)

        self.son5.imprimir(" "+ident)


        print (ident + "Nodo: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else: 
            son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"

        return id

#--------------------------------------------------------------------------------------------

class expresion1(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

         
        son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class expresion2(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):


        self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

 
        son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class expresion3(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class expresion4(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        
        self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        
        son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class expresion5(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class expresion6(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        

        return id



class expresion7(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        

        return id
#--------------------------------------------------------------------------------------------

class operador1(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id

class operador2(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id



class operador3(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id


class operador4(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id


class operador5(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id

    
#--------------------------------------------------------------------------------------------


class funcion1(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id



class funcion2(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id


class funcion3(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id



class funcion4(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id



class funcion5(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id



class funcion6(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id                        





class funcion7(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id


class funcion8(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id

class funcion9(Nodo):

    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1


    
    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
 

        return id


#--------------------------------------------------------------------------------------------
class condicion1(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class condicion2(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class condicion3(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class condicion4(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class condicion5(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class condicion6(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
            
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else: 
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



#------------------------------Igual-----------------------------------
class Igual1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Igual2(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id



class Igual3(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Igual4(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

#--------------------------------Diferente--------------------------------------------



class Diferente1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id



class Diferente2(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Diferente3(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Diferente4(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id
#--------------------------------Mayor--------------------------------------------
class Mayor1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id 


class Mayor2(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id    


class Mayor3(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id    

class Mayor4(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id               

#--------------------------------Menor--------------------------------------------  

class Menor1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Menor2(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Menor3(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Menor4(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


#--------------------------------Mayorigual--------------------------------------------


class Mayorigual1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Mayorigual2(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Mayorigual3(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Mayorigual4(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

#--------------------------------MenorIgual--------------------------------------------



class Menorigual1(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Menorigual2(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Menorigual3(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class Menorigual4(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)

        print(ident+"Nodo: "+self.name)


    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

#-----------------------------------------------------------------------

 
class Opera(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else: 
            self.son3.imprimir(" "+ident)

        self.son4.imprimir(" "+ident)

        if type(self.son5) == type(tuple()):
            self.son5[0].imprimir(" "+ident)
        else: 
            self.son5.imprimir(" "+ident)

        self.son6.imprimir(" "+ident)

        if type(self.son7) == type(tuple()):
            self.son7[0].imprimir(" "+ident)
        else: 
            self.son7.imprimir(" "+ident)

        self.son8.imprimir(" "+ident)

        self.son9.imprimir(" "+ident)




    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else: 
            son3 = self.son3.traducir()

        son4 = self.son4.traducir()

        if type(self.son5) == type(tuple()):
            son5 = self.son5[0].traducir()
        else: 
            son5 = self.son5.traducir()

        son6 = self.son6.traducir()

        if type(self.son7) == type(tuple()):
            son7 = self.son7[0].traducir()
        else: 
            son7 = self.son7.traducir()
        
        son8 = self.son8.traducir()
        son9 = self.son9.traducir()


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"

        return id

#-----------------------------------------------------------------------

class Move(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)
        

    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"

        return id

#-----------------------------------------------------------------------  

class Delay(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7


    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)
        self.son6.imprimir(" "+ident)
        self.son7.imprimir(" "+ident)

    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()
        son7 = self.son7.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id

#-----------------------------------------------------------------------

class If1(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5


    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else: 
            self.son4.imprimir(" "+ident)

        self.son5.imprimir(" "+ident)




    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        son3 = self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else: 
            son4 = self.son4.traducir()

        son5 = self.son5.traducir()


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"


        return id


class If2(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    
    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else: 
            self.son2.imprimir(" "+ident)

        self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else: 
            self.son4.imprimir(" "+ident)

        self.son5.imprimir(" "+ident)

        self.son6.imprimir(" "+ident)

        self.son7.imprimir(" "+ident)

        if type(self.son8) == type(tuple()):
            self.son8[0].imprimir(" "+ident)
        else: 
            self.son8.imprimir(" "+ident)

        self.son9.imprimir(" "+ident)

    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else: 
            son2 = self.son2.traducir()

        son3 = self.son3.traducir()
        
        if type(self.son4) == type(tuple()):
            son4 = self.son4[0].traducir()
        else: 
            son4 = self.son4.traducir()

        son5 = self.son5.traducir()

        son6 = self.son6.traducir()

        son7 = self.son7.traducir()

        if type(self.son8) == type(tuple()):
            son8 = self.son8[0].traducir()
        else: 
            son8 = self.son8.traducir()

        son9 = self.son9.traducir()
        


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"

        return id

#-----------------------------------------------------------------------

class Else(Nodo):
    def __init__(self,son1,son2,son3,son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        


    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)

        self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else: 
            self.son3.imprimir(" "+ident)

        self.son4.imprimir(" "+ident)





    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else: 
            son3 = self.son3.traducir()

        son4 = self.son4.traducir()



        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        


        return id

#-----------------------------------------------------------------------

class While(Nodo):

    def __init__(self,son1,son2,son3,son4,son5,son6,son7,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7


    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else: 
            self.son3.imprimir(" "+ident)
        
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)
        
        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else: 
            self.son6.imprimir(" "+ident)

        self.son7.imprimir(" "+ident)

    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else: 
            son3 = self.son3.traducir()

        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        if type(self.son6) == type(tuple()):
            son6 = self.son6[0].traducir()
        else: 
            son6 = self.son6.traducir()

        son7 = self.son7.traducir()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id
 
#-----------------------------------------------------------------------   

class For(Nodo):
    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)
        self.son6.imprimir(" "+ident)
        self.son7.imprimir(" "+ident)

        if type(self.son8) == type(tuple()):
            self.son8[0].imprimir(" "+ident)
        else: 
            self.son8.imprimir(" "+ident)

        self.son9.imprimir(" "+ident)




    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()
        son6 = self.son6.traducir()
        son7 = self.son7.traducir()

        if type(self.son8) == type(tuple()):
            son8 = self.son8[0].traducir()
        else: 
            son8 = self.son8.traducir()

        son9 = self.son9.traducir()


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"
        return id


#-----------------------------------------------------------------------

class Loop(Nodo):
    def __init__(self,son1,son2,son3,son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        


    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        
        self.son2.imprimir(" "+ident)
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else: 
            self.son3.imprimir(" "+ident)

        self.son4.imprimir(" "+ident)

        




    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else: 
            son3 = self.son3.traducir()

        son4 = self.son4.traducir()


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id


#-----------------------------------------------------------------------


class Println(Nodo):

    def __init__(self,son1,son2,son3,son4,son5,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5


    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)




    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"


        return id

class main(Nodo):

    def __init__(self,son1,son2,son3,son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4



    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
      




    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        


        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"


        return id


#----------------------------------TERMINALES DE LAS PRODUCCIONES-------------------------------
class Inicio(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"INICIO: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class Fin(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"FIN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class Let(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"LET: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id




class Id(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"ID: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id



class PuntoComa(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"PUNTOCOMA: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id



class Equal(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"EQUAL: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class IGUAL(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"IGUAL: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id



class DIFERENTE(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"DIFERENTE: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class MAYOR(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MAYOR: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class MENOR(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MENOR: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class MAYORIGUAL(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MAYORIGUAL: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class MENORIGUAL(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MENORIGUAL: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Suma(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"SUMA: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Resta(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"Minus: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Multiplica(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MULTIPLICA: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Divide(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"Divide: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class Potencia(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"POTENCIA: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


#----------------------------Tipos de datos------------------------------------

class Integer(Nodo):
    def __init__(self,name):
        self.name = str(name)

    def imprimir(self,ident):
        print (ident+"INTEGER: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Boolean(Nodo):
    def __init__(self,name):
        self.name = str(name)

    def imprimir(self,ident):
        print (ident+"BOOLEAN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class String(Nodo):
    def __init__(self,name):
        self.name = name.strip('"')

    def imprimir(self,ident):
        print (ident+"STRING: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class OPERA(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"OPERA: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class COMA(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"COMA: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class fn(Nodo):

    def __init__(self,son1,son2,son3,son4,son5,son6,son7,son8,son9,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    def imprimir(self,ident):

        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        self.son4.imprimir(" "+ident)
        self.son5.imprimir(" "+ident)

        if type(self.son6) == type(tuple()):
            self.son6[0].imprimir(" "+ident)
        else: 
            self.son6.imprimir(" "+ident)

        self.son7.imprimir(" "+ident)
        self.son8.imprimir(" "+ident)

        if type(self.son9) == type(tuple()):
            self.son9[0].imprimir(" "+ident)
        else: 
            self.son9.imprimir(" "+ident)



    def traducir(self):
        global txt
        id = incrementar_cont()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()
        son5 = self.son5.traducir()

        if type(self.son6) == type(tuple()):
            son6 = self.son6[0].traducir()
        else: 
            son6 = self.son6.traducir()

        son7 = self.son7.traducir()
        son8 = self.son8.traducir()
        
        if type(self.son9) == type(tuple()):
            son9 = self.son9[0].traducir()
        else: 
            son9 = self.son9.traducir()
    

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"

        return id


class MOVE(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MOVE: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class LPAREN(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"LPAREN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class RPAREN(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"RPAREN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class DELAY(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"DELAY: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class ELSE(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"ELSE: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class IF(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"IF: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class MAIN(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"MAIN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class LLAVEL(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"LLAVEL: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class LLAVER(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"LLAVER: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class WHILE(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"WHILE: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class FOR(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"FOR: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id    


class IN(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"IN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id   

class PUNTOS(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"PUNTOS: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id   

class LOOP(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"LOOP: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id   

class PRINTLN(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"PRINTLN: "+self.name)
            
    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id                   

#-----------------------------------------------------------------------------
class empty(Nodo):
    def __init__(self,name):
        self.name = name

    def imprimir(self,ident):
        print("")

    def traducir(self):
        global txt
        id = incrementar_cont()
        return id

class error(Nodo):
    def __init__(self,name):
        self.name = name
    def imprimir(self,ident):
        print("")

    def traducir(self):
        global txt
        id = incrementar_cont()
        return id

    
class FN(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+"FN: "+self.name)

    def traducir(self):
        global txt
        id = incrementar_cont()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return id