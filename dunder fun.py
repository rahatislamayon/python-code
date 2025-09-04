

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