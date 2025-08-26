
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