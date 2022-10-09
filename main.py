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
    lista={"LE":["R","F","|","F","|","R"],
    "E":["s","*","l","E"],
    "F":["4","|","6","F"],
    "R":["i","|","E"]}
    terminales=["s","*","l","4","6","i"]
    noTerminales=["LE","F","R","E"]
    
    listaPrimeros=[]
    re.recursion(lista);
    primeros.hallarPrimeros(lista,listaPrimeros)
    Lprimeros= crearPrimeros(listaPrimeros,lista)
    siguientes.siguientes(lista,primeros)





    
