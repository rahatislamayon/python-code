class car :
    @staticmethod
    def start():
        print("The car has started.")

    @staticmethod
    def stop():
        print("The car has stopped.")


class toyta(car):
    def __init__(self,name):
        self.name=name



car1=toyta("Corolla")
car2=toyta("Camry")

print(car1.name)
print(car1.start())





#Multi label inheritance

class car :
    @staticmethod
    def start():
        print("The car has started.")

    @staticmethod
    def stop():
        print("The car has stopped.")


class toyta(car):
    def __init__(self,name):
        self.name=name


class lexus(toyta):
    def __init__(self,type):
        self.type=type

car1=lexus("RX")
car2=lexus("NX")

print(car1.type)
print(car1.start())


#multiple inheritance
class a:
    varA="helo from class A"

class b:
    varB="helo from class B"

class c(a,b):
    varC="helo from class C"


c1=c()
print(c1.varA)
print(c1.varB)
print(c1.varC)


#super method
class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("The car has started.")

    @staticmethod
    def stop():
        print("The car has stopped.")


class lexus(car):
    def __init__(self,type):
        super().__init__(type)



c1=lexus("RX")
print(c1.type)