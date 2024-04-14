class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,length = 0,width = 0):
        self.length = length
        self.width = width
    def getArg(self):
        self.length = int(input())
        self.width = int(input())
    def area(self):
        return self.width * self.length
rectangle = Rectangle()
rectangle.getArg()
print(rectangle.area())
    
