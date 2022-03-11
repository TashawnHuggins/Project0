from abc import ABC, abstractmethod

from dal_layer.customer_dao_implementation import BankCustomerDAOImp
from dal_layer.customer_dao_interface import BankCustomerDAOInterface
from entities.BankCustomer import BankCustomer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: BankCustomerDAOInterface):  # customer_dao is an object of BankCustomerInterface
        self.customer_dao: BankCustomerDAOImp = customer_dao  # this is copying the customer dao implementation

    @abstractmethod
    def service_create_bank_customer(self, bank_customer: BankCustomer) -> BankCustomer:
        pass

    @abstractmethod
    def service_get_bank_customer_by_id(self, id_number: int) -> BankCustomer:
        pass

    @abstractmethod
    def service_update_bank_customer_by_id(self, bank_customer: BankCustomer) -> BankCustomer:
        pass

    @abstractmethod
    def service_delete_bank_customer_by_id(self, id_number: int) -> bool:
        pass
