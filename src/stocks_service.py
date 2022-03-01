import os
from csv_reader import *
from datetime import datetime

dirname = os.path.dirname(__file__)

class StocksService:
    def __init__(self):
        self._file = {}


    def read_file(self, file):
        path = os.path.join(dirname, file)
        reader = CSVReader(path)
        self._file = reader.read()

        market  = self._file
        return market
        
    def give_values(self,label,date,list):
        for key,value in list.items():
            if key == date:            
#                print(key, value)
#        print(f"tässä päiväys {date}")
                return label, value[0], value[1], date
    
    def last_day(self):
        last_prices = {"Elisa": 54.177, "Finnair": 0.59, "Fortum": 27.05, "Kone": 63.084, "Metso": 9.368, "Neste": 43.328, "Nokia": 5.582, "Nordea": 10.828, "Orion B": 36.429, "Sampo": 44.147, "UPM": 33.502, "Wärtsilä": 12.366}
        return last_prices


stocks_service = StocksService()
