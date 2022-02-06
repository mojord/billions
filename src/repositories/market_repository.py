from sqlalchemy import text
from db import db

class MarketRepository:
    def __init__(self):
        pass
    
    def create_portfolio(self, username, date, name):
        sql = "INSERT INTO portfolios (username, date, name) VALUES (:username, :date, :name)"
        db.session.execute(sql, {"username":username, "date":date, "name":name})
        db.session.commit()

    def create_stock(self, company, amount, buy_date, sell_date, buy_price, sell_price):
        sql = """INSERT INTO stocks (company, amount, buy_date, sell_date, buy_price, sell_price)
            VALUES (:company, :amount, :buy_date, :sell_date, :buy_price, :sell_price)"""
        db.session.execute(sql, {"company":company, "amount":amount, "buy_date":buy_date, "sell_date":sell_date, "buy_price":buy_price, "sell_price":sell_price})

    def find_portfolio_by_username(self, username):
        sql = "SELECT username FROM portfolio WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        return result.fetchone()

market_repository = MarketRepository()