class account:
    def __init__(self,owner = "",balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        self.depo = int(input())
        if(self.depo) < 0:
            print("Nelzya popolnit otricatelnoe chislo")
        else:
            self.balance = self.balance + self.depo
    def withdrawal(self):
        self.withdrawal = int(input())
        if(self.balance - self.withdrawal)< 0:
            print("there are not enough funds on the balance sheet")
        else:
            self.balance = self.balance - self.withdrawal
    def show(self):
        print(self.balance)
a = account()
a.show()
a.deposit()
a.show()
a.withdrawal()
a.show()
