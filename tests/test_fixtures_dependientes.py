import pytest

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Carrito:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        
    def agregar_item(self, item):
        self.items.append(item)
        
# Fixture para crear un objeto cliente
@pytest.fixture
def cliente():
    return Cliente(nombre="Alice")

# Fixture para crear un objeto Carrito, que depende de la fixture cliente
@pytest.fixture
def carrito():
    return Carrito(cliente)

# Fixture de prueba que utiliza el fixture carrito
def test_carrito_vacio(carrito):
    assert len(carrito.items) == 0