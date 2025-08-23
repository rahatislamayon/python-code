#file i/o

# Types of all files
# 1 . Text Files : .txt, .docx, . log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.



# Character
# Meaning
# 'r'
# open for reading (default)
# 'w'
# open for writing, truncating the file first
# 'x'
# create a new file and open it for writing
# 'a'
# open for writing, appending to the end of the file if it exists
# 'b'
# binary mode
# 't'
# text mode (default)
# '+'
# open a disk file for updating (reading and writing)



file=open("demo.txt","r")
data =file.read()  #if you want read or write number of Character file.read(6)
                    # read or write at a one line line1 =file.readline()
                                                  #print(line1)
print(data)
print(type(data))
file.close()



file=open("demo.txt","a")
data=file.write("\n file i/o")
print(data)
file.close()





file=open("demo.txt","+r")
data=file.write("abc")
print(data)
file.close()





#with syntax

with open("demo.txt","r") as file:
    data=file.read()
    print(data)



    