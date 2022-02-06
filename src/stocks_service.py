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


stocks_service = StocksService()
