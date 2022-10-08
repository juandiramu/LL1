from RecursionIzquierda import RecursionIzquierda 
if __name__ == "__main__":
    re= RecursionIzquierda()
    lista={"LE":["LE","|","F","|","R"],
    "E":["s","*","l","E"],
    "F":["4","|","6","|","F"],
    "R":["i","|","E","F"]}
    terminales=["s","*","l","4","6","i"]
    noTerminales=["LE","F","R","E"]
    
    re.recursion(lista);

    