num=[1,2,3,4,5,6,7,8,9,10]
for val in num:
    print(val)


str="hello world"
for element in str:
    if element=="r" :
        print("Found 'r', stopping the loop.")
        break
    print(element)
else:
    print("End of string")




    str="hello world"
for element in str:
    if element=="r" :
        print("Found 'r', stopping the loop.")
        continue
    print(element)
else:
    print("End of string")

#range

seq = range(6)  # range(2,6)   #range(start, stop, step)
for i in seq:
    print(i)


    seq1=range(0,20,5) #step of 5
for i in seq1:
    print(i)