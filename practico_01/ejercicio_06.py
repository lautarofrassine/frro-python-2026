"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    numeros = []
    strings = []
    for elem in lista:
        if isinstance(elem, (int, float)):
            numeros.append(elem)
        else:
            strings.append(elem)
    return strings + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(
    lista: List[Union[float, str]],
) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    strings = [elem for elem in lista if isinstance(elem, str)]
    numeros = [elem for elem in lista if isinstance(elem, (int, float))]
    return strings + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == [
    "a",
    "b",
    "j",
    3,
    1,
    10,
]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    return sorted(lista, key=lambda x: isinstance(x, (int, float)))


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    strings = list(filter(lambda x: isinstance(x, str), lista))
    numeros = list(filter(lambda x: isinstance(x, (int, float)), lista))
    return strings + numeros


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == [
        "a",
        "b",
        "j",
        3,
        1,
        10,
    ]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(
    lista: List[Union[float, str]],
) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    if len(lista) == 0:
        return []

    primero = lista[0]
    resto = lista[1:]

    resultado_resto = numeros_al_final_recursivo(resto)

    if isinstance(primero, str):
        return [primero] + resultado_resto
    else:
        strings = [x for x in resultado_resto if isinstance(x, str)]
        numeros = [x for x in resultado_resto if not isinstance(x, str)]
        return strings + [primero] + numeros


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == [
        "a",
        "b",
        "j",
        3,
        1,
        10,
    ]
# NO MODIFICAR - FIN
