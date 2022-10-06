from lib2to3.pgen2.token import EQEQUAL
from operator import length_hint
import string
from this import d


class RecursionIzquierda:
    def __init__(self):
        self.lista=[{}]

    def hallarRecursion(self,key,diccionario):
        for i in range(len(diccionario)) :
            if (key== diccionario[i]) and(diccionario[i-1]=="|" or i==0):
                print("Hay recursion izquierda" +diccionario[i])        


    def  recursion(self,lista):
        for  lista in lista:
            for key in lista:
                print(key)
                #self.hallarRecursion(key,lista[key])
                

    
    