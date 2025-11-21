# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    pass

          
    #Parte 1: triangulo creciente
     for i in range (1, m + 1):
          print(s * i)
    
    #Parte 2: triangulo decreciente
     for i in range (m - 1, 0, -1):
          print(s * i)
