"""
facade pattern
"""


class Invoice:
    def __init__(self, customer): pass


class Customer:
    def __init__(self, customer_id): pass


class Item:
    def __init__(self, barcode): pass


class Facade:
    @staticmethod
    def make_invoice(customer): return Invoice(customer)

    @staticmethod
    def make_customer(customer_id): return Customer(customer_id)

    @staticmethod
    def make_item(barcode): return Item(barcode)
