# Functions with multiple arguments

def area (a,b):
    return a*b

print(area(4,5))

# Default and No-default Parameters and Keyword and Non-keyword Arguments

def area (a,b):
    return a*b

print(area(a = 4, b = 5))
print(area(b = 4, a = 5))

def area (a,b = 6):
    return a*b

print(area(a = 4, b = 8))

# Functions with an Arbitrary Number of Non-keyword Arguments

def mean(*args):
    return type(args)

print (mean(1,2,3))

def mean(*args):
    return sum(args)  / len (args)

print (mean(1,2,3))

# Functions with an Arbitrary Number of Kwyword Arguments

def mean(**kwargs):
    return kwargs

print(mean(a = 1,b = 2,c = 3))
