from abc import ABC, abstractmethod

from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.non_negative_numbers import NonNegativeNumber
from custom_exceptions.overdraw_account import OverdrawAccount
from entities.BankCustomer import BankCustomer
from entities.BankAccount import BankAccount


class AccountServiceInterface(ABC):

    @abstractmethod
    def service_create_account(self, bank_account: BankAccount, starting_balance: int) -> BankAccount:
        pass

    @abstractmethod
    def service_get_specific_account_by_id(self, bank_account: BankAccount, account_number: int) -> BankAccount:
        pass

    @abstractmethod
    def service_get_all_accounts_for_users(self, customer_id: int) -> BankAccount:
        pass

    @abstractmethod
    def service_withdraw_from_account_by_id(self, bank_account: BankAccount, account_number: int,
                                            withdraw_amount: int) -> BankAccount:
        pass

    # Update

    @abstractmethod
    def service_deposit_into_account_by_id(self, bank_account: BankAccount, account_number: int,
                                           deposit_amount: int) -> BankAccount:
        pass

    @abstractmethod
    def service_transfer_money_between_accounts_by_their_ids(self, id_number: int, account_number_one: int,
                                                             account_number_two: int,
                                                             transfer_amount: int) -> BankAccount:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, id_number: int, account_number: int) -> bool:  #
        pass
