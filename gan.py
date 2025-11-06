import time
import sys

lyrics = [
    "I'm a little teapot, short and stout",
    "Here is my handle, here is my spout",
    "When I get all steamed up, hear me shout",
    "Tip me over and pour me out!"
] 
delays =[0.3, 0.3, 0.4, 0.5]

def print_lyrics():

  print("Starting the teapot song...\n")
time.sleep(1.2)
for i, line in enumerate(lyrics): 
    for char in line: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        print()
        if i < len(delays):
            time.sleep(delays[i])
    else:
                time.sleep(0.3)
    print_lyrics()