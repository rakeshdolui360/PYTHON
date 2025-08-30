
class account:
    
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def credit(self,amount):
        self.balance-=amount
        print(f"{amount} was debited")
        print(f"available balance is = {self.balance}")
        
    def debit(self,amount):
        self.balance+=amount
        print(f"{amount} was credited")
        print(f"available balance is = {self.balance}")
    
    
    def get_balance(self):
        return self.balance
     
        
acc1=account(50000,42011)
acc1.credit(10000)
acc1.debit(20000)
acc1.credit(9000)
print(acc1.get_balance())