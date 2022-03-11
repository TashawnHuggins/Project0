"""Tests the account service imp"""
from dal_layer.bank_dao_implementation import BankAccountDAOImp
from service_layer.account_service_imp import AccountServiceImp

"""These tests show that service implements are successful and unsuccessful"""

bank_account_dao = BankAccountDAOImp()
account_service = AccountServiceImp()


def test_catch_non_int_account_number():
    pass


def test_catch_non_positive_account_number():
    pass


def test_catch_duplicate_account_number():
    pass


def test_catch_non_int_customer_id():
    pass


def test_catch_non_positive_customer_id():
    pass


def test_catch_non_int_starting_balance():
    pass


def test_catch_positive_starting_balance():
    pass
