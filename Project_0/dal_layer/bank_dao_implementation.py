from custom_exceptions.id_not_found import IdNotFound
from dal_layer.bank_dao_interface import BankAccountDAOInterface
from entities.BankAccount import BankAccount


class BankAccountDAOImp(BankAccountDAOInterface):
    bank_account_list = [BankAccount(0, 0, 300, 100)]  # this is an object of BankAccount class
    account_number_generator = 2

    def __init__(self):
        account_needed_for_id_catch = BankAccount(1, 1, 100, 100)
        self.bank_account_list = []  # why is this needed?
        self.account_number_generator = 2
        self.bank_account_list.append(account_needed_for_id_catch)

    # Create

    def create_account(self, bank_account: BankAccount) -> BankAccount:
        bank_account.account_number = self.account_number_generator
        bank_account.account_balance = bank_account.starting_balance
        return bank_account

    # Read (or look for)

    def get_specific_account_by_id(self, bank_account: BankAccount, account_number: int) -> BankAccount:
        # display balance

        if bank_account.account_number == account_number:
            return bank_account.account_balance

    # Read

    def get_all_accounts_for_users(self, customer_id) -> BankAccount:
        try:
            for account in self.bank_account_list:
                if account.customer_id == customer_id:
                    return account
        except IdNotFound as e:
            assert str(e) == "ID not found"

    # Update

    def withdraw_from_account_by_id(self, bank_account: BankAccount, account_number: int,
                                    withdraw_amount) -> BankAccount:
        #  withdraw and display account_balance

        if bank_account.account_number == account_number:
            withdraw = bank_account.account_balance - withdraw_amount
            bank_account.account_balance = withdraw
            return bank_account.account_balance

    # Update

    def deposit_into_account_by_id(self, bank_account: BankAccount, account_number: int, deposit_amount) -> int:
        if bank_account.account_number == account_number:
            deposit = bank_account.account_number
            bank_account.account_balance = deposit
            return bank_account.account_balance

    # Update

    def transfer_money_between_accounts_by_their_ids(self, account_one: BankAccount, account_two: BankAccount,
                                                     account_number_one: int, account_number_two: int, transfer_amount:
                                                     int) -> int:

        if account_one.account_number == account_number_one:
            withdraw = account_one.account_balance - transfer_amount
            account_one.account_balance = withdraw
            return account_one.account_balance
        if account_two.account_balance == account_two:
            deposit = account_two.account_balance + transfer_amount
            account_two.account_balance = deposit
            # return bank_account.account_balance
            return account_two.account_balance
        else:
            raise IdNotFound()

    # Delete

    def delete_account_by_id(self, customer_id: int) -> bool:
        for account in self.bank_account_list:
            if account.customer_id == customer_id:
                self.bank_account_list.remove(account)
                return True
        raise IdNotFound()
