class ConjuntoPrediccion:
    def __init__(self):
        self.conjuntos={}

    def conjunto(self,diccionario,primeros,siguientes):
        for key in diccionario.keys():
            self.conjuntos[key]=[]
            if "lamda" in diccionario[key]:
                self.asignar(key,primeros,siguientes,0)
            else:
                self.asignar(key,primeros,siguientes,1)
            print(self.conjuntos[key])
        self.comprobarLl1()
    
    def asignar(self,key,primeros,siguientes,x):
        if x==0:
            for i in primeros[key]:
                self.conjuntos[key].append(i)
            for j in siguientes[key]:
                self.conjuntos[key].append(j)
        else:
             for i in primeros[key]:
                self.conjuntos[key].append(i)

    def comprobarLl1(self):
        repetido = []
        for key in self.conjuntos.keys():
            unico = []
            for x in self.conjuntos[key]:
                if x not in unico:
                    unico.append(x)
                else:
                    if x not in repetido:
                        repetido.append(x)
        if repetido:print("Esta gramatica no es LL1")
        else:print("La gramatica es LL1")
            
        
        
            
                
        