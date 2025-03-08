# Reading Text From a File

my_file = open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/fruits.txt")
print(my_file.read())

# File Cursor

# - The cursor after read() method goes to the end of the file to print the content more than one time, save the ontent to a variable

# Closing a File

my_file = open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/fruits.txt")
content = my_file.read()
my_file.close()
print(content)

# Opening Files Using "with"

with open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/fruits.txt") as my_file_with:
    content_with = my_file_with.read()

print(content_with)

# Writing Text to a File

print("Writing Text to a File")

with open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/vegetables.txt","w") as my_file_with:
    my_file_with.write("Tomato\n")
    my_file_with.write("Garlic")

# Appending Text to an Existing File

with open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/vegetables.txt","a+") as my_file_with:
    my_file_with.write("\nAdded!\n")
    my_file_with.seek(0)
    content = my_file_with.read()

print(content)