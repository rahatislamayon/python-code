# class car:
#     color = "blue"

# car1 = car()
# car2 = car()
# print(car1.color)



class student:
    def __init__(self,fullname):
        self.name= fullname
        print("adding student details")


s1 = student("John Doe")
print(s1.name)



class car:
    garage_name="XYZ Garage"
    def __init__(self,model,color,condition):
        self.model=model
        self.color=color
        self.condition=condition
        print("car details added")

def welcome(self):
    print("welcome to the car garage",self.model)


    def con(self):
        print("the car is in",self.condition,"condition")


car1=car("BMW","Black","New")
print(car1.model)
print(car.garage_name)


car2=car("audi","red","used")
print(car2.color)
print(car2.garage_name)




    
class student:
    def __init__(self,name,marks):
      self.name= name
      self.marks= marks
      
   
    def avg (self):
          sum=0
          for i in self.marks:
             sum+=i
          print("hi",self.name,"your average is:",sum/len(self.marks))




    
    
    
s1=student ("kolo",[39,58,90.23,78,45],)
s1.avg()



# Important
# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.


class car:
    def __init__(self):
        self.accelaration=False
        self.brakes=False
        self.cluth=False

    def start(self):
        self.accelaration=True
        self.brakes=True
        self.cluth=True
        print("the car has started")


car1=car()
car1.start()





