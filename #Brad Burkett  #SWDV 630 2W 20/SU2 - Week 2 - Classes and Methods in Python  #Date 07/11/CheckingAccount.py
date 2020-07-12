#Brad Burkett

#SWDV 630 2W 20/SU2 - Week 2 - Classes and Methods in Python

#Date 07/12/2020

class CheckingAccount:
    def __init__(self, lastName, homeAddress, accountNumber, accountBalance):
        self.lastName = lastName
        self.homeAddress = homeAddress
        self.accountNumber = accountNumber
        self._accountBalance = accountBalance

    def __str__(self):
        return f"{self.lastName}, {self.homeAddress}, Account No: {self.accountNumber}, Account Balance: ${self._accountBalance:.2f}"

    def withdrawal(self, amount):
        if amount > self._accountBalance:
            print("You can not withdraw an amount that exceeds your available balance\n")
            print(f"Your available Account Balance is: ${self._accountBalance:.2f} \n")
        elif amount <= self._accountBalance:
            self._accountBalance -= amount
            print( f" ${amount:.2f} has been deducted from account.\n New Account Balance is: ${self._accountBalance:.2f}")
        return self._accountBalance

    def deposit(self, amount):
        self._accountBalance += amount
        print (f" ${amount:.2f} has been deposited in your account.\n New Account Balance is: ${self._accountBalance:.2f}")
        return self._accountBalance


def main(): #This is the ATM transctions
    owner = CheckingAccount("Burkett", "Avon, Indiana", "xxx999", 500)
   
    print("Welcome to the Bank of Indiana \n")

    
    while True:
        #Enter Transaction Code
        print("Please choose a transaction Code: ")
        transactionCode = input(" (1) Check Account Balance\n (2) Deposit funds\n (3) Withdraw Funds\n (4) End Transaction\n ").upper()
        
        #Display available Account Balance
        if transactionCode == "1":
            print()
            print(f"Available accountBalance: ${owner._accountBalance:.2f} \n")
            
        #Deposit amount and add to current account balance and display total balance
        elif transactionCode == "2":
            amount = float(input("How much would you like to deposit? $"))
            owner.deposit(amount)
            print()
            
        #Withdrawal and subtract amount from current account balance and display total balance
        elif transactionCode == "3":
            amount = float(input("How much would you like to withdraw? $"))
            owner.withdrawal(amount)
            print()
            
        #End Transaction
        elif transactionCode == "4":
            print("\n")
            print("Transaction Ended")
            break
        
        #Error Invalid input
        else:
            print("\n")
            print("Input " +str(transactionCode)+ " is an invaled entry.\n")
             

main()
