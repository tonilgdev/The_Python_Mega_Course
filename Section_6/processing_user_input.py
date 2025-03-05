# User input

def weather_condition(temperature:float):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input  = float(input("Enter temperature: "))
print(weather_condition(user_input))

# String formatting
user_input = input("Enter your name: ")
message = "Hello, %s!" %user_input
message = f"Hello, {user_input}!"
print(message)

# Stirng formatting with multiple variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")
message = "Hello, %s!" %user_input
message = f"Hello, {user_input}!"
print(message)

message = "Hello %s %s" % (name, surname)
message = f"Hello my name is {name} {surname}"
print(message)
