#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.transactions = []

    def add_item(self, item_name, price, quantity = 1):
        self.total += price * quantity
        self.items.extend([item_name]*quantity)
        self.transactions.append(price * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_transaction = self.transactions.pop()
            self.total -= last_transaction
        else:
            print("no transactions to void.")

    def get_items(self):
        return self.items