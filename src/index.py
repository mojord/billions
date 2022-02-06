from app import app
#from stocks_service import StocksService
from stocks_service import stocks_service



#def prepare_stockmarket():
#    stocks_service = StocksService()
#    nordea = stocks_service.read_file("NDA.csv")

#    for key,value in nordea.items():
#        print(key, value)



if __name__ == "__main__":
#    prepare_stockmarket()
    app.run()