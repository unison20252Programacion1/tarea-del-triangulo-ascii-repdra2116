# En este archivo debes implementar la función

def triangulo_simetrico(m: int, s: str) -> str:
    if m <=0:
        print("Error: La altura debe ser un entero positivo")
        return
        
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    
    # TODO: implementar la lógica para generar el triángulo simétrico en ASCII

    #Parte 1: triangulo creciente
    for i in range (1, M + 1):
        print(s * i)
    
    #Parte 2: triangulo decreciente
    for i in range (m -1, 0 -1):
        print(s * i)
