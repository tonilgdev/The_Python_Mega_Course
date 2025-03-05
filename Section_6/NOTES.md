# More String Formatting

There is also another way to format strings using the "{}".format(variable) form. Here is an example:

> name = "John"
> surname = "Smith"
>  
> message = "Your name is {}. Your surname is {}".format(name, surname)
> print(message)

Output: Your name is John. Your surname is Smith

# Cheatsheet: Processing User Input
In this section, you learned that:

A Python program can get user input via the input function:

The input function halts the execution of the program and gets text input from the user:

> name = input("Enter your name: ")


The input function converts any input to a string, but you can convert it back to int or float:

> experience_months = input("Enter your experience in months: ")
> experience_years = int(experience_months) / 12


You can also format strings with:

> name = "Sim"
> experience_years = 1.5
> print("Hi {}, you have {} years of experience".format(name, experience_years))

Output: Hi Sim, you have 1.5 years of experience.