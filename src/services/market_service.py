from datetime import datetime
from repositories.market_repository import market_repository as default_market_repository


class MarketService:
    def __init__(self, market_repository=default_market_repository):
        self._market_repository = market_repository

    def find_stocks(self, portfolio_id):
        stocks = self._market_repository.find_stocks(portfolio_id)
        return stocks
    
    def find_remaining_stocks(self, portfolio_id):
        remaining = self._market_repository.find_remaining_stocks(portfolio_id)
        return remaining

    def create_portfolio(self, owner, date, name):
        self._market_repository.create_portfolio(owner, date, name)

    def find_portfolio_name(self, owner):
        portfolio_name = self._market_repository.find_portfolio_name(owner)
        return portfolio_name
    
    def create_stock(self, company, amount, buy_date, sell_date, buy_price, sell_price, portfolio_id):
        self._market_repository.create_stock(company, amount, buy_date, sell_date, buy_price, sell_price, portfolio_id)
    
    def create_stat(self, portfolio_name, user_name, investment, result):
        self._market_repository.create_stat(portfolio_name, user_name, investment, result)
    
    def get_stats(self):
        stats = self._market_repository.get_stats()
        return stats
    
    def update_amount(self, company, amount, buy_date, sell_date, buy_price, sell_price, portfolio_id):
        self._market_repository.update_amount(company, amount, buy_date, sell_date, buy_price, sell_price, portfolio_id)

    def find_portfolio_id(self, owner):
        id = self._market_repository.find_portfolio_id_by_owner(owner)
        return id
    
    def check_portfolio(self, owner):
        check = self._market_repository.check_portfolio(owner)
        return check
    
    def get_sellable_stocks(self, company, portfolio_id):
        sellable_stocks = self._market_repository.get_sellable_stocks(company, portfolio_id)
        return sellable_stocks
    
    def sell(self, amount, sell_date, sell_price, id):
        self._market_repository.sell(amount, sell_date, sell_price, id)
    
    def buy(self, amount):
        self._market_repository.buy(amount)
    
    def delete_sold_stocks(self):
        self._market_repository.delete_sold_stocks()
    
    def add_transaction(self, date, company, buy_price, sell_price, banking, dividend, balance, portfolio_id):
        self._market_repository.add_transaction(date, company, buy_price, sell_price, banking, dividend, balance, portfolio_id)
    
    def get_latest_transaction(self, portfolio_id):
        date = self._market_repository.get_latest_transaction(portfolio_id)
        return date

    def find_transactions(self, portfolio_id):
        transactions = []
        transactionlist = self._market_repository.find_transactions(portfolio_id)
        for transaction in transactionlist:
            if transaction[2]!="company":
                transactions.append(transaction)
                           
        return transactions
    
    def delete_stocks_by_portfolio(self, portfolio_id):
        self._market_repository.delete_stocks_by_portfolio(portfolio_id)

    def delete_transactions_by_portfolio(self, portfolio_id):
        self._market_repository.delete_transactions_by_portfolio(portfolio_id)

    def delete_portfolio_by_owner(self, owner):
        self._market_repository.delete_portfolio_by_owner(owner)
    

market_service = MarketService()
