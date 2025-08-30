# class student:
#     def __init__(self,name):
#         self.name = name
# s1 = student("John")
# #del s1
# print(s1.name)




class bank:
    def __init__(self,ac_no,pas):
        self.ac_no = ac_no
        self.__pas = pas


    def reset_pas(self):
        print(self.__pas) 



ac1 = bank(12345,"abcde")
print(ac1.ac_no)
#print(ac1.__pas)
