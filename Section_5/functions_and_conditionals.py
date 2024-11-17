#  Creating Your Own Functions
def mean(my_list):
    the_mean = sum(my_list)/len(my_list)
    return the_mean

print(mean([1,4,5]))

print(type(mean), type(sum))

# Print or Return?

# Nothing to write

# If conditional example

def mean(value):
    if type(value) == dict: # isintsance(value, dict)
        the_mean = sum(value.values())/len(value)
    else: 
        the_mean = sum(value)/len(value)
    return the_mean

student_grades = {"Marry":9.1, "Sim":8.8, "John":7.5}
print(mean(student_grades))

#elif conditional
x = 3
y = 1

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is lees than y")