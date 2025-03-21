# Syntax error

print(1)
int(9)
# int 9 no brackets error (syntax error)

print(2)
# print 3 no brackets error (syntax error)

# Runtime Errors
a =1
b= "2"
c=2
print(int(2.5))
print(a + float(b))
#print(c/0)

# Making the Code handle Errors by Itself

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You are dividing by Zero."

print(divide(1,2))
print(divide(1,0))
print("End of program")