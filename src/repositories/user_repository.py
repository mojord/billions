from sqlalchemy import text
from db import db

class UserRepository:
    def __init__(self):
        pass
    
    def create(self, username, password_hash):
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":password_hash})
        db.session.commit()

    def check_username(self, username):
        sql = "SELECT username, password FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        return result.fetchone()
    

user_repository = UserRepository()