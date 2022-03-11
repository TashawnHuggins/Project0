"""This is the interface of the banking customer's class"""
from entities.BankAccount import BankAccount

"""In order for a customer to create an account at a bank, they will need their first name, and last name; 
they will get an id number fom the bank

"""


class BankCustomer:
    def __init__(self, customer_id: int, first_name: str, last_name: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def convert_to_dictionary(self):
        return {
            "CustomerId": self.customer_id,
            "firstName": self.first_name,
            "lastName": self.last_name
        }
