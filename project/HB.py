import time
import time
import random
import pyfiglet as pf
from pyfiglet import Figlet
from termcolor import colored

# Write your message here
Text = "Happy Birthday"

# Enter his/her name (set a default if empty)
Name = "AYON"  # Change this to the recipient's name

# Reverse your given name
#reverseText = Name[::-1]

colorList = ['red', 'green', 'yellow', 'blue']
timeInterval = [0.2, 0.3, 0.2, 0.4]


# Getting all the font types from 'fonts.txt' and storing into a list
dataList = []
try:
    with open('../fonts.txt') as f:
        for line in f:
            font = line.strip()
            if font:
                dataList.append(font)
except FileNotFoundError:
    print("fonts.txt not found. Please ensure it exists in the parent directory.")
    dataList = ["standard"]

# This part of the code prints the message
# with different font types(fixed and randomly)
#==================================
for i in range(1, 100):
    if i % 10 == 0:
        textArt = pf.figlet_format(Text)
        print("\n" + textArt)
    elif i % 9 == 0:
        textArt = pf.figlet_format(Text, font="xsbook")
        print(textArt)
    elif i % 5 == 0:
        F = Figlet(font=random.choice(dataList))
        textArt = colored(F.renderText(Name), random.choice(colorList))
        print("\n" + textArt)
    elif i % 8 == 0:
        F = Figlet(font=random.choice(dataList))
        textArt = colored(F.renderText(Text), random.choice(colorList))
        print("\n" + textArt)
    elif i % 7 == 0:
        textArt = pf.figlet_format(Text, font=random.choice(dataList))
        print("\n" + textArt)
    # elif i % 4 == 0:
    #     textArt = pf.figlet_format(reverseText)
    #     print("\n" + textArt)
    else:
        print("")
    time.sleep(random.choice(timeInterval))