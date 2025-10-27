# ============================================
# FILE: test_mergesort.py
# ALUMNA: 2598198 - DAPHNE VALERIA MORALES MORENO
# ============================================
"""
Pruebas unitarias para el algoritmo Merge Sort
Ejecuta: python test_mergesort.py
"""

from mergesort import merge_sort, validar_lista_numeros


def test_merge_sort_basico():
    """Pruebas básicas del algoritmo merge_sort."""
    # Caso normal
    assert merge_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]
    print("✅ test_merge_sort_basico - Caso normal pasó")


def test_casos_base():
    """Pruebas de los casos base."""
    # Lista vacía (debe mostrar "Lista vacía" pero retornar lista vacía)
    assert merge_sort([]) == []

    # Lista con un elemento
    assert merge_sort([1]) == [1]
    assert merge_sort([42]) == [42]

    print("✅ test_casos_base - Casos base pasaron")


def test_ordenamientos_varios():
    """Pruebas con diferentes tipos de ordenamiento."""
    # Lista en orden inverso
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Lista ya ordenada
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Lista con elementos repetidos
    assert merge_sort([5, 2, 5, 1, 2]) == [1, 2, 2, 5, 5]

    # Lista con números negativos
    assert merge_sort([3, -1, 4, -2, 0]) == [-2, -1, 0, 3, 4]

    print("✅ test_ordenamientos_varios - Varios casos pasaron")


def test_elementos_especiales():
    """Pruebas con casos especiales."""
    # Todos los elementos iguales
    assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    # Lista con cero
    assert merge_sort([0, 5, -3, 0, 2]) == [-3, 0, 0, 2, 5]

    # Números grandes
    assert merge_sort([1000, 1, 100, 10]) == [1, 10, 100, 1000]

    print("✅ test_elementos_especiales - Casos especiales pasaron")


def test_estabilidad_merge():
    """Prueba que merge mantiene el orden de elementos iguales (estabilidad)."""
    # Aunque merge sort es estable, probamos con elementos iguales
    lista = [(5, 'a'), (2, 'b'), (5, 'c'), (1, 'd')]
    # Convertimos a lista simple para la prueba
    lista_simple = [x[0] for x in lista]
    resultado = merge_sort(lista_simple)
    assert resultado == [1, 2, 5, 5]
    print("✅ test_estabilidad_merge - Estabilidad verificada")


def test_validacion_lista_numeros():
    """Pruebas de la función validar_lista_numeros."""
    # Casos válidos
    assert validar_lista_numeros("1,2,3") == [1, 2, 3]
    assert validar_lista_numeros("5, -2, 0, 10") == [5, -2, 0, 10]
    assert validar_lista_numeros("42") == [42]
    assert validar_lista_numeros("") == []
    assert validar_lista_numeros("   ") == []

    # Casos con espacios
    assert validar_lista_numeros(" 1 , 2 , 3 ") == [1, 2, 3]

    print("✅ test_validacion_lista_numeros - Validaciones pasaron")


def test_errores_validacion():
    """Pruebas de manejo de errores en validación."""
    try:
        validar_lista_numeros("1, abc, 3")
        assert False, "Debería haber fallado con 'abc'"
    except ValueError as e:
        assert "abc" in str(e)

    try:
        validar_lista_numeros("1, 2.5, 3")
        assert False, "Debería haber fallado con '2.5'"
    except ValueError:
        pass  # Esperado

    try:
        validar_lista_numeros("10, 20, tres")
        assert False, "Debería haber fallado con 'tres'"
    except ValueError:
        pass  # Esperado

    print("✅ test_errores_validacion - Manejo de errores pasó")


def test_comparacion_con_sorted():
    """Compara merge_sort con la función sorted de Python."""
    import random

    # Generar listas aleatorias y comparar
    for _ in range(10):  # 10 pruebas aleatorias
        tamaño = random.randint(0, 20)
        lista_aleatoria = [random.randint(-100, 100) for _ in range(tamaño)]

        resultado_merge = merge_sort(lista_aleatoria)
        resultado_sorted = sorted(lista_aleatoria)

        assert resultado_merge == resultado_sorted, f"Falló con: {lista_aleatoria}"

    print("✅ test_comparacion_con_sorted - 10 pruebas aleatorias pasaron")


def test_rendimiento_pequeno():
    """Pruebas de rendimiento con listas pequeñas."""
    import time

    # Lista de 100 elementos
    lista_grande = list(range(100, 0, -1))  # Lista en orden inverso

    inicio = time.time()
    resultado = merge_sort(lista_grande)
    fin = time.time()

    assert resultado == list(range(1, 101))
    assert fin - inicio < 1.0  # Debe tomar menos de 1 segundo

    print(f"✅ test_rendimiento_pequeno - Rendimiento aceptable: {fin - inicio:.4f}s")


def test_propiedades_ordenamiento():
    """Prueba propiedades matemáticas del ordenamiento."""
    # La longitud debe mantenerse
    lista = [5, 2, 8, 1, 9]
    resultado = merge_sort(lista)
    assert len(resultado) == len(lista)

    # Todos los elementos de la original deben estar en el resultado
    for elemento in lista:
        assert elemento in resultado

    # El resultado debe estar ordenado
    for i in range(len(resultado) - 1):
        assert resultado[i] <= resultado[i + 1]

    print("✅ test_propiedades_ordenamiento - Propiedades verificadas")


def test_casos_borde():
    """Pruebas de casos borde adicionales."""
    # Un solo elemento negativo
    assert merge_sort([-5]) == [-5]

    # Lista con muchos elementos iguales
    assert merge_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]

    # Lista alternando positivo/negativo
    assert merge_sort([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]

    # Lista con máximo y mínimo de enteros
    assert merge_sort([2147483647, -2147483648, 0]) == [-2147483648, 0, 2147483647]

    print("✅ test_casos_borde - Casos borde pasaron")


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas y muestra resultados."""
    print("=" * 60)
    print("INICIANDO PRUEBAS DE MERGE SORT")
    print("ALUMNA: 2598198 - DAPHNE VALERIA MORALES MORENO")
    print("=" * 60)

    # Lista de todas las funciones de prueba
    pruebas = [
        test_merge_sort_basico,
        test_casos_base,
        test_ordenamientos_varios,
        test_elementos_especiales,
        test_estabilidad_merge,
        test_validacion_lista_numeros,
        test_errores_validacion,
        test_comparacion_con_sorted,
        test_rendimiento_pequeno,
        test_propiedades_ordenamiento,
        test_casos_borde,
    ]

    pruebas_pasadas = 0
    pruebas_totales = len(pruebas)

    for prueba in pruebas:
        try:
            prueba()
            pruebas_pasadas += 1
        except Exception as e:
            print(f"❌ {prueba.__name__} falló: {e}")

    print("\n" + "=" * 60)
    print("RESUMEN DE PRUEBAS")
    print("=" * 60)
    print(f"Pruebas pasadas: {pruebas_pasadas}/{pruebas_totales}")

    if pruebas_pasadas == pruebas_totales:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON!")
    else:
        print(f"⚠️  {pruebas_totales - pruebas_pasadas} pruebas fallaron")

    print("=" * 60)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
