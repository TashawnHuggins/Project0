"""Bank Customers Unit Tests"""
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.bank_dao_implementation import BankAccountDAOImp
from entities.BankAccount import BankAccount
from service_layer.account_service_imp import AccountServiceImp

"""DAO = Data Access Object"""
"""These tests are to show that each DAO implementations are successful and unsuccessful"""

bank_account_dao = BankAccountDAOImp()


# account_service = AccountServiceImp()


# Create

def test_create_bank_customer_success():
    test_bank_account = BankAccount(0, 1, 100, 100)
    result = bank_account_dao.create_account(test_bank_account)
    print(result.customer_id)
    assert result.customer_id != 0


def test_catch_non_unique_id():
    test_bank_account = BankAccount(0, 1, 200, 100)
    result = bank_account_dao.create_account(test_bank_account)
    assert result.customer_id != 0


# Read (or look for)


def test_get_specific_account_by_id():
    test_bank_account = BankAccount(0, 1, 200, 100)
    result = bank_account_dao.get_specific_account_by_id(test_bank_account, 1)
    return result


# Read

def test_get_specific_account_by_non_existent_id():
    try:
        bank_account_dao.get_specific_account_by_id(11, 10)
        assert True
    except IdNotFound as e:
        assert str(e) == "ID not found"


# Read


def test_get_all_accounts_for_users() -> BankAccount:
    try:
        bank_account_dao.get_all_accounts_for_users(1)
        assert True
    except IdNotFound as e:
        assert str(e) == "ID not found"


def test_user_does_not_exist():
    try:
        bank_account_dao.get_all_accounts_for_users(1)
        assert True
    except IdNotFound as e:
        assert str(e) == "ID not found"


# Update

def test_withdraw_from_account_by_id() -> BankAccount:
    try:
        test_bank_account = BankAccount(0, 1, 200, 100)
        result = bank_account_dao.withdraw_from_account_by_id(test_bank_account, 1, 20)
        return result
    except IdNotFound as e:
        assert str(e) == "ID not found"


# Update

def test_deposit_into_account_by_id() -> int:
    try:
        test_bank_account = BankAccount(0, 1, 100, 100)
        result = bank_account_dao.deposit_into_account_by_id(test_bank_account, 1, 20)
        return result
    except IdNotFound as e:
        assert str(e) == "ID not found"


# Update

def test_transfer_money_between_accounts_by_their_ids() -> BankAccount:
    test_bank_account_one = BankAccount(0, 1, 100, 100)
    test_bank_account_two = BankAccount(1, 1, 100, 100)
    result = bank_account_dao.transfer_money_between_accounts_by_their_ids(test_bank_account_one, test_bank_account_two,
                                                                           0, 1, 20)
    return result


# Delete

def test_delete_account_by_id() -> bool:
    result = bank_account_dao.delete_account_by_id(1)
    assert result
