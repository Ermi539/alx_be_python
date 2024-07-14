# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount with an optional initial balance (default is 0).
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        Returns True if successful, False otherwise.
        """
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)  # Example starting balance

    # Command line interaction (similar to main-0.py)
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
