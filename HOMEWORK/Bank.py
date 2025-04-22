class Bank:
    def __init__(self, lihva=0.0, balance=0.0):
        self.__lihva = lihva
        self.__balance = balance
        self.__transactions = []

    def deposit(self, summa):
        if summa > 0:
            self.__balance += summa
            self.__transactions.append(f"Deposit: {summa}")
            print(f"Successfully deposited: {summa}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, summa):
        if summa > 0 and summa <= self.__balance:
            self.__balance -= summa
            self.__transactions.append(f"Withdrawal: {summa}")
            print(f"Successfully withdrew: {summa}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def add_lihva(self):
        interest = self.__balance * (self.__lihva / 100)
        self.__balance += interest
        self.__transactions.append(f"Interest added: {interest}")
        print(f"Interest earned: {interest}")
        print(f"New balance: {self.__balance}")

    def transaction_history(self):
        if self.__transactions:
            print("Transaction History:")
            for transaction in self.__transactions:
                print(transaction)
        else:
            print("No transactions yet.")

    def get_balance(self):
        print(f"Current balance: {self.__balance}")




print("Welcome to the Bank!")
initial_balance = float(input("Enter initial balance: "))
interest_rate = float(input("Enter interest rate (as a percentage): "))

account = Bank(balance=initial_balance, lihva=interest_rate)

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Add Interest")
    print("4. View Transaction History")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.add_lihva()
    elif choice == "4":
        account.transaction_history()
    elif choice == "5":
        account.get_balance()
    elif choice == "6":
        print("Thank you for using the Bank! Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")