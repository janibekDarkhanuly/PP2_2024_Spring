class Point:
    def __init__(self,x1 = 0,x2 = 0):
        self.x1 = x1
        self.x2 = x2
    def show(self):
        print(self.x1)
        print(self.x2)
    def move(self):
        self.x1 = int(input())
        self.x2 = int(input())
        print("Changes are done!")
    def dist(self):
        print( abs(self.x2 - self.x1))
m1 = Point()
m1.show()
m1.move()
m1.dist()



