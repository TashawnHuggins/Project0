"""This is the interface of the bank account's class"""
from abc import ABC, abstractmethod

from entities.BankAccount import BankAccount

"""This is for the CRUD operators"""


class BankAccountDAOInterface(ABC):

    # Create
    @abstractmethod
    # def create_account(self, bank_account: BankAccount, bank_customer: BankCustomer,
    # id_number: BankCustomer) -> BankAccount:
    def create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    # Read (or look for)
    @abstractmethod
    def get_specific_account_by_id(self, bank_account: BankAccount, account_number: int) -> BankAccount:
        pass

    # Read
    @abstractmethod
    def get_all_accounts_for_users(self, customer_id: int) -> BankAccount:
        pass

    # Update
    @abstractmethod
    def withdraw_from_account_by_id(self, bank_account: BankAccount, account_number: int,
                                    withdraw_amount) -> BankAccount:
        pass

    # Update
    @abstractmethod
    def deposit_into_account_by_id(self, bank_account: BankAccount, account_number: int, deposit_amount) -> BankAccount:
        pass

    # Update
    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, account_one: BankAccount, account_two: BankAccount,
                                                     account_number_one: int, account_number_two: int, transfer_amount:
                                                     int) -> BankAccount:
        pass

    # Delete
    @abstractmethod
    def delete_account_by_id(self, id_number: int) -> bool:
        pass
