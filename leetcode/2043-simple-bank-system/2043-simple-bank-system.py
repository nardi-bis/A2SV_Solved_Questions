class Bank:
   
    def validaccount(self, a):
        return 1 <= a <= self.n

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.validaccount(account1) and self.validaccount(account2):
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
            return False
        return False
    
    def deposit(self, account: int, money: int) -> bool:
        if self.validaccount(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.validaccount(account):
            if self.balance[account - 1] >= money:
                self.balance[account - 1] -= money
                return True
            return False
        return False
        
# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)