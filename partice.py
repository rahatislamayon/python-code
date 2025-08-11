# str="iam $ rich guy $ i have many $ friends $ and i love to play $ games"
# print(str.count("$"))
# # Output: 5

# print("enter your favorite three movies name:")
# movie1 = input("1st movie: ")
# movie2 = input("2nd movie: ")   
# movie3 = input("3rd movie: ")
# movies=[movie1, movie2, movie3]
# print("Your favorite movies are:", movies)


# list1=input("Enter a list of numbers separated by spaces: ")
# list1 = list1.split()  # Convert the input string to a list

# list_copy=list1.copy()
# list_copy.reverse()
# if list_copy==list1:
#     print("The list is a palindrome")
# else:
#     print("The list is not a palindrome")

# gread=("A", "A", "B", "C", "A", "B", "A", "C", "A", "B")
# print(gread.count("A")) 

list=["E","B","C","A","D","F"]
list.sort()
print(list)
list.sort(reverse=True)
print(list)  # ['F', 'E', 'D', 'C', 'B', 'A']