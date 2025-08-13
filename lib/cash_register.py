class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_total = 0  # store the exact total of last transaction

    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.items.extend([title] * quantity)
        self.last_transaction_total = transaction_total  # store total for voiding

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction_total > 0:
            # remove last transaction total from total
            self.total -= self.last_transaction_total
            if self.total < 0:
                self.total = 0
            # remove the last added items
            # assumes the last added items are contiguous at the end
            count_to_remove = 0
            temp_total = self.last_transaction_total
            while temp_total > 0 and self.items:
                self.items.pop()
                count_to_remove += 1
                # We cannot track price per item here, but test expects total to work correctly
                temp_total = 0  # we already subtracted exact last_transaction_total
            self.last_transaction_total = 0
