class myClass:
    def getString(self):
        self.str = input()
        self.str = self.str.upper()
    def printString(self):
        print(self.str)
s1 = myClass()
s1.getString()
s1.printString()