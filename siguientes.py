from ast import Return
from multiprocessing.spawn import is_forking
from re import S
from this import d
from tkinter.tix import DirSelectBox
from RecursionIzquierda import RecursionIzquierda
from primeros import Primeros


class Siguientes:
    def __init__(self):
        self.primeros=Primeros()
        self.re=RecursionIzquierda()

    def siguientes(self,diccionario):
        siguientes={}
        i=0
        for key in diccionario.keys():
            siguientes[key]=self.hallarSiguientes(key,diccionario,i,siguientes)
            i+=1;
        self.re.imprimir(siguientes)
        return siguientes;

    def hallarSiguientes(self,key,diccionario,contador,dSiguientes):
        bandera=False;
        siguientes=[]
        if contador==0:
            siguientes.append("$")
        for value in diccionario.values():
            for i in range(len(value)):
                if key==value[i]:
                    bandera=True
                    llave=self.enccontrarLlave(value,diccionario)
                    self.casosSiguientes(value,i,diccionario,siguientes,dSiguientes,llave)
                    break;
            if bandera: break
        return siguientes

    def casosSiguientes(self,lista,i,diccionario,siguientes,dSiguientes,llave):
        if i<len(lista)-1:
            for key in diccionario.keys():
                if lista[i+1]==key:
                    resultado=self.primeros.mostrar(lista,diccionario)
                    for r in resultado:
                        siguientes.append(r)
                    return
            if lista[i+1]!="|":
                siguientes.append(lista[i+1])
                return
            else:
                for d in dSiguientes[llave]:
                    siguientes.append(d)
        else:   
            for d in dSiguientes[llave]:
                siguientes.append(d)
        return siguientes


    def enccontrarLlave(self,value,diccionario):
        for key in diccionario.keys():
            if diccionario[key]==value:
                return key


         

   

