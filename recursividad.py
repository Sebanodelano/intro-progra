def barra_progreso(porcentaje):
    if 0 <= porcentaje <= 100:
        completado = "#" * porcentaje       # Caracteres completados
        restante = "-" * (100 - porcentaje) # Caracteres restantes
        print(f"[{completado}{restante}] {porcentaje}%")
    else:
        print("El número debe estar entre 0 y 100.")


def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    
def combinacion(n, x):
    if x > n:
        return 0 # el numero de arriba siempre debe ser mayor al de abajo o igual
    else:
        return factorial(n) / (factorial(x) * factorial(n-x))
    
print(combinacion(10,5))




def temperatura(x):
    faren = ((x) * 9/5) + 32
    return faren
def resultado(x):
    f = temperatura(x)
    print("La conversion es " , f , "grados")
resultado(32)


def validar(n):
    if 0 <= n <= 20:
        return True
    else:
        return False
    
def promedio(aprobados, sumapro,desaprobados,sumadespro , mayores_15):
    if aprobados >0:
        print("el promedio de aprobados es: " , sumapro / aprobados)
    else:
        print("No hubo aprobados")
    if desaprobados > 0:
        print("El promedio de desaprobados es: ", sumadespro / desaprobados)
    else:
        print("No hubo desaprobados")
    print("la cantidad de alumnos con nota mayor a 15 es " , mayores_15)

def notas():    

    mayores_15= 0
    aprobados = 0
    sumapro = 0
    desaprobados = 0
    sumadespro = 0
    nota = 1
    while nota != 0:
        nota = int(input("Escriba la nota del 1 al 20 y 0 para acabar: "))
        
        if validar(nota):
            if nota >= 11:
                sumapro = sumapro + nota
                aprobados = aprobados + 1
            else:
                sumadespro = sumadespro + nota
                desaprobados = desaprobados + 1
            if nota > 15:
                mayores_15 = mayores_15 + 1
        elif nota !=0:
            print("Nota no valida debe estar entar entre 1 y 20: ")
    promedio(aprobados, sumapro, desaprobados, sumadespro, mayores_15)
notas()




def invertir(n,x= 0):
    if 0 <= n <= 9:
        return "Un numero de un digito no se puede invertir"
    else:
        return n%10 , invertir(n= n//10 , x= x*10 +n%10)
invertir(123)
    