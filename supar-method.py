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
        super().start()
        super().stop()


c1=lexus("RX")
print(c1.type)
