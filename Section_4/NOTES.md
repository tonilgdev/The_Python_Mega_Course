# Did You Know?
> Python is mainly used for automation purposes, web apps, and data science. Many big companies, like Instagram, Facebook, and Amazon, use Python in different parts of their products. For example, Facebook uses Python to process images.

# Dictionary Reminder
> In the next lecture, you will learn more about dictionaries, so here's an example of a dictionary in case you forgot about them:

> search_engines_users = {"google": 1000000000, "bing": 127000000, "duck duck go":12000000}

> A dictionary is made of pairs of keys and values. For example, the first pair is "google": 1000000000 where "google" is the key and 1000000000 is the value of that key.

> Let's go!

# Tip: Converting Between Datatypes

> Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

- From tuple to list:
> >>> cool_tuple = (1, 2, 3)
> >>> cool_list = list(cool_tuple)
> >>> cool_list
> [1, 2, 3]

- From list to tuple:

> >>> cool_list = [1, 2, 3]
> >>> cool_tuple = tuple(cool_list)
> >>> cool_tuple
> (1, 2, 3)


- From string to list:

> >>> cool_string = "Hello"
> >>> cool_list = list(cool_string)
> >>> cool_list
> ['H', 'e', 'l', 'l', 'o']


- From list to string:

> >>> cool_list = ['H', 'e', 'l', 'l', 'o']
> >>> cool_string = str.join("", cool_list)
> >>> cool_string
> 'Hello'

> As can be seen above, converting a list into a string is more complex. Here str() is not sufficient. We need str.join(). Try running the code above again, but this time using str.join("---", cool_list) in the second line. You will understand how str.join() works.

# Cheatsheet: Operations with Data Types

In this section, you learned that:



- Lists, strings, and tuples have a positive index system:

> ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
>    0      1      2      3      4      5      6


- And they have a negative index system as well:

> ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
>   -7     -6     -5     -4     -3     -2     -1


- In a list, the 2nd, 3rd, and 4th items can be accessed with:

> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
> days[1:4]
> Output: ['Tue', 'Wed', 'Thu']


- First three items of a list:

> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
> days[:3]
> Output:['Mon', 'Tue', 'Wed'] 


- Last three items of a list:

> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
> days[-3:]
> Output: ['Fri', 'Sat', 'Sun']

- Everything but the last:

> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
> days[:-1] 
> Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

- Everything but the last two:

> days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
> days[:-2] 
> Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 


- A dictionary value can be accessed using its corresponding dictionary key:

> phone_numbers = {"John":"+37682929928","Marry":"+423998200919"}
> phone_numbers["Marry"]
> Output: '+423998200919'