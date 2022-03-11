"""This is the interface of the banking customer's class"""
from abc import ABC, abstractmethod
from entities.BankCustomer import BankCustomer

"""This is for the CRUD """


class BankCustomerDAOInterface(ABC):

    # Create
    @abstractmethod
    def create_bank_customer(self, bank_customer: BankCustomer) -> BankCustomer:
        pass

    # Read (or look for)
    @abstractmethod
    def get_bank_customer_by_id_number(self, id_number: int) -> BankCustomer:
        pass

    # Update
    @abstractmethod
    def update_bank_customer_by_id(self, id_number: int) -> BankCustomer:
        pass

    # Delete
    @abstractmethod
    def delete_bank_customer_by_id(self, id_number: int) -> bool:
        pass
