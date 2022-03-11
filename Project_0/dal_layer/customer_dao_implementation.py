from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao_interface import BankCustomerDAOInterface
from entities.BankCustomer import BankCustomer


class BankCustomerDAOImp(BankCustomerDAOInterface):
    # bank_customer_dictionary = {"IdNumber": 1, "firstName": "John", "lastName": "Doe"}
    test_account = BankCustomer(1, "John", "Doe")
    bank_customer_list = [test_account]
    id_number_generator = 2

    # Create
    # customers can only have one ID number, and there cannot be duplicates
    # need to create an object of the class BankCustomer (object: of Class is in parameter) correct?
    # bank_customer is an object of BankCustomer class
    def create_bank_customer(self, bank_customer: BankCustomer) -> BankCustomer:
        bank_customer.id_number = self.id_number_generator
        self.id_number_generator += 1
        self.bank_customer_list.append(bank_customer)
        return bank_customer

    # Read (or look for)

    def get_bank_customer_by_id_number(self, id_number: int) -> BankCustomer:
        pass

    # Update

    def update_bank_customer_by_id(self, id_number: int) -> BankCustomer:
        pass

    # Delete

    def delete_bank_customer_by_id(self, id_number: int) -> bool:  # how to know when to place objects as argument
        for bank_customer in self.bank_customer_list:
            if bank_customer.id_number == id_number:
                self.bank_customer_list.remove(bank_customer)
                return True
        raise IdNotFound("No customer matches the id given: please try again!")
