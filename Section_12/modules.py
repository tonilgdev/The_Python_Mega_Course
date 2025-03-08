# Bultin Modules (https://docs.python.org/3/library/time.html)
"""
import time as t

while True:
    with open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/fruits.txt") as my_file:
        print(my_file.read())
        t.sleep(3)
"""
"""
import sys
sys.builtin_module_names
"""

# Standard Python Modules (https://docs.python.org/3/library/os.html)

"""
import os
sys.prefix
"""

"""
import time as t #Written in C
import os # Wriotten in python

while True:
    if os.path.exists("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/fruits.txt"):
        with open("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_11/fruits.txt") as my_file:
            print(my_file.read())
    else:
        print("File does not exixst.")
    
    t.sleep(3)

"""

# Third-Party modules (https://pandas.pydata.org/docs/) (Example)

# python -m pip install pip
# python -m pip --version
# python -m pip install pandas

import time as t
import os
import pandas as pd

while True:
    if os.path.exists("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_12/temps_today.csv"):
        data = pd.read_csv("C:/Users/Toni/Desktop/Programming/The_Python_Mega_Course/Section_12/temps_today.csv")
        print(data.mean())
    else:
        print("File does not exixst.")
    
    t.sleep(3)