# num=[1,2,3,4,5,6,7,8,9,10]
# for val in num:
#     print(val)


# str="hello world"
# for element in str:
#     if element=="r" :
#         print("Found 'r', stopping the loop.")
#         break
#     print(element)
# else:
#     print("End of string")




#     str="hello world"
# for element in str:
#     if element=="r" :
#         print("Found 'r', stopping the loop.")
#         continue
#     print(element)
# else:
#     print("End of string")



    
#     num =[1,4,9,16,25,36,49,64,81,100]
# for i in num:
#     x =49
#     if i == x:
#         print("The number is found at index:", num.index(i))
#         break
#     print(i)
#     i+=1

# for el in num:
#     if el== 49:
#         print("the number is found")


# #range

# seq = range(6)  # range(2,6)   #range(start, stop, step)
# for i in seq:
#     print(i)


#     seq1=range(0,20,5) #step of 5
# for i in seq1:
#     print(i)




#     i=0
#     for i in range(101,0,-1):
#             print(i)



# n=int(input("Enter a number: "))
# for i in range(1,100):
#  print(n * i)





n =5
sum = 0
for i in range(1,n+1):
    sum += i
print("The sum of the first", n, "natural numbers is:", sum)

# Manual Trace:
# Initialization:

# n = 5
# n is assigned the value 5.

# sum = 0
# sum is initialized to 0.

# Loop Execution:
# The for loop iterates over the range range(1, n+1), which is range(1, 6). This generates the sequence [1, 2, 3, 4, 5].

# Iteration 1: i = 1

# sum += i → sum = 0 + 1 → sum = 1

# Iteration 2: i = 2

# sum += i → sum = 1 + 2 → sum = 3

# Iteration 3: i = 3

# sum += i → sum = 3 + 3 → sum = 6

# Iteration 4: i = 4

# sum += i → sum = 6 + 4 → sum = 10

# Iteration 5: i = 5

# sum += i → sum = 10 + 5 → sum = 15



n =5
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
