def matriz():
    matriz = []

    for i in range(4):
        fila= []
        print(f"ingrese los 4 numeros de la fila {i+1}: ")
        
        for j in range (4):
            num = int(input(f"ingrese numero en posición [{i+1},{j+1}]:  "))
            fila.append(num)
        matriz.append(fila)
        
        print("la matriz ingresada es: ")
        for fila in matriz:
            for num in fila:
                print(num, end=" ")
            print( )
#ahora quiero empezar a contar pares:
    pares = 0
    for fila in matriz:
        for num in fila:
            if num%2 ==0 and num !=0:
                pares += 1
    print(f"La cantidad de numeros pares es {pares} ")
#ahora quiero contar impares
    impares = 0
    for fila in matriz:
        for num in fila:
            if num%2 != 0 and num !=0:
                impares +=1
    print(f"La cantidad de numeros impares es {impares} ")



import random
def matrizloca(filas, columnas):
    matriz=[]
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            num = random.randint(15,45)
            fila.append(num)
        matriz.append(fila)
    return matriz


def buscarmatriz(matriz, numero):
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return (i, j)
    return 0

def final():
    filas = int(input("Escriba el numero de filas: "))
    columnas= int(input("Escriba el numero de columnas: "))

    matz= matrizloca(filas, columnas)

    print("Matriz generada: ")
    for fila in  matz:
        for num in fila:
            print(num , end =" ")
        print()
    n = int(input("Que numero quieres buscar: "))

    resultado = buscarmatriz(matz , n)

    if resultado !=0:
        print(f"el numero {n} se encuentra en la posición fila {resultado[0]}, columna {resultado[1]}")
    else:
        print("El numero no se encuentra en la matriz")
final()
import random
def matriz_cuadrada(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            num = random.randint(1,100)
            fila.append(num)
        matriz.append(fila)
    return matriz

def principal():
    n = int(input("Escriba de el tamaño de la matriz (n x n): "))
    matz = matriz_cuadrada(n)
    for fila in matz:
        for num in fila:
            print(num, end=" ")
        print()

    matztrans=[]

    for j in range(len(matz)):
        nueva_fila=[]
        for i in range(len(matz)):
            nueva_fila.append(matz[i][j])
        matztrans.append(nueva_fila)

    print("\nMatriz transpuesta:")
    for fila in matztrans:
        for num in fila:
            print(num, end=" ")
        print()

import random
def problema4():
    matriz=[]
    for filas in range(3):
        fila = []
        for j in range(4):
            numero = random.randint(1,10)
            fila.append(numero)
        matriz.append(fila)

    for fila in matriz:
        for numero in fila:
            print(numero , end=" ")
        print()
    return matriz
def matsuma():
    matz = problema4()
    suma=[]
    for i in range(len(matz)):
        sumafila= 0
        for j in range(len(matz[0])):
            sumafila = sumafila + matz[i][j]
        suma.append(sumafila)
    print(suma)
matsuma()    







