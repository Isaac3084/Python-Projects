class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. Current balance: ${self.balance}")

def bank_system():
    account = BankAccount("John Doe", 1000)
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            print(f"Current balance: ${account.balance}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
bank_system()
