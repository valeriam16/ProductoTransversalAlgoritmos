ALUMNA: 2598198 - DAPHNE VALERIA MORALES MORENO
Este es mi pseudocódigo, para resolver el problema planteado para el desarrollo del proyecto.

Algoritmo: Merge Sort

Entrada: Lista A de números enteros

Salida: Lista A ordenada ascendentemente

FUNCIÓN merge_sort(A)

    // Caso base: si la lista tiene 0 elementos
    SI longitud(A) == 0 ENTONCES
        MOSTRAR "Lista vacía"
    FIN SI

    // Caso base: si la lista tiene 1 elemento
    SI longitud(A) == 1 ENTONCES
        RETORNAR A
    FIN SI

    // Paso 1: Dividir
    medio = longitud(A) // 2
    izquierda = A[0:medio]     // Primera mitad
    derecha = A[medio:]        // Segunda mitad

    // Paso 2: Conquistar (llamadas recursivas)
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    // Paso 3: Combinar
    resultado = merge(izquierda_ordenada, derecha_ordenada)

    RETORNAR resultado
FIN FUNCIÓN

FUNCIÓN merge(izquierda, derecha)

    // Combinar dos listas ordenadas en una sola lista ordenada
    resultado = []
    i = 0, j = 0 // Índices para recorrer izquierda y derecha

    // Comparar elementos de ambas listas
    MIENTRAS i < longitud(izquierda) Y j < longitud(derecha) HACER
        SI izquierda[i] <= derecha[j] ENTONCES
            AGREGAR izquierda[i] AL FINAL de resultado
            i = i + 1
        SINO
            AGREGAR derecha[j] AL FINAL de resultado
            j = j + 1
        FIN SI
    FIN MIENTRAS

    // Agregar elementos restantes de izquierda (si los hay)
    MIENTRAS i < longitud(izquierda) HACER
        AGREGAR izquierda[i] AL FINAL de resultado
        i = i + 1
    FIN MIENTRAS

    // Agregar elementos restantes de derecha (si los hay)
    MIENTRAS j < longitud(derecha) HACER
        AGREGAR derecha[j] AL FINAL de resultado
        j = j + 1
    FIN MIENTRAS

    RETORNAR resultado
FIN FUNCIÓN