
from bank import AccountManager
import getpass

manager = AccountManager()

def main_menu(account):
    while True:
        print(f"\n==== Account #{account.account_number} Menu ====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. List All Transactions")
        print("7. Exit")


        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdraw()
            elif choice == '4':
                check_balance()
            elif choice == '5':
                view_transactions()
            elif choice == '6':
                manager.list_accounts()
            elif choice == '7':
                print("Exiting the bank system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


def create_account():
    acc_type = input("Account type (savings/checking): ").strip().lower()
    name = input("Account holder name: ").strip()
    pin = input("set a 4-digit PIN: ").strip()
    balance = float(input("Initial deposit amount: "))
    manager.create_account(acc_type, name, pin, balance)

def deposit():
    acc_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    acc = manager.find_account(acc_number)
    acc.deposit(amount)
    print("Deposited successfull")

def withdraw():
    acc_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))
    acc = manager.find_account(acc_number)
    acc.withdraw(amount)
    print("Withdrawn successfull")

def check_balance():
    acc_number = int(input("Enter account number: "))
    pin = getpass.getpass("Enter your PIN: ")
    acc = manager.find_account(acc_number)
    bal = acc.grt_balance(pin)
    print(f"Current balance: ${bal:.2f}")

def view_transactions():
    acc_number = int(input("Enter account number: "))
    acc = manager.find_account(acc_number)
    acc.show_transactions()


def start_menu():
    while True:
        print("\n === welcome to the buze trust bank ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def login():
    try:
        acc_number = int(input("Enter account number: "))
        pin = getpass.getpass("Enter your PIN: ").strip()
        account = manager.find_account(acc_number)

        if not account.verify_pin(pin):
            print("Invalid PIN. Please try again.")
            return
        
        print(f"\n Welcome, {account.name}")
        main_menu(account)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    start_menu()
