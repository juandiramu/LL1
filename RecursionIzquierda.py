from errno import EDEADLK
from lib2to3.pgen2.token import EQEQUAL
from operator import length_hint
import string
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
                derivacion=self.eliminarRecursion(key,lista)
                lista1[key]="";
                lista1[key+"'"]={"S"}
            
                #diccionario[key]=self.eliminarRecursion(key,diccionario)

    def eliminarRecursion(self,key,lista):
        deriva=[]
        for i in range(len(lista)):
            deriva.append(9)
        return deriva

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

                

    
    