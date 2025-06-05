class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance =0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited Rs. {amount:.2f}. New balance is Rs. {self.balance:.2f}.")
        else:
            print("Deposite amount must be positive.")    
    def withdraw (self, amount):     
        if 0 < amount<= self.balance:
            self.balance-=amount
            print(f"withdraw Rs. {amount:.2f}. New balance is Rs. {self.balance:.2f}.")
        else:
            print("Insufficient funds or Invalid amount.")
    def get_balance(self):
        return self.balance
    def __str__(self):
        return(f" Account Number: {self.account_number}\n"
               f"Holder Name:{self.holder_name}\n"
             f"Balance: Rs.{self.balance:.2f}")
if __name__=="__main__":
    account =BankAccount("123456789", "Priya", 20000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    print(F"Final balance:Rs.{account.get_balance():.2f}")
               
