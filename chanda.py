class Chada:
    def __init__(self, serviceName, baseChada):
        self.serviceName = serviceName
        self.baseChada = baseChada

    def displayInfo(self):
        print(f"Service: {self.serviceName}, Base Chada: {self.baseChada}")

   
    def calculateChada(self, quantity=None, extraPercent=None):
        if quantity is None and extraPercent is None:
        
            return self.baseChada
        elif extraPercent is None:
          
            return self.baseChada * quantity
        else:
          
            return (self.baseChada * quantity) + (self.baseChada * (extraPercent / 100))



class BusChada(Chada):
    def displayInfo(self):
        print(f"Bus Service: {self.serviceName}, Base Chada: {self.baseChada}")

class AutoStandChada(Chada):
    def displayInfo(self):
        print(f"Auto Stand Service: {self.serviceName}, Base Chada: {self.baseChada}")
        print("Includes: Extra 10% for prio ovivabok + singara coke costs")


bus = BusChada("Dhaka City Bus", 50)
auto = AutoStandChada("Mohakhali Auto Stand", 30)

print("BusChada calculateChada():", bus.calculateChada())
print("BusChada calculateChada(3):", bus.calculateChada(3))
print("BusChada calculateChada(3, 20):", bus.calculateChada(3, 20))

print("AutoStandChada calculateChada():", auto.calculateChada())
print("AutoStandChada calculateChada(2):", auto.calculateChada(2))
print("AutoStandChada calculateChada(2, 10):", auto.calculateChada(2, 10))

chadaRef = bus
chadaRef.displayInfo()

chadaRef = auto
chadaRef.displayInfo()


