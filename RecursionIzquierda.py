from errno import EDEADLK
from lib2to3.pgen2.token import EQEQUAL
from operator import length_hint
from this import d
from tkinter import E


class RecursionIzquierda:
    def __init__(self):
        self.lista={}

    def hallarRecursion(self,key,lista):
        self.lista[key]=[]
        for i in range(len(lista)):
            if key==lista[i] and( lista[i-1]=="|" or i==0):
                self.lista[key+"'"]=[]
                print("hay recursion izquierda en:"+key)
                deriva=self.eliminarRecursion2(key,lista,i)
                self.deriva(deriva,key)
            if not self.lista[key]:  
                self.lista[key]=lista              

    def eliminarRecursion2(self,key,lista,i):
        lista2=[]
        aux=[]
        for j in range(len(lista)):
            if lista[j]=="|" and aux:
                aux.append(key+"'")
                lista2.append(aux)
                aux=[]
            elif lista[j]!=lista[i] and lista[j]!="|":
                print(lista[j])
                aux.append(lista[j])
        aux.append(key+"'")
        lista2.append(aux)
        print(lista2)
        return lista2

    def deriva(self,deriva,key):
        self.lista[key+"'"]
        self.lista[key]=[]
        for der in deriva:
            for d in der:
                self.lista[key].append(d)
            self.lista[key].append("|")
        self.lista[key].pop()
        print(self.lista[key])

    def  recursion(self,lista):
        self.imprimir(lista)
        for key in lista.keys():
            self.hallarRecursion(key,lista[key])
        print("Gramática ya sin recursión izquierda")
        self.imprimir(self.lista)

                
    def imprimir(self,lista):
        for key in lista.keys():
            print(key+"->",end="")
            for l in lista[key]:
                 print(l,end="")
            print()

                

    
    