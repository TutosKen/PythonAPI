from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from uuid import uuid4


class Encoding():

    # PasswordHasher instance
    password_hasher = None

    def __init__(self) -> None:
        self.password_hasher = PasswordHasher()

    # Encrypt password with Argon2 algorithm
    def argon2_encrypt(self, password: str) -> str:
        hash = self.password_hasher.hash(password)
        return hash

    # Verify encrypted password
    def argon2_verify(self, password: str, hash: str) -> bool:
        try:
            self.password_hasher.verify(hash, password)
            return True
        except VerifyMismatchError:
            return False

    # Generate unique auth token
    def generate_auth_token(self):
        token = uuid4()
        return str(token)
