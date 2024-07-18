# test para la función filtrar_numeros.py

import pytest
from logica.filtrador_de_numeros import Filtrador

filtrador = Filtrador()

def test_filtrar_numeros_pares():
    assert filtrador.filtrar_numeros([1,2,3,4,5], True) == [2,4]
    
def test_filtrar_numeros_impares():
    assert filtrador.filtrar_numeros([1,2,3,4,5], False) == [1,3,5]
