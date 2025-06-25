def resultado():
    goles_peru=int(input("goles p"))
    goles_ecuador=int(input("goles e"))




    for i in range (1 , 10):
        for j in range(1 , 16):
            if j <=5:
                print("🟥" , end= "")
            elif 5< j <=10:
                print("⬜" , end= "")
            else:
                print("🟥", end= "")
        if i == 5:
            
            print(" " f"{goles_peru} - {goles_ecuador}", end="")
        else:
            print(" "*6, end ="")
        if i <= 4:
            print("🟨"*15, end="")
        elif 4 < i <=7:
            print("🟦"*15, end="")
        else:
            print("🟥"*15 , end="")
        print()


#examen pregunta 2

def sumadiv(n):
    i = 1
    suma= 0
    while i <= n:
        if n % i == 0:
            suma = suma + i
        i += 1
    return suma


def amigos(x,y):
    if sumadiv(x) == sumadiv(y):
        return True
    else:
        return False

print(amigos(220,284))


#pregunta 3


def calcular_puntos_partido(goles, asistencias, amarillas,rojas):
    g = 10
    a = 5
    am = -5
    r = -10
    return goles*g + asistencias*a + amarillas*am + rojas*r
    

def partido_destacado(goles,asistencias,amarillas,rojas):
    puntos = calcular_puntos_partido(goles, asistencias, amarillas,rojas)
    if puntos >= 15 and rojas ==0:
        return "Partido destacado"
    else:
        return "Partido normal"
    
def calcular_promedio(suma_puntos , numero_partidos):
    return suma_puntos / numero_partidos

def determinar_categoria(promedio_puntos):
    if promedio_puntos < 0:
        return "Necesita mejorar"
    elif 0 <= promedio_puntos <= 4:
        return "Reserva"
    elif 5 <= promedio_puntos <=9:
        return "Suplente"
    elif 10 <= promedio_puntos <=14:
        return "Titular"
    else:
        return "Estrella"
    
def evaluar_jugador_completo(g1,a1,am1,r1, g2,a2,am2,r2, g3,a3,am3,r3):
    p1 = calcular_puntos_partido(g1,a1,am1,r1)
    p2 = calcular_puntos_partido(g2,a2,am2,r2)
    p3 = calcular_puntos_partido(g3,a3,am3,r3)

    d1 = partido_destacado(g1,a1,am1,r1)
    d2 = partido_destacado(g2,a2,am2,r2)
    d3 = partido_destacado(g3,a3,am3,r3)

    total = p1 + p2 + p3
    promedio = calcular_promedio (total , 3)

    categoria = determinar_categoria(promedio)

    destacados = 0
    if d1 == "Partido destacado":
        destacados = destacados + 1
    if d2 =="Partido destacado":
        destacados = destacados + 1
    if d3 == "Partido destacado":
        destacados = destacados + 1

    print("📊 EVALUACIÓN DEL JUGADOR:")
    print(f"Partido 1: {p1} puntos → {d1}")
    print(f"Partido 2: {p2} puntos → {d2}")
    print(f"Partido 3: {p3} puntos → {d3}")
    print("\n📈 RESUMEN:")
    print(f"- Puntos totales: {total}")
    print(f"- Promedio por partido: {promedio}")
    print(f"- Categoría: \"{categoria}\"")
    print(f"- Partidos destacados: {destacados} de 3")


def cant_digitos(n):
    digitos = 0
    while n != 0:
        n = n//10
        digitos = digitos + 1
    return digitos

def es_capicuas(n):
    if n < 0:
        return False
    if n <10:
        return True
    digitos = cant_digitos(n)
    primer_digito = n //10**(cant_digitos - 1)
    ultimo_digito = n%10
    
    if primer_digito != ultimo_digito:
        return False
    else:
        numero_medio= (n%10**(digitos-1))//10
    return es_capicua(numero_medio)


def cantidad_digitos(n):
    digitos = 0
    while n != 0:
        n //10 
        digitos = digitos + 1
    return digitos

def es_capicua(n):
    if n <0:
        return False
    if n < 10:
        return True
    digitos = cant_digitos(n)
    primer_digito = n // 10 ** (digitos - 1)
    ultimo_digito = n % 10
    if primer_digito != ultimo_digito:
        return False
    else:
        numero_medio= (n% 10**(digitos-1)//10)
    return es_capicua(numero_medio)

if es_capicua(2332):
    print("Es capicua")
else:
    print("No es capicua")

        
    