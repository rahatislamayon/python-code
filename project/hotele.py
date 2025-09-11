manu={
    "pizza":70,
    "burger":50,
    "pasta":60,
    "salad":40,
    "coke":30,
}

print("Welcome to the Hotel!")
print("menu:", manu)

order_total=0

item1=input("Enter your first item: ")
if item1 in manu:
    order_total+=manu[item1]
    print(f"{item1} add to your  orde. price is :{manu[item1]}")
else:
    print(f"sorry we dont have this :{item1} in our menu")


print("you can order one more item ? yes/no")
if input()=="yes":
 item2=input("Enter your second item: ")
 if item2 in manu:
     order_total+=manu[item2]
     print(f"{item2} add to your  orde. price is :{manu[item2]}")
 else:
     print(f"sorry we dont have this :{item2} in our menu")
print("thank you for your order")
print(f"your total order amount is :{order_total}")