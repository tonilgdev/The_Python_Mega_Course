# For Loops: How and Why
monday_temperatures = [9.1, 8.8, 7.6]

for temp in monday_temperatures:
    print(round(temp))

for letter in "hello":
    print(letter.title())

# Looping Through a Dictionary
student_grades = {"Marry": 9.1, "Sim": 8.8, "John":7.5}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)

# While Loops: How and Why
# a = 3
# 
# while a > 0:
#     print(1)
# 
# While Loop Example with User Input

username = ''

while username != "pypy":
    username = input("Enter username: ")

# While Loops with Break and Continue

while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue