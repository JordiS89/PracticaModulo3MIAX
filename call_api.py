import requests, json
import pandas as pd

class ApiHandler:
    def __init__(self, day):
        self.day = day 
        self.url_base = 'https://api.esios.ree.es/archives/70/download_json?locale=es&date='
        
    
    def get_ticker_master(self):
        url = f'{self.url_base}self.day'
        response = requests.get(url)
        df = pd.DataFrame(response.json()[’PVPC’])
        return df