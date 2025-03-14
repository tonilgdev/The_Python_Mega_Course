# Installing OpenCV (https://opencv.org/)

In the next lecture, and in Section 17, we will use the OpenCV image processing library. Let us first make sure you have installed the OpenCV library. OpenCV is also referred to as cv2 in Python.



##How to Install OpenCV
To install OpenCV for Python 3.9 on Mac or Linux, execute the following in the terminal:

> python3.9 -m pip install opencv-python

To install OpenCV for Python 3.9 on Windows, execute the following in the terminal:

> python -m pip install opencv-python

Note: The above commands work for Python 3.9. You may need to replace the 3.9 part from the commands with the number of the Python version you are using in your system. For example, you may need to type python3.10 instead of python3.9.

Once the installation completes, open a Python session and try:

> import cv2 

If you get no errors, you installed OpenCV successfully. If you get an error, see the FAQs below:



FAQs

### 1. My OpenCV installation didn't work on Windows

Solution:

1. Uninstall OpenCV with:

> python -m pip uninstall opencv-python

2. Download a wheel (.whl) file from this link and install the file with pip. Make sure you download the correct file for your Windows and your Python versions. For example, for Python 3.6 on Windows 64-bit, you would do this:

> python -m pip install opencv_python‑3.2.0‑cp39‑cp39m‑win_amd64.whl 

3. Try to import cv2 in Python again. If there's still an error, type the following again in the command line:

>python -m pip install opencv-python

4. Try importing cv2 again. It should work at this point.



### 2. My OpenCV installation didn't work on Mac

Solution:

If python3.9 -m pip install opencv-python here are alternative steps to install OpenCV:

1. Install brew.

To install brew, open your terminal, and execute the following:

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. OpenCV depends on GTK+, so install that dependency first with brew (always from the terminal):

brew install gtk+ 

3. Install OpenCV with brew:

brew install opencv 

4. Open Python and try to import OpenCV with:

import cv2 

If you get no errors, you installed OpenCV successfully.



### 3. My OpenCV installation didn't work on Linux

1. Open your terminal and execute the following commands, one by one:

> sudo apt-get install libqt4-dev
> cmake -D WITH_QT=ON ..
> make
> sudo make install
2. If the above commands don't work, execute this:

> sudo apt-get install libopencv-*
3. Then, install OpenCV with pip:

> python3.9 -m pip install opencv-python 

4. Import cv2 in Python. If you get no errors, you installed OpenCV successfully.