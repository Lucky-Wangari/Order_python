class Account:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        balance = sum(transaction["amount"] for transaction in self.deposits) - sum(transaction["amount"] for transaction in self.withdrawals)
        return balance

    def deposit(self, amount):
        transaction = {"amount": amount, "narration": "deposit"}
        self.deposits.append(transaction)

    def withdrawal(self, amount):
        transaction = {"amount": amount, "narration": "withdrawal"}
        self.withdrawals.append(transaction)

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= sum(transaction["amount"] for transaction in self.deposits) / 3:
            self.loan_balance = amount
            print("Loan approved. Loan balance updated.")
        else:
            print("Loan request not approved.")

    def repay_loan(self, amount):
        if amount >= self.loan_balance:
            self.loan_balance = 0
            self.deposit(amount - self.loan_balance)
            print("Loan fully repaid. Excess amount added to account balance.")
        else:
            self.loan_balance -= amount
            print("Loan partially repaid.")

    def transfer(self, amount, destination_account):
        if amount <= self.check_balance():
            self.withdrawal(amount)
            destination_account.deposit(amount)
            print("Transfer successful.")
        else:
            print("Insufficient funds for transfer.")


# Example usage:
account1 = Account()
account2 = Account()

account1.deposit(1000)
account1.withdrawal(500)
account1.print_statement()

account1.borrow_loan(200)
account1.repay_loan(150)

account1.transfer(300, account2)
