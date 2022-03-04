from werkzeug.security import check_password_hash, generate_password_hash
from repositories.user_repository import user_repository as default_user_repository

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def create_user(self, username, password):
        hash_value = generate_password_hash(password)
        self._user_repository.create(username, hash_value)
    
    def check_username(self, username):
        return self._user_repository.check_username(username)
    
    def login(self, username, password):
        result = self.check_username(username)
        user = result[0]
        if not user:
            return False
        if not check_password_hash(result[1], password):
            return False
        return True

user_service = UserService()