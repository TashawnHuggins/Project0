from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao_implementation import BankCustomerDAOImp
from entities.BankCustomer import BankCustomer
from service_layer.customer_service_imp import CustomerServiceImp

customer_dao = BankCustomerDAOImp()
customer_service = CustomerServiceImp()

"""
create customer tests
"""


# To create a customer, we need a BankCustomer object
def test_create_customer_success():
    test_customer = BankCustomer(0, "John", "Doe")  # this is the blueprint for a test bank customer
    result = customer_dao.create_bank_customer(test_customer)  # this creates a test bank customer
    assert result.id_number != 0


def test_catch_duplicate_id(id_number):  # go through customer list and look at their ids to match them.
    test_customer2 = BankCustomer(1, "Jane", "Doe")
    result = customer_dao.get_bank_customer_by_id_number(test_customer2)
    assert result.id_number != 1


"""
get customer tests
"""


def test_get_customer_info_by_id_success():
    result = customer_dao.get_bank_customer_by_id_number(1)
    assert result.id_number == 1


def test_customer_using_non_existing_id():
    try:
        customer_dao.get_bank_customer_by_id_number(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No player matches the id given: please try again!"


"""
update customer tests
"""


def test_update_customer_by_id_success():
    test_customer_two = BankCustomer(1, 1, "Batman", "Fort Wayne", 50)
    result = customer_dao.update_bank_customer_by_id(test_customer_two)
    assert result.first_name == "Batman"


def test_update_customer_using_non_existing_id():
    try:
        test_customer_two = BankCustomer(0, 1, "Batman", "Fort Wayne", 50)
        customer_dao.update_bank_customer_by_id(test_customer_two)
        assert False
    except IdNotFound as e:
        assert str(e) == "No player matches the id given: please try again!"


"""
delete team tests
"""


def test_delete_customer_by_id_success():
    result = customer_dao.delete_bank_customer_by_id(1)
    assert result


def test_delete_customer_with_non_existing_id():
    try:
        customer_dao.delete_bank_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No player matches the id given: please try again!"
