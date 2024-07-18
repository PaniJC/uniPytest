from logica.calculadora import Calculadora

import pytest

calculadora = Calculadora()

def test_suma_positiva():
    assert calculadora.mi_function_a_probar(2,8)==10
    
@pytest.mark.PruebaNegativa
def test_suma_negativa():
    assert calculadora.mi_function_a_probar(-8,3) == -5

def test_suma_de_ceros():
    assert calculadora.mi_function_a_probar(0,0) == 0