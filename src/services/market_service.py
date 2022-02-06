from repositories.market_repository import market_repository as default_market_repository


class MarketService:
    def __init__(self, market_repository=default_market_repository):
        self._market_repository = market_repository

    def create_portfolio(self, name, date, owner):
        self._market_repository.create_portfolio(name, date, owner)
    
    def create_stock(self, company, amount, buy_date, sell_date, buy_price, sell_price):
        self._market_repository.create_stock(company, amount, buy_date, sell_date, buy_price, sell_price)


market_service = MarketService()
