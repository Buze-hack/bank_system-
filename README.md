# Buze Trust Bank System

A simple command-line banking system in Python that supports account creation, login, deposits, withdrawals, balance checks, and transaction history. PINs are securely hashed and hidden during input for security.

## Features

- Create Savings or Checking accounts
- Secure PIN storage (hashed with bcrypt)
- PIN input hidden (except during account creation)
- Deposit and withdraw money
- Minimum balance and overdraft rules
- View account balance (PIN required)
- View transaction history
- List all accounts (admin feature)

## Requirements

- Python 3.8+
- Packages: `bcrypt`

Install dependencies:

```bash
pip install bcrypt getpass
```

## Usage

Run the program:

```bash
python main.py
```

## Menu Options

- **Create Account**: Enter your name, choose account type, set a 4-digit PIN, and make an initial deposit.
- **Login**: Enter your account number and PIN (PIN input is hidden).
- **Deposit/Withdraw**: After login, deposit or withdraw money.
- **Check Balance**: Requires PIN verification (PIN input is hidden).
- **View Transactions**: See your transaction history.
- **List All Accounts**: Admin feature to list all accounts.
- **Exit**: Quit the program.

## Security Notes

- PINs are never stored in plain text.
- PINs are only visible during account creation for confirmation.
- All sensitive actions require PIN verification.

## File Structure

- `main.py` - Main program logic and user interface
- `bank.py` - Account classes and business logic

---

© 2025 Buze Trust Bank System
