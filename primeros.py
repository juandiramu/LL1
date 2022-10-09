class Primeros:
    def __init__(self):
        self.lista=[{}]

    def hallarPrimeros(self,diccionario,lista2):
        lista=[]
        for dic in diccionario.values():
            self.mostrar(dic,diccionario,lista)
            lista2.append(lista)
            lista=[]

            
    def mostrar(self,dic,diccionario,lista=[]):
            bandera=True
            for i in range(len(dic)):
                if i==0:
                    for key in diccionario.keys():
                        if dic[i]==key:
                            bandera=False;
                            self.mostrar(diccionario[key],diccionario,lista)
                    if bandera and dic[i] not in lista:
                        lista.append(dic[i])
                if i!=0 and dic[i-1]=="|":
                    for key in diccionario.keys():
                        if dic[i]==key:
                            bandera=False;
                            self.mostrar(diccionario[key],diccionario,lista)
                    if bandera and dic[i] not in lista:
                        lista.append(dic[i])
            return lista
    