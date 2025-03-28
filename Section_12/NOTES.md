# Cheatsheet: Imported Modules

In this section, you learned that:

Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

> import time
> time.sleep(5)
A list of all builtin modules can be printed out with:

> import sys
> sys.builtin_module_names
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

> pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:

> pip3 install pandas or use python3 -m pip install pandas if that doesn't work.