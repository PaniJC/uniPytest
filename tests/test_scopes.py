import pytest

contador =0

# Fixture con el ámbito function
@pytest.fixture(scope="function")
def fixture_function():
    global contador
    contador += 1
    return contador

# Fixture con el ámbito class
@pytest.fixture(scope="class")
def fixture_class():
    global contador
    contador += 1
    return contador

# Fixture con el ámbito module
@pytest.fixture(scope="module")
def fixture_module():
    global contador
    contador += 1
    return contador

# Fixture con el ámbito session
@pytest.fixture(scope="session")
def fixture_session():
    global contador
    contador += 1
    return contador


def test_uno(fixture_function, fixture_class, fixture_module, fixture_session):
    print(f"Contador en test_uno: {contador}")
    
def test_dos(fixture_function, fixture_class, fixture_module, fixture_session):
    print(f"Contador en test_dos: {contador}")