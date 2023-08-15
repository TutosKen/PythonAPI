from abc import ABC, abstractmethod


class BankingBase(ABC):

    @abstractmethod
    def get_balance(self, account: str) -> dict:
        """
        Get customer account balance from provider

        Args:
            account (str): Customer bank account.

        Returns:
            dict: A python dictionary containing provider information.
        """
        pass
