from RecursionIzquierda import RecursionIzquierda
from primeros import Primeros
from siguientes import Siguientes 
def crearPrimeros(lista,diccionario):
    diccionario2={}
    i=0
    for key in diccionario.keys():
        diccionario2[key]=[lista[i]]
        i+=1;
    return diccionario2

if __name__ == "__main__":
    re= RecursionIzquierda();
    primeros=Primeros();
    siguientes=Siguientes();
    lista={"LE":["R","F","|","F","|","E"],
    "E":["s","*","|","l","R","LE","s"],
    "F":["4","|","6","R","|","t","E"],
    "R":["i","|","E"]}
    
    
    listaPrimeros=[]
    re.recursion(lista);
    primeros.hallarPrimeros(lista,listaPrimeros)
    Lprimeros= crearPrimeros(listaPrimeros,lista)
    print("....Lista primeros...")
    re.imprimir(Lprimeros)
    print("....Lista Siguientes...")
    siguientes.siguientes(lista)





    
