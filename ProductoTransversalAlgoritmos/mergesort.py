# ============================================
# FILE: mergesort.py
# ALUMNA: 2598198 - DAPHNE VALERIA MORALES MORENO
# ============================================
"""
Proyecto: Ordenamiento por Fusión (Merge Sort)
Descripción: Implementación del algoritmo Merge Sort con manejo de lista vacía
y entrada de usuario validada.
"""

from typing import List, Iterable


def merge(izquierda: List[int], derecha: List[int]) -> List[int]:
    """Fusiona dos listas ORDENADAS en una sola lista ORDENADA."""
    i = j = 0
    resultado: List[int] = []

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def merge_sort(A: Iterable[int]) -> List[int]:
    """Retorna una NUEVA lista ordenada ascendente."""
    # Convertir a lista para garantizar manipulación segura
    lista = list(A)

    # Caso base: lista vacía
    if len(lista) == 0:
        print("Lista vacía")
        return lista

    # Caso base: lista con un elemento
    if len(lista) == 1:
        return lista

    # Dividir y conquistar
    medio = len(lista) // 2
    izquierda_ordenada = merge_sort(lista[:medio])
    derecha_ordenada = merge_sort(lista[medio:])

    return merge(izquierda_ordenada, derecha_ordenada)


def validar_lista_numeros(entrada: str) -> List[int]:
    """
    Valida y convierte una cadena de texto en una lista de números enteros.

    Args:
        entrada (str): Cadena con números separados por comas

    Returns:
        List[int]: Lista de números enteros validados

    Raises:
        ValueError: Si la entrada contiene valores no numéricos
    """
    if not entrada.strip():
        return []

    # Dividir por comas y limpiar espacios
    elementos = [elemento.strip() for elemento in entrada.split(',')]
    lista_numeros = []

    for elemento in elementos:
        if elemento:  # Ignorar elementos vacíos
            try:
                numero = int(elemento)
                lista_numeros.append(numero)
            except ValueError:
                raise ValueError(f"❌ Error: '{elemento}' no es un número entero válido")

    return lista_numeros


def solicitar_lista_usuario() -> List[int]:
    """
    Solicita al usuario que ingrese una lista de números y valida la entrada.

    Returns:
        List[int]: Lista de números enteros validados
    """
    print("\n" + "=" * 50)
    print("INGRESO DE LISTA PARA ORDENAR")
    print("=" * 50)

    while True:
        try:
            print("\n📝 Instrucciones:")
            print("   - Ingresa números enteros separados por comas")
            print("   - Ejemplo: 5, 2, 8, 1, 9, 3")
            print("   - Deja vacío y presiona Enter para una lista vacía")

            entrada = input("\n👉 Ingresa tu lista de números: ")

            lista_validada = validar_lista_numeros(entrada)
            return lista_validada

        except ValueError as e:
            print(f"\n{e}")
            print("Por favor, intenta nuevamente.")
        except KeyboardInterrupt:
            print("\n\n❌ Entrada cancelada por el usuario.")
            return []
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("Por favor, intenta nuevamente.")


def mostrar_resultados(lista_original: List[int], lista_ordenada: List[int]) -> None:
    """
    Muestra los resultados del proceso de ordenamiento de forma clara.

    Args:
        lista_original (List[int]): Lista original ingresada por el usuario
        lista_ordenada (List[int]): Lista ordenada resultante
    """
    print("\n" + "=" * 50)
    print("RESULTADOS DEL ORDENAMIENTO")
    print("=" * 50)

    print(f"📊 Lista original:  {lista_original}")
    print(f"✅ Lista ordenada:  {lista_ordenada}")
    print(f"🔢 Cantidad de elementos: {len(lista_original)}")


def principal() -> None:
    """
    Función principal que coordina todo el proceso:
    1. Solicita la lista al usuario
    2. Valida la entrada
    3. Aplica merge sort
    4. Muestra resultados
    """
    print("🎯 ALGORITMO MERGE SORT")
    print("💻 ALUMNA: 2598198 - DAPHNE VALERIA MORALES MORENO")

    try:
        # Solicitar lista al usuario
        lista_usuario = solicitar_lista_usuario()

        # Aplicar merge sort
        lista_ordenada = merge_sort(lista_usuario)

        # Mostrar resultados
        mostrar_resultados(lista_usuario, lista_ordenada)

    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {e}")
    finally:
        print("\n" + "=" * 50)
        print("¡Proceso completado! 🎉")
        print("=" * 50)


# ============================================
# FUNCIÓN PRINCIPAL PARA DEMOSTRACIÓN
# ============================================
if __name__ == "__main__":
    principal()
