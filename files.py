# r = read
# a = append
# w = write
# x = create
import os
from turtle import title
from venv import create


title = " Lesson 22 - Files Operations in Python"
print(f'{title}\n{"=" * len(title)}')

title = 'Read Files - error if it does not exist'
print(f'\n{title}\n{"-" * len(title)}')

f = open("names.txt", "r")
# print(f.read())  # Output: Sisovin, Sovanny, Vuddhi, Viphea, Viphop - reads the whole file
# print(f.read(4)) # Output: Siso - reads the first 4 characters

# print(f.readline())  # Output: Sisovin - reads the first line
# print(f.readline())  # Output: Sovanny - reads the second line 

for line in f:
    print(line)
    
f.close()

try:
    f = open("names_list.txt")
    print(f.read())
except:
    print(f"\nThe File you want to read doesn't exist")
finally:
    f.close()

title = 'Append Files - create the file if it does not exist'
print(f'\n{title}\n{"-" * len(title)}')
# f = open("names.txt", "a")
# f.write("\nVuthy")
# f.close()

f = open("names.txt", "r")
print(f.read())
f.close()

title = ' Write (Overwrite) Files '
print(f'\n{title}\n{"-" * len(title)}')
f = open("context.txt", "w")
f.write("I deleted all of the context in this file")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()

""" f = open("context.txt", "a")
f.write("\nSisovin\nSovanny\nVuddhi\nViphea\nViphop")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close() """

title = " Two ways to create a new file "
print(f'\n{title}\n{"-" * len(title)}')
# Opens a file for writing, creates the file if it does not exist
f = open("name_file.txt", "w")
f.close()

title = " Create the specified file, but returns an error if the file exist "
print(f'\n{title}\n{"-" * len(title)}')
if not os.path.exists("name_file.txt"):
    f = open("name_file.txt", "x")
    f.close()
else:
    print("The file already exists")
    
title = " Delete a file "
print(f'\n{title}\n{"-" * len(title)}')
import os

def delete_file():
    print("\nWhat file do you want to delete? Please enter the file name with extension: \n")
    fileName = input().strip()  # Strip any leading/trailing whitespace
    if os.path.exists(fileName):
        os.remove(fileName)
        print("The file has been deleted")
    else:
        print("The file you wish to delete does not exist")

# Call the function to delete the file
delete_file()

title = " Using with Statement: Automatically close the file "
print(f'\n{title}\n{"-" * len(title)}')
with open("names.txt", "r") as f:
    content = f.read()
    print(content)
    f.close()
    
print(f"\nIs the file closed? {f.closed}") # Output: True

with open("names.txt", "w") as f:
    f.write(content)
    print(f"\nIs the file closed? {f.closed}") # Output: False
    
