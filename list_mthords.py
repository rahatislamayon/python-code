num=[1,2,3,4,5,6,7,8,9,10] #list Slicing.
num.insert(4,69) #1, 2, 3, 4, 69, 5, 6, 7, 8, 9, 10]
num.append(11)
print(num,)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

list=[6,2,5,1,9,3,4,8,7]
list.sort()
print(list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


list1=[6,2,5,1,9,3,4,8,7]
list1.sort(reverse=True)
print(list1)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]


list2=["volovo", "toyota", "honda", "bmw", "audi"]
list2.sort()
print(list2)  # ['audi', 'bmw', 'honda', 'toyota', 'volovo']

list2.reverse()
print(list2)  # ['volovo', 'toyota', 'honda', 'bmw', 'audi']\

list2.remove("honda")
print(list2)  # ['volovo', 'toyota', 'bmw', 'audi']
list2.pop(1)
print(list2)  # ['volovo', 'toyota', 'bmw']





