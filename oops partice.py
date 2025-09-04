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



class employee:
    def __init__(self,name,defarment,salary):
        self.name=name
        self.defarment=defarment
        self.salary=salary
    

    def display(self):
        print("name:",self.name)
        print("defarment:",self.defarment)
        print("salary:",self.salary)

class engineer(employee) :
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("sub engineer", "ict", 30000)

emp1=employee("koli","IT",25000)
emp1.display()


emp2=engineer("john",30)
emp2.display()





class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, oed2):
        return self.price > oed2.price


oed1=order("nudle",50)
oed2=order("pizza",200)

print(oed1>oed2)
print(oed2>oed1)