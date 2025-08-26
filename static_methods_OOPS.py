class car:
    garage_name="XYZ Garage"
    def __init__(self,model,color,condition):
        self.model=model
        self.color=color
        self.condition=condition
        print("car details added")
    @staticmethod
    def hello():
     print("hello welcome to the car garage")       

    def welcome(self):
     print("welcome to the car garage",self.model)


    def con(self):
        print("the car is in",self.condition,"condition")


car1=car("BMW","Black","New")
print(car1.model)
print(car.garage_name)
car1.hello()

car2=car("audi","red","used")
print(car2.color)
print(car2.garage_name)

