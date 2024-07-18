import requests

class ApiHandler:
    def get_data_from_api(self):
        response = requests.get('https://rickandmortyapi.com/api')
        if response.status_code == 200:
            return response.json()["data"]
        else:
            return []