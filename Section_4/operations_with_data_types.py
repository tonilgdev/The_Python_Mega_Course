# Error messages in Python 3.10

# print("todai".replace("i","y")
# x = [1, 2 3]

# More operations with Lists

monday_temperatures =  [9.1, 8.8, 7.5]
monday_temperatures.append(8.1)
print(monday_temperatures)

monday_temperatures.clear()
print(monday_temperatures)

monday_temperatures =  [9.1, 8.8, 7.5]
print(monday_temperatures.index(8.8))

# print(monday_temperatures.index(8.8,2))

# Accessing list items
monday_temperatures =  [9.1, 8.8, 7.5]
monday_temperatures.index(8.8)
monday_temperatures.__getitem__(1)
monday_temperatures[1]

# Accessing list slices
monday_temperatures =  [9.1, 8.8, 7.5, 6.6,9.9]
print(len(monday_temperatures))
print(monday_temperatures[1:4])
print(monday_temperatures[3:])

# Accessing Items and Slices with Negative Indexes
monday_temperatures =  [9.1, 8.8, 7.5, 6.6,9.9]
print(monday_temperatures[-1])
print(monday_temperatures[-2:])
print(monday_temperatures[-4:-2])

#  Accessing Characters and Slices in Strings
monday_temperatures = ["hello", 1, 2, 3]
print(monday_temperatures[0])
print(monday_temperatures[0][2])

# Accessing Items in Dictionaries
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(student_grades["Sim"])

eng_port = {"rain":"chuva", "sun":"sol"}
print(eng_port["sun"])