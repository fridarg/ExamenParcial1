#Frida Rangel
#A01651385
#Problema 1

#Verificar si el número es primo:

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Función para generar una matriz de m x m con un rango del tamaño de la matriz

def generar_matriz_primos(matrixsize):
    matrix = []
    count = 0
    num = 2
    
# Insertar en la matriz los numeros primero

    while count < matrixsize * matrixsize:
        if es_primo(num):
            count += 1
            matrix.append(num)
        num += 1
   
# Convertir la lista de números primos en una matriz m x m

    return [matrix[i:i+matrixsize] for i in range(0, len(matrix), matrixsize)]


# Función para imprimir matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join([str(x) for x in fila]))



# Función para calcular la suma de los elementos en y por encima de la diagonal principal
def suma_diagonal_y_superior(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i <= j:
                suma += matriz[i][j]
    return suma


# Función que ejecuta el programa
def main():
    # Solicitar al usuario el tamaño de la matriz
    matrixsize = int(input("Introduzca el tamaño de la matriz cuadrada (mxm):"))

    # Verificar si el tamaño de la matriz es mayor o igual a 3
    if matrixsize < 3:
        print("La dimensión debe ser mayor o igual a 3.")
        return
# Generar la matriz de números primos
    matriz_primos = generar_matriz_primos(matrixsize)
    
# Imprimir la matriz de números primos
    print("Matriz de primos:")
    imprimir_matriz(matriz_primos)
    
# Calcular y mostrar la suma de los elementos en y por encima de la diagonal principal
    
    suma = suma_diagonal_y_superior(matriz_primos)
    print("Suma de los elementos en y por encima de la diagonal principal:", suma)
    
    
# Ejecutar la función principal
if __name__ == "__main__":
    main()
