# En este archivo debes implementar la función
def triangulo_simetrico(m: int, s: str) -> str:
     if m <=0:
        print("Error: La altura debe ser un entero positivo")
        return
          
    #Parte 1: triangulo creciente
     for i in range (1, m + 1):
          print(s * i)
    
    #Parte 2: triangulo decreciente
     for i in range (m - 1, 0, -1):
          print(s * i)
