import pytest
import requests
import requests_mock
from logica.controlador_api import ApiHandler

api_handler = ApiHandler()

status_code_list = [400, 401, 402, 403, 404, 500, 501]

# @pytest.mark.skip(reason="La lógica invocada en este test NO está terminada.")
# def test_get_data_from_api():
#     # Simular una llamada a la API de Rick y Morty y vamos a introducir datos en respuesta.
#     with requests_mock.Mocker() as moker:
#         moker.get('https://rickandmortyapi.com/api', json={"data":[1,2,3]})
#         data = api_handler.get_data_from_api()
        
#         assert data == [1,2,3]

@pytest.mark.parametrize("status_code",status_code_list) # Esto indica que va a correr tantas veces como le indiquemos por parámetros
def test_no_get_data_from_api(status_code):
    #Simular que no recibimos ninguna data al llamar a la API; acá particularmente no voy a manipular el json en la respuesta sino el status code a través de una lista previamente definida con los status code y a un decorador de pytest @pytest.mark.parametrize, en donde inyecto el nombre de la variable que voy a usar y la lista.
    with requests_mock.Mocker() as mocker:
        mocker.get('https://rickandmortyapi.com/api', status_code = status_code)
        data = api_handler.get_data_from_api()
        
        assert data == []