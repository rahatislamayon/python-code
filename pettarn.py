input_string = input("Enter a number: ")
n = int(input_string)

for i in range(n):                             
    for j in range(n):
        print("*", end=" ")
    print()


for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


    for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i+1):
        print(" ", end=" ")
    print()

for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()


for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()


This loop builds the pyramid pattern.
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()





for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(i,n-1):
            print("*", end=" ")
        for j in range(i,n):
            print("*", end=" ")
        print()


for i in range(n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()





for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(i,n-1):
            print("*", end=" ")
        for j in range(i,n):
            print("*", end=" ")
        print()
