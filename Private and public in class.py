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




class pasrson:
    __name="anonymous"


    def __hello(self):
        print("hello people")

    def welcome(self):
        self.__hello()



p1=pasrson()
print(p1.welcome())