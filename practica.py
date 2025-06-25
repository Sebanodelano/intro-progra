def calcular_puntos_partido(goles, asistencias, amarillas,rojas):
    suma = 0
    g = 10
    a = 5
    am = -3
    r = -10
    suma = goles*g + asistencias*a + amarillas*am + rojas*r
    return suma

def es_partido_destacado(goles,asistencias,amarillas,rojas):
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

    d1 = es_partido_destacado(g1,a1,am1,r1)
    d2 = es_partido_destacado(g2,a2,am2,r2)
    d3 = es_partido_destacado(g3,a3,am3,r3)

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
    print("\n# Casos de prueba:")

evaluar_jugador_completo(2,1,1,0, 0,2,0,0, 1,0,1,0)
evaluar_jugador_completo(3,0,0,1, 1,1,2,0, 0,3,0,0)
evaluar_jugador_completo(0,0,2,1, 0,1,1,0, 1,1,0,0)

