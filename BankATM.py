from numpy.random import choice


class Bank:

    def __init__(self,balance):
        self.balance = balance

    def deposite(self,amount):
        if amount <= 0:
            raise ValueError("Deposite amount must be positive")
        else:
            self.balance += amount
            print(f"Deposited {amount}, Current Balance {self.balance}")

    def withdraw(self,amount):
        if amount>=self.balance:
            raise ValueError("Insufficient Balance")
        else:
            self.balance -= amount
            print(f" Withdrawn: {amount}, Current Balance: {self.balance}")



    def checkbalance(self):
         print(f"Your curent balance is {self.balance}")


try:
    acc = Bank(1000)

    while True:
        print("\n--- ATM Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choose = int(input("Enter choice"))

        if choose==1:
           amt = float(input("Enter Deposite amout"))
           acc.deposite(500)
        elif choose ==2:
                    amt = float(input("Enter withdraw amount: "))
                    acc.withdraw(amt)

        elif choose == 3:
            acc.check_balance()

        elif choose == 4:
            print("Thank you for using ATM. Goodbye!")
            break

        else:
            print(" Invalid choice! Please try again.")

except ValueError as v:
    print("value error",v)

except Exception as e:
    print("something went wrong",e)

finally:
    print("ATM session closed!")


















