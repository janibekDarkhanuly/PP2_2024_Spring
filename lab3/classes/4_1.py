import math
class Point:
    def __init__(self,x1 = 0,x2 = 0,y1 =0,y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def show(self):
        print(self.x1,self.y1)
        print(self.x2,self.y2)
    def move(self):
        coordinates1 = input().split()
        self.x1 = int(coordinates1[0])
        self.y1 = int(coordinates1[1])
        cordinates2 = input().split()
        self.x2 = int(cordinates2[0])
        self.y2 = int(cordinates2[1])
        print("Changes are done!")
    def dist(self):
        print(math.sqrt(math.pow((self.x2 - self.x1), 2) + math.pow((self.y2 - self.y1), 2)))

m1 = Point()
m1.show()
m1.move()
m1.dist()
