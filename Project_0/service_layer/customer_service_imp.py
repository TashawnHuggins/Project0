from custom_exceptions.bad_customer_info import BadCustomerInfo
from entities.BankCustomer import BankCustomer
from service_layer.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def service_create_bank_customer(self, bank_customer: BankCustomer) -> BankCustomer:
        if type(bank_customer.first_name) != str:
            raise BadCustomerInfo("First name must be string")
        elif type(bank_customer.last_name) != str:
            raise BadCustomerInfo("Last name must be string")
        if len(bank_customer.first_name) > 20:
            raise BadCustomerInfo("First name is too long")
        elif len(bank_customer.last_name) > 20:
            raise BadCustomerInfo("Last name is too long")
        else:
            return self.customer_dao.create_bank_customer

    def service_get_bank_customer_by_id(self, id_number: int) -> BankCustomer:
        if type(id_number) == int:
            return self.customer_dao.get_bank_customer_id_number(id_number)
        else:
            raise BadCustomerInfo("Please provide a valid Id")

    def service_update_bank_customer_by_id(self, bank_customer: BankCustomer) -> BankCustomer:
        if len(bank_customer.first_name) > 20:
            raise BadCustomerInfo("First name is too long")
        elif len(bank_customer.last_name) > 20:
            raise BadCustomerInfo("Last name is too long")
        for p in self.customer_dao.customer_list:
            if p.team_id == bank_customer.id_number and p.jersey_number == bank_customer.jersey_number:
                raise BadCustomerInfo("Jersey number already taken")
        return self.customer_dao.update_bank_customer_by_id(bank_customer)

    def service_delete_bank_customer_by_id(self, id_number: int) -> bool:
        if type(id_number) == int:
            return self.customer_dao.delete_bank_customer_by_id(id_number)  # should return true
        else:
            raise BadCustomerInfo("Please provide a valid ID number")


