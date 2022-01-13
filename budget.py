class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"

            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        """A deposit method that accepts an amount and description.
         the method append an object to the ledger list in the form of
         {"amount": amount, "description": description """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        amount should be stored as negative number, returns True if withdrawal took place, otherwise
        returns false
        """
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        a method that returns the current balance of the budget
        """
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]

        return total_cash

    def check_funds(self, amount):
        """
        check amount with balance
        """
        if self.get_balance() >= amount:
            return True
        return False

    def transfer(self, amount, category):
        """
        transfer amount from one category to another
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False