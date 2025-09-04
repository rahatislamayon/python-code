print(1+2)
print("koli"+"pokoli")
print([1,2,3]+[4,5,6])


#complex number

class complev:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def printnumber(self):
        print(self.real,"i","+",self.img,"j")


    def add(self,other):
       new_real=self.real+other.real
       new_img=self.img+other.img
       return complev(new_real,new_img)

com1=complev(3,4)
com1.printnumber()
com2=complev(5,6)
com2.printnumber()
com3=com1.add(com2)
com3.printnumber()