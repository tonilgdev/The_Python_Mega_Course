# For Loop Over a Function

A for loop can also be used to execute a function multiple times. For example, below we are executing celsius_to_kelvin three times since there are three items in the iterating list:

> def celsius_to_kelvin(cels):
>     return cels + 273.15
>  
> for temperature in [9.1, 8.8, -270.15]:
>     print(celsius_to_kelvin(temperature))


The output of that would be:

> 282.25
> 281.95
> 3.0

So, in the first iteration celsius_to_kelvin(9.1) was executed, in the second celsius_to_kelvin(8.8) and in the third celsius_to_kelvin(-270.15).

# Dictionary Loop and String Formatting

Here is an example that combines a dictionary loop with string formatting. The loop iterates over the dictionary and it generates and prints out a string in each iteration:



> phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
>  
> for pair in phone_numbers.items():
>     print(f"{pair[0]} has as phone number {pair[1]}")


And here is a better way to achieve the same results by iterating over keys and values:

> phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
>  
> for key, value in phone_numbers.items():
>     print(f"{key} has as phone number {value}")


In both cases, the output is:

John has as phone number +37682929928

Marry has as phone number +423998200919

# Cheatsheet: Loops

In this section, you learned the following:

A for-loop is useful to repeatedly execute a block of code.

You can create a for-loop like so:

> for letter in 'abc':
>     print(letter.upper())
> Output:

> A
> B
> C

As you can see, the for-loop repeatedly converted all the items of 'abc' to uppercase.

The name after for (e.g. letter) is just a variable name



You can loop over dictionary keys as follows:

> phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
> for value in phone_numbers.keys():
>     print(value)

Output:

> John Smith
> Marry Simpsons

You can loop over dictionary values:

> phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
> for value in phone_numbers.values():
>     print(value)

Output:

> +37682929928
> +423998200919



You can loop over dictionary items:

> phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
> for key, value in phone_numbers.items():
>     print(key, value)

Output: 

> John Smith +37682929928
> Marry Simpons +423998200919


We also have while-loops. The code under a while-loop will run as long as the while-loop condition is true:

> while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
>     print("It's not yet 19:30:20 of 2090.8.20")

The loop above will print out the string inside print() over and over again until the 20th of August, 2090.