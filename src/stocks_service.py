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
    
    def dividends_2020(self):
        dividends_2020 = {"Elisa": ("6.4.2020", 1.85), "Fortum": ("27.4.2020", 1.1), "Kone": ("27.2.2020", 1.7), "Metso": ("13.3.2020", 0.1),
                            "Neste": ("20.5.2020", 1.02), "OrionB": ("8.5.2020", 1.5), "Sampo": ("4.6.2020", 1.5), "UPM": ("2.4.2020", 1.3),
                            "Wärtsilä": ("10.9.2020", 0.48)}
        self.convert_to_date(dividends_2020)
        return dividends_2020

    def dividends_2021(self):
        dividends_2021 = {"Elisa": ("12.4.2021", 1.95), "Fortum": ("30.4.2021", 1.12), "Kone": ("4.3.2021", 2.25), "Metso": ("3.11.2021", 0.2),
                            "Neste": ("1.4.2021", 0.8), "Nordea": ("5.10.2021", 0.79), "OrionB": ("29.3.2021", 1.5), "Sampo": ("21.5.2021", 1.7),
                            "UPM": ("1.4.2021", 1.3), "Wärtsilä": ("13.9.2021", 0.2)}
        self.convert_to_date(dividends_2021)
        return dividends_2021

    def convert_to_date(self, list):
        strdate = ""
        for element in list:
            strdate = list[element][0]
            div= list[element][1]
            tdate = datetime.strptime(strdate, "%d.%m.%Y")
            date = datetime.date(tdate)
            list[element] = (date, div)




stocks_service = StocksService()
