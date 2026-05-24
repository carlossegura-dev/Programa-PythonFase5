# VIDEOTECA DIGITAL - PROBLEMA 4
# Matriz con al menos 7 títulos
# Formato: [Título, Año de Lanzamiento, Calificación (1-10), Género]

videoteca = [
    ["Dune: Part Two", 2024, 8.5, "Ciencia Ficción"],
    ["Oppenheimer", 2023, 8.9, "Drama"],
    ["The Nun II", 2023, 5.4, "Terror"],
    ["Avatar", 2009, 7.8, "Ciencia Ficción"],
    ["Everything Everywhere", 2022, 7.9, "Comedia"],
    ["Black Adam", 2022, 5.9, "Acción"],
    ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
    ["Pobres Criaturas", 2023, 8.0, "Drama"],
]

# Contar títulos que cumplen criterios
def contar_titulos(matriz, umbral_calificacion, anio_limite):
    conteo = 0
    for pelicula in matriz:
        titulo      = pelicula[0]
        año        = pelicula[1]
        calificacion = pelicula[2]
        if calificacion >= umbral_calificacion and año >= anio_limite:
            conteo += 1
    return conteo

# Parametros de busqueda
UMBRAL_CALIFICACION = 7.5
AÑO_LIMITE         = 2022

# Salida 
print("=" * 45)
print("         VIDEOTECA DIGITAL")
print("=" * 45)
print(f"  Criterios aplicados:")
print(f"  - Calificación >= {UMBRAL_CALIFICACION}")
print(f"  - Año de lanzamiento >= {AÑO_LIMITE}")
print("=" * 45)

resultado = contar_titulos(videoteca, UMBRAL_CALIFICACION, AÑO_LIMITE)

print(f"\n  Total de títulos populares y recientes: {resultado}")
print("\n" + "=" * 45)