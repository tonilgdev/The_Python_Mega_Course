# The "pandas" Data Analysis Library

# Moddule tha helps as to open and manage dataframes, Json, Csv and excel files.

# Getting Started with pandas (https://pandas.pydata.org/docs/)

import pandas as pd

df1 = pd.DataFrame([[2,4,6],[10,20,30]])

print(df1)

df2 = pd.DataFrame([[2,4,6],[10,20,30]], columns = ["Price","Age","Value"])

print(df2)

df3 = pd.DataFrame([[2,4,6],[10,20,30]], columns = ["Price","Age","Value"], index = ["First", "Second"])

print(df3)

df4 = pd.DataFrame([{"Name":"John"},{"Name":"Jack"}])

print(df4)

print(type(df1))

# Getting Started with Jupyter (https://jupyter-notebook.readthedocs.io/en/stable/)

""" 
First, please check notes.md
Second, please check testing_jupyter.ipynb
"""

# Loading CSV, Excel Files and Plain Text file (Download supermarkets.zip)

"""
First, please check notes.md
Second, please check loading_files.ipynb 
"""