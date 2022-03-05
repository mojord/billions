import os

#dirname = os.path.dirname(__file__)

from datetime import datetime, timedelta

class CSVReader():

    def __init__(self, file):
        self.file = file

    def read(self):
        """Reads csv files into hashmaps of stocks.
        Returns:
            Hashmaps of stocks.
        Raises:
            FileNotFoundError:
                When filename not found.
        """

        stocks = {}
        try:
            with open(self.file) as fname:
                for row in fname:
                    parts = row.split(";")
                    if parts[0] == "Date":
                        continue
                    date = datetime.strptime(parts[0], "%d.%m.%Y")
                    price_string = parts[7].replace(",", ".")
                    price = float(price_string)
                    
                    trades = int(parts[10])
                    
                    stocks[date]=(price, trades)

        except FileNotFoundError:
            raise FileNotFoundError("File not found.")

        return stocks