
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
    listacu=[]
    for i in range(len(matriz)):
        
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                listacu.append([i,j])
    return listacu

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

    for i in range(len(resultado)):
        print(f"el numero {n} se encuentra en la posición fila {resultado[i][0]}, columna {resultado[i][1]}")
    
final()