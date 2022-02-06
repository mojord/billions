from werkzeug.security import check_password_hash, generate_password_hash
from repositories.user_repository import user_repository as default_user_repository

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def create_user(self, username, password):
        hash_value = generate_password_hash(password)
        self._user_repository.create(username, hash_value)

user_service = UserService()