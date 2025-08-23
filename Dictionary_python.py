# info={
#     "mane": "Dictionary in Python",
#     "divise":"windows",
#     "from": "Python",
# }
# print(info)
# print(type(info))

# info["form"]="lakshmipur"
# info["country"]="bangladesh"
# print(info)



#nested dictionary
student={
    "mame":"ayon",
    "num":{
        "math": 85,
        "science": 90,
        "english": 88,
        "teachers":{
            "name": "Rahman",
            "bisoy":{
                "subject": "Physics",
                "experience": 5
            }
            
          
        }
    }
}
# print(student)
# print(student["num"]["math"])  # Accessing nested dictionary value\
# print(student["num"]["teachers"]["bisoy"]["experience"])  # Accessing nested dictionary value
# print(student["num"]["teachers"]["bisoy"]["subject"])  # Accessing nested dictionary value


#print(student.keys())
# print(list(student.keys()))
# print(len(student.keys()))


# print(student.values()) #display all values
# print(list(student.values()))  # Convert values to a list


# print(student.items())  # Display all key-value pairs
# print(list(student.items()))  # Convert items to a list of tuples

# pairs = list(student.items())
# print(pairs[0])  # Access the first key-value pair


# print(student.get("mame"))  # Access value using get method
# print(student.get("age", "Not Found"))  # Access non-existing key with default value
student.update({"info": "Student Information"})  # Update dictionary with new key-value pair
print(student)




