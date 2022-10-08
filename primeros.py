class Primeros:
    def __init__(self):
        self.lista=[{}]

    def hallarPrimeros(self,diccionario):
        for dic in diccionario.values():
            self.mostrar(dic,diccionario)
            print(dic)
            
    def mostrar(self,dic,diccionario):
        for i in range(len(dic)):
            if i==0:
                print(dic[i]+" Es un primero")
            if i!=0 and dic[i-1]=="|":
                print(dic[i]+" Es un primero")