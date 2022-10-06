from errno import EDEADLK
from lib2to3.pgen2.token import EQEQUAL
from operator import length_hint
import string
from this import d
from tkinter import E


class RecursionIzquierda:
    def __init__(self):
        self.lista=[{}]

    def hallarRecursion(self,key,diccionario):
        for i in range(len(diccionario)):
            if key==diccionario[i] and( diccionario[i-1]=="|" or i==0):
                print("hay recursion en:"+key)
            


    def  recursion(self,lista):
        self.imprimir(lista)
        
        for  lista1 in lista:
            for key in lista1:
                self.hallarRecursion(key,lista1[key])
                
    def imprimir(self,lista):
        for list in lista:
            for key in list:
                print(key+"->",end="")
                for list in list[key]:
                    print(list,end="")
                print()

                

    
    