from RecursionIzquierda import RecursionIzquierda
from primeros import Primeros 
if __name__ == "__main__":
    re= RecursionIzquierda()
    primeros=Primeros();
    lista={"LE":["R","|","F","|","R"],
    "E":["s","*","l","E"],
    "F":["4","|","6",],
    "R":["i","|","E","F"]}
    terminales=["s","*","l","4","6","i"]
    noTerminales=["LE","F","R","E"]
    
    re.recursion(lista);
    primeros.hallarPrimeros(lista)

    
