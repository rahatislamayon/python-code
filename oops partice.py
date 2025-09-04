class circle:
    def __init__(self,redius):
        self.redius=redius


    def area(self):
        return 3.14*self.redius**2

    def perimeter(self):
        return 2*3.14*self.redius    

c1=circle(21)
print(c1.area())
print(c1.perimeter())  