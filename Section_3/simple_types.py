x = 10 
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1,sum2)
print(type(x), type(y), type(z))

#lists

student_grades = [9.1, 8.8, 7.5]

student_grades2 = [9, "Hello", [1,2,4.33]]

print(student_grades)

#ranges

student_grades = range(0,11)
print(student_grades)

student_grades = list(range(0,11))
print(student_grades)

student_grades = list(range(0,11,2))
print(student_grades)

#data atributtes

dir(list)
help(str.upper)

#find the code that you need 

# search in a git shell dir(list) or dir(__builtins__)
student_grades = [9.1, 8.8, 7.5]
mysum = sum(student_grades)
l = len(student_grades)

mean = mysum / l

print(mean)

#dictionary type

student_grades = {"Marry": 9.1, "Sim":8.8, "John":7.5}
mysum = sum (student_grades.values())
length = len(student_grades)
mean = mysum/length
print(mean)

#TUples (They are inmutables, The are faster than lists)

monday_temperatures = (1,4,5)
print(monday_temperatures)