# def shown(n):
#  print(n)
#  if n==0:
#   return
#  shown(n-1)

# num=int(input("enter number"))
# shown(num)





# def number(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * number(n - 1)


# print(number(5))



def nutcal(n):
    if n==0:
        return 0
    else:
        return n + nutcal(n-1)    
num=int(input("enter number:"))
print(nutcal(num))



def print_list(list,index):
    if index==len(list):
        return
    print(list(index))
    print_list(list(index+1))


cuntry=["nepal","india","china","bhutan"]
print_list(cuntry,0)