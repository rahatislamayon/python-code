class psrson:
    name = "John"
    def change_name(self, name):
     self.name = name #    psrson.name = name


p1 = psrson()
p1.change_name("Alice")
print(p1.name)
print(psrson.name) #when psrson.name=name its changed to class attribute
 





#this also doing change class attribute
class psrson:
    name = "John"
    @classmethod
    def change_name(cls, name):
     cls.name = name


p1 = psrson()
p1.change_name("Alice")
print(p1.name)
print(psrson.name)