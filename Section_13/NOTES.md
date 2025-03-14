# Installing pandas

Please make sure you have pandas installed. You can install it with pip from your computer or Atom/VS Code terminal/cmd just like you have installed other third-party packages. Please execute one of the commands below to do the installation depending on what version of Python you are using:

> pip3.10 install pandas

or

> python -m pip install pandas

etc.

Also, in the next lecture, we will use an enhanced Python interactive shell called IPython.

IPython is just like the standard shell you get when you run Python, but IPython provides better printing for large text. This ability makes IPython suitable for data analysis because the program prints data in a well-structured format. You can install IPython with pip:

> pip3.10 install ipython

or

> python -m pip install ipython

# Installing Jupyter

In the next videos, we will use Jupyter Notebook is a third-party library. Please install Jupyter Notebook by executing one of the commands below:

Installing Jupyter

> pip3.10 install jupyter

or

> python -m pip install jupyter


Please change the number after pip to reflect the version of Python you are using.

## Starting Jupyter

After a successful installation you can start Jupyter Notebook by running the command below from your terminal:

> jupyter notebook

If the above command does not work try the following command:

> python -m jupyter notebook (for Windows users)

> python3.9 -m jupyter notebook  (for Mac and Linux users)

If it works, you will see Jupyter Notebook opened up in your default internet browser.

Jupyter in the cloud

If you do not want to install Jupyter or you cannot install it, you can use Jupyter in the cloud. Google offers a ready-to-use Jupyter notebook here: https://colab.research.google.com/#create=true


# Note on Loading Excel Files

In the next lecture, you will learn how to load Excel files in Python with pandas. For this, you need pandas (which you have already installed) and also two other dependencies that pandas needs for opening Excel files. You can install them with pip:

> python -m pip install openpyxl (needed to load Excel .xlsx files)

> python -m pip install xlrd (needed to load Excel old .xls files)

# Note
We are going to use Nominatim() in the next video. Nominatim() currently has a bug. To fix this problem, whenever you see these lines in the next video:

> rom geopy.geocoders import Nominatim
> om = Nominatim()
change them to these

> from geopy.geocoders import ArcGIS
> nom = ArcGIS()
The rest of the code remains the same.