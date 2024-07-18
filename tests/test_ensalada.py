import pytest

class Fruta:
    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.en_cubos = False
        
    # Function cortar en cubos
    def cortar_en_cubos(self):
        self.en_cubos = True
        
class EnsaladaDeFrutas:
    def __init__(self, *bowl_de_frutas):
        self.frutas = bowl_de_frutas
        self._cortar_frutas()
        
    def _cortar_frutas(self):
        for fruta in self.frutas:
            fruta.cortar_en_cubos()
            
# Setup
@pytest.fixture
def bowl_de_frutas():
    return [Fruta("pera"), Fruta("Manzana")]

def test_ensalada_de_frutas(bowl_de_frutas):
    # Acción
    ensalada_de_frutas = EnsaladaDeFrutas(*bowl_de_frutas)
    
    #Verificación "Las frutas en cubo para cada fruta dentro de la ensalada de frutas"
    assert all(fruta.en_cubos for fruta in ensalada_de_frutas.frutas)
           