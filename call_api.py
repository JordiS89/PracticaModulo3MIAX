import requests, json
import pandas as pd

class ApiHandler:
    def __init__(self, day):
        self.day = day 
        self.url_base = 'https://api.esios.ree.es/archives/70/download_json?locale=es&date=2021-01-01'
        
    
    def get_precio(self):
        url = f'{self.url_base}'
        response = requests.get(url)
        df = pd.DataFrame(response.json()['PVPC'])
        return df

#
a1 = ApiHandler(day = '2021-10-01')
precio = a1.get_precio()
print(precio['PVPC'])