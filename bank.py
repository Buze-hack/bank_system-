
from datetime import datetime
import bcrypt

class BankAccount:
    _next_account_number = 1001

    def __init__(self, name: str, pin: str, balance: float = 0.0):
        self.account_number = BankAccount._generate_account_number()
        self.name = name
        self._pin_hash = self._hash_pin(pin)
        self.balance = balance
        self.transactions = []
    @staticmethod
    def _hash_pin(pin: str) -> bytes:
        return bcrypt.hashpw(pin.encode(), bcrypt.gensalt())

    def verify_pin(self, pin: str) -> bool:
        return bcrypt.checkpw(pin.encode(), self._pin_hash)
        
    @classmethod
    def _generate_account_number(cls):
        account_number = cls._next_account_number
        cls._next_account_number += 1
        return account_number
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._add_transaction("Deposit", amount)
        return self.balance
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._add_transaction("Withdraw", amount)
        return self.balance
    
    def grt_balance(self, pin: str):
        if not self.verify_pin(pin):
            raise PermissionError("Invalid PIN.")
        return self.balance
    
    def _add_transaction(self, type_: str, amount: float):
        self.transactions.append({
            "type": type_,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return
        for transaction in self.transactions:
            print(f"[{transaction['timestamp']}] {transaction['type']}: ${transaction['amount']:.2f}")

class SavingsAccount(BankAccount):
    MIN_BALANCE = 100.0
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Cannot go below minimum balance of ${self.MIN_BALANCE}.")
        self.balance -= amount
        self._add_transaction("Withdraw", amount)
        return self.balance
    
class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = 500.0

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.OVERDRAFT_LIMIT:
            raise ValueError(f"Cannot withdraw beyond overdraft limit of ${self.OVERDRAFT_LIMIT}.")
        self.balance -= amount
        self._add_transaction("Withdraw", amount)
        return self.balance


class AccountManager:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_type: str, name: str, pin: str, balance: float):
        if account_type == "savings":
            account = SavingsAccount(name, pin, balance)
        elif account_type == "checking":
            account = CheckingAccount(name, pin, balance)
        else:
            raise ValueError("Invalid account type. Choose 'savings' or 'checking'.")
        
        self.accounts.append(account)
        print(f"{account_type.capitalize()} account created for {name} with account number {account.account_number}.")
        return account
    
    def find_account(self, account_number: int):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        raise ValueError("Account not found.")
    
    def list_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        for account in self.accounts:
            print (f"Account Number: {account.account_number}, Name: {account.name}, Balance: ${account.balance:.2f}")

        