from sqlalchemy import text
from db import db

class MarketRepository:
    def __init__(self):
        pass
    
    def create_portfolio(self, owner, date, name):
        sql = "INSERT INTO portfolios (owner, date, name) VALUES (:owner, :date, :name)"
        db.session.execute(sql, {"owner":owner, "date":date, "name":name})
        db.session.commit()

    def create_stock(self, company, amount, buy_date, sell_date, buy_price, sell_price, portfolio_id):
        sql = """INSERT INTO stocks (company, amount, buy_date, sell_date, buy_price, sell_price, portfolio_id)
            VALUES (:company, :amount, :buy_date, :sell_date, :buy_price, :sell_price, :portfolio_id)"""
        db.session.execute(sql, {"company":company, "amount":amount, "buy_date":buy_date, "sell_date":sell_date, "buy_price":buy_price, "sell_price":sell_price, "portfolio_id":portfolio_id})
        db.session.commit()
    
    def create_stat(self, portfolio_name, user_name, investment, result):
        sql = """INSERT INTO stats (portfolio_name, user_name, investment, result)
            VALUES (:portfolio_name, :user_name, :investment, :result)"""
        db.session.execute(sql, {"portfolio_name":portfolio_name, "user_name":user_name, "investment":investment, "result":result})
        db.session.commit()
    
    def get_stats(self):
        sql = "SELECT portfolio_name, user_name, investment, result FROM stats ORDER BY result DESC"
        result = db.session.execute(sql)
        return result.fetchall()
    
    def find_stocks(self, portfolio_id):
        sql = "SELECT * FROM stocks WHERE portfolio_id=:portfolio_id AND amount IS NOT NULL ORDER BY buy_date"
        result = db.session.execute(sql, {"portfolio_id":portfolio_id})
        return result.fetchall()
    
    def find_remaining_stocks(self, portfolio_id):
        sql = "SELECT company, amount, buy_price, buy_date FROM stocks WHERE portfolio_id=:portfolio_id"
        result = db.session.execute(sql, {"portfolio_id":portfolio_id})
        return result.fetchall()
    
    def check_portfolio(self, owner):
        sql = "SELECT * FROM portfolios WHERE owner=:owner"
        result = db.session.execute(sql, {"owner":owner}).fetchall()
        if len(result)==0:
            return False
        else:
            return True

    def find_portfolio_name(self, owner):
        sql = "SELECT name FROM portfolios WHERE owner=:owner"
        result = db.session.execute(sql, {"owner":owner})
        return result.fetchone()[0]

    def find_portfolio_id_by_owner(self, owner):
        sql = "SELECT id FROM portfolios WHERE owner=:owner"
        result = db.session.execute(sql, {"owner":owner})
        return result.fetchone()[0]

    def get_sellable_stocks(self, company, portfolio_id):
        sql = "SELECT * FROM stocks WHERE company=:company AND portfolio_id=:portfolio_id AND amount >= 0 ORDER BY buy_date"
        result = db.session.execute(sql, {"company":company, "portfolio_id":portfolio_id})
        return result.fetchall()
    
    def sell(self, amount, sell_date, sell_price, id):
        sql = "UPDATE stocks SET amount=:amount*-1, sell_date=:sell_date, sell_price=:sell_price WHERE id=:id"
        db.session.execute(sql, {"amount":amount, "sell_date":sell_date, "sell_price":sell_price, "id":id})
        db.session.commit()

    def buy(self, amount):
        sql = "UPDATE stocks SET amount=:amount WHERE amount=0"
        db.session.execute(sql, {"amount":amount})
        db.session.commit()
    
    def delete_sold_stocks(self):
        sql = "DELETE FROM stocks WHERE amount <= 0"
        db.session.execute(sql)
        db.session.commit()
    
    def add_transaction(self, date, company, buy_price, sell_price, banking, dividend, balance, portfolio_id):
        sql = """INSERT INTO transactions (date, company, buy_price, sell_price, banking, dividend, balance, portfolio_id)
            VALUES (:date, :company, :buy_price, :sell_price, :banking, :dividend, :balance, :portfolio_id)"""
        db.session.execute(sql, {"date":date, "company":company, "buy_price":buy_price, "sell_price":sell_price, "banking":banking, "dividend":dividend, "balance":balance, "portfolio_id":portfolio_id})
        db.session.commit()
    
    def get_latest_transaction(self, portfolio_id):
        sql = "SELECT MAX(date) FROM transactions WHERE portfolio_id=:portfolio_id"
        result = db.session.execute(sql, {"portfolio_id":portfolio_id})
        db.session.commit()
        return result.fetchone()[0]
    
    def find_transactions(self, portfolio_id):
        sql = "SELECT * FROM transactions WHERE portfolio_id=:portfolio_id"
        result = db.session.execute(sql, {"portfolio_id":portfolio_id})
        return result.fetchall()
    
    def delete_stocks_by_portfolio(self, portfolio_id):
        sql = "DELETE FROM stocks WHERE portfolio_id=:portfolio_id"
        db.session.execute(sql, {"portfolio_id":portfolio_id})
        db.session.commit()
    
    def delete_transactions_by_portfolio(self, portfolio_id):
        sql = "DELETE FROM transactions WHERE portfolio_id=:portfolio_id"
        db.session.execute(sql, {"portfolio_id":portfolio_id})
        db.session.commit()
    
    def delete_portfolio_by_owner(self, owner):
        sql = "DELETE FROM portfolios WHERE owner=:owner"
        db.session.execute(sql, {"owner":owner})
        db.session.commit()

market_repository = MarketRepository()