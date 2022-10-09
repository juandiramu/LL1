class Siguientes:
    def __init__(self):
        self.lista=[{}]
    def siguientes(self,diccionario,primeros):
         for dic in diccionario.values():
                self.hallarSiguientes(dic,diccionario,primeros)

    def hallarSiguientes(self,dic, diccionario,primeros):
        listaSiguientes=[]
        bandera=True
        for i in range(len(dic)):
            if i==0  and dic[i+1]!="|":
                for key in diccionario.keys():
                    if dic[i]==key:
                        bandera=False;
                if bandera and dic[i] not in listaSiguientes:
                    print(dic[i+1] +"Es un siguiente")
                    listaSiguientes.append(dic[i+1])                  
                            

            