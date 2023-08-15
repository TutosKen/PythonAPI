from .banking_base import BankingBase
import random


class Example(BankingBase):

    def get_balance(self, account: str) -> dict:
        result = {}
        result["balance"] = self.random_balance()
        return result

    def random_balance(self):
        num_list = [200, 123, 456, 123, 5785, 1256, 8, 0, 76]
        return random.choice(num_list)
