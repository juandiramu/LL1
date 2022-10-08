from errno import EDEADLK
from lib2to3.pgen2.token import EQEQUAL
from operator import length_hint
from this import d
from tkinter import E


class RecursionIzquierda:
    def __init__(self):
        self.lista=[{}]

    def hallarRecursion(self,key,lista,lista1):
        lista1[key]=lista
        for i in range(len(lista)):
            if key==lista[i] and( lista[i-1]=="|" or i==0):
                print("hay recursion izquierda en:"+key)
                self.eliminarRecursion(key,lista)
                
            

    def eliminarRecursion(self,key,lista):
        diccionario=[]
        deriva=[]

        for i in range(len(lista)):
            if lista[i]=="|":
                diccionario.append(deriva)
                diccionario.append(key+"'")
                deriva=[]
            if lista[i]!=key:
                deriva.append(lista[i])
        diccionario.append(deriva)
        print(diccionario)




    def  recursion(self,lista):
        self.imprimir(lista)
        diccionario1={}
        for key in lista.keys():
            self.hallarRecursion(key,lista[key],diccionario1)
        self.imprimir(diccionario1)
    
        
        
                
    def imprimir(self,lista):
        for key in lista.keys():
            print(key+"->",end="")
            for l in lista[key]:
                 print(l,end="")
            print()

                

    
    