class bank:
    def __init__(self,ah):
        self.IFSC_CODE="da1rra2"
        self.closing_balance=0
        self.account_holder=ah

    def display(self):
        print("welcome :",self.account_holder)
        print("your ifsc is ",self.IFSC_CODE)
        print("please choose.")
        print("1.Deposit" '\n' "2.withdraw" '\n')
        choice = int(input("please make a choice :"))
        if choice==1:
            self.deposit()
        elif choice==2:
            self.withdraw()
        elif choice !=1 or choice !=2:
            print("Thanks")
            print("if you want to continue:" '\n' "select Y/N:")
            aa = str(input("enter the choice:"))
            if aa == Y or y:
                self.display()
            else:
                print("Thanks for visiting.")

        return

    def deposit(self):
        print("Welcome to deposit")
        deposit_amount=int(input("enter the Deposit Amount:"))
        self.deposit_amount=self.closing_balance+ deposit_amount
        print("Thanks for the deposit  ")
        print("your closing balance is :",self.closing_balance)
        print("if you want to continue:" '\n' "select Y/N:")
        aa = str(input("enter the choice:"))
        if aa == "Y" or "y":
            self.display()
        else:
            print("Thanks for visiting.")
        return self.deposit_amount



    def withdraw(self):
        print("Welcome to Withdraw")
        withdraw_amount=int(input("Enter the Withdraw Amount"))
        if self.closing_balance < withdraw_amount:
            print(self.closing_balance)
            print("insufficient Funds")
        else:
            self.withdraw_amount=closing_balance - withdraw_amount
            print("do you want to check balance '\n' choose Y/N")
            balance_check = str(input("enter the choice :"))
            if balance_check == Y or y:
                print("your closing balance is ",self.closing_balance)
            else:
                print("Thanks for visiting")
        return self.closing_balance

#test

obj1=bank("dharan")
obj1.display()
# obj1.withdraw()
# obj1.deposit()