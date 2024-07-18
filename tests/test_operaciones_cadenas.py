import pytest
from logica.operaciones_cadenas import OperacionesCadenas

operaciones_cadenas = OperacionesCadenas()

# Prueba 1: Comprobar si la función combina las cadenas correctamente.
def test_combinar_cadenas():
    resultado = operaciones_cadenas.combinar_cadenas("Hola", "Mundo")
    assert resultado == "Hola Mundo", "La combinación de cadenas es incorrecta"

# Prueba 2: Comprobar si la función maneja cadenas vacías.    
def test_combinar_cadenas_vacias():
    resultado = operaciones_cadenas.combinar_cadenas("", "")
    assert resultado == " ", "La combinación de cadenas vacías es incorrecta"

# Prueba 3: Comprobar si la función maneja una cadena vacía y una no vacía.    
def test_combinar_cadenas_con_cadena_vacia():
    resultado = operaciones_cadenas.combinar_cadenas("Hola", "")
    assert resultado == "Hola ", "La combinación de cadenas con una cadena vacía es incorrecta"

# Prueba 4: Comprobar si la función maneja espacios en blanco alrededor de las cadenas.      
def test_combinar_cadenas_con_espacios_en_blanco():
    resultado = operaciones_cadenas.combinar_cadenas(" Hola ", " mundo ")
    assert resultado == " Hola   mundo ", "La combinación de cadenas con espacios en blanco es incorrecta"