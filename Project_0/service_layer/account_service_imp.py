from abc import ABC

from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.bad_customer_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.non_negative_numbers import NonNegativeNumber
from custom_exceptions.overdraw_account import OverdrawAccount
from dal_layer.bank_dao_implementation import BankAccountDAOImp
from service_layer.account_service_interface import AccountServiceInterface
from entities.BankAccount import BankAccount
from entities.BankCustomer import BankCustomer

"""The job of the service layer is to validate the info inside the BankAccount object"""


# account_
class AccountServiceImp(AccountServiceInterface, ABC):
    def __init__(self, account_dao: BankAccountDAOImp):
        self.account_dao = account_dao

    # Create

    def service_create_account(self, bank_account: BankAccount, starting_balance: int) -> BankAccount:
        if bank_account.starting_balance < 0:
            raise NonNegativeNumber()  # "Please enter a positive number"
        if type(starting_balance) != int:  # starting_balance has to be an integer
            raise BadAccountInfo()  # "Please enter numbers"
        else:
            return self.account_dao.create_account()

    # Read (or look for)

    def service_get_specific_account_by_id(self, bank_account: BankAccount, account_number: int) -> BankAccount:
        if type(account_number) != int:  # account_number has to be an integer
            raise BadAccountInfo()  # "Please enter numbers"
        elif account_number < 0:
            raise NonNegativeNumber()  # "Please enter a valid account number"
        elif account_number != bank_account.account_number:
            raise BadAccountInfo()  # "Invalid ID"
        else:
            return self.account_dao.get_specific_account_by_id(bank_account.customer_id)

    # Read

    def service_get_all_accounts_for_users(self, bank_account: BankAccount, customer_id: int) -> BankAccount:
        if type(customer_id) != int:  # customer id_number has to be an integer
            raise BadAccountInfo()  # "Please enter numbers"
        elif customer_id < 0:
            raise NonNegativeNumber()  # "Please enter a valid ID number"
        elif customer_id != bank_account.customer_id:
            raise BadAccountInfo()  # "Invalid ID"
        else:
            return self.account_dao.get_all_accounts_for_users(bank_account.customer_id)

    # Update

    def service_withdraw_from_account_by_id(self, bank_account: BankAccount, account_number: int,
                                            withdraw_amount: int) -> BankAccount:
        if type(account_number) != int:  # account_number has to be an integer
            raise BadAccountInfo()  # "Please enter numbers"
        elif account_number < 0:
            raise NonNegativeNumber()  # "Please enter a valid ID number"
        elif account_number != bank_account.account_number:
            raise BadAccountInfo()  # "Invalid ID"
        if withdraw_amount < 0:
            raise NonNegativeNumber()  # "Please enter a positive number"
        elif type(withdraw_amount) != int:
            raise BadAccountInfo  # "Please enter numbers"
        elif withdraw_amount > 0 and withdraw_amount > bank_account.account_balance:
            raise OverdrawAccount()  # "Withdraw amount exceeds account balance"
        else:
            return self.account_dao.withdraw_from_account_by_id(bank_account, account_number,
                                                                withdraw_amount)

    # Update

    def service_deposit_into_account_by_id(self, bank_account: BankAccount, account_number: int,
                                           deposit_amount: int) -> int:
        if type(account_number) != int:  # account_number has to be an integer
            raise BadAccountInfo()  # "Please enter numbers"
        elif account_number < 0:
            raise NonNegativeNumber()  # "Please enter a valid ID number"
        elif account_number != bank_account.account_number:
            raise BadAccountInfo()  # "Invalid ID"
        if type(deposit_amount) != int:  # customer id_number has to be an integer
            raise BadAccountInfo()  # "Please enter numbers"
        elif deposit_amount < 0:
            raise NonNegativeNumber()  # "Please enter a positive number"
        elif self.account_dao.customer_id != bank_account.customer_id:
            raise BadAccountInfo()  # "Invalid ID"
        else:
            return self.account_dao.deposit_into_account_by_id(account_number, deposit_amount)

    # Update

    def service_transfer_money_between_accounts_by_their_ids(self, bank_account: BankAccount, account_one: BankAccount,
                                                             account_two: BankAccount, account_number_one: int,
                                                             account_number_two: int,
                                                             transfer_amount: int) -> BankAccount:
        if type(account_one.account_number) != int or type(account_two.account_number) != int:
            raise BadAccountInfo()  # "Please enter numbers"
        elif account_one.account_number < 0 or account_two.account_number < 0:
            raise NonNegativeNumber()  # "Please provide a valid account number"
        elif transfer_amount < 0:
            raise NonNegativeNumber()  # "Please enter a positive number"
        elif type(transfer_amount) != int:
            raise BadAccountInfo()  # "Please enter a numbers"
        elif transfer_amount > account_number_one:
            raise OverdrawAccount()  # "Transfer amount exceeds account balance"
        else:
            return self.account_dao.transfer_money_between_accounts_by_their_ids(id_number, account_number_one,
                                                                                 account_number_two, transfer_amount)

    # Delete

    def service_delete_account_by_id(self, id_number: int, account_number: int) -> bool:  #
        if type(id_number) == int:
            return self.account_dao.delete_account_by_id(id_number)  # should return true
        else:
            raise BadCustomerInfo()  # "Please provide a valid ID number"
