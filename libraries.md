# Python Libraries

Libraries are portable code that can be
[Built-In](https://github.com/mvecchione145/python-quickstart/blob/main/libraries.md#built-in-libraries) (come
pre-installed with your virtual environment) or installed via
[pip](https://github.com/mvecchione145/python-quickstart/blob/main/libraries.md##pip).


## pip

Pip is a versatile, command line tool, that comes with python, used for utilizing libraries. Pip allows you to import
3rd party libraries into your virtual environment, you can also export a requirements file based on the libraries that
have already been installed.

### Installing a single library

```
pip install pandas
```

Running the above code in your command line terminal will install [pandas](https://pandas.pydata.org/) as well as all
other dependencies of pandas.

### Installing a list of libraries from file

```
pip install -r requirements.txt
```

Running the above code in your command line terminal will install ALL libraries (at the versions) that exist in your
[requirements](https://github.com/mvecchione145/python-quickstart/blob/main/requirements.txt) file.

**PLEASE NOTE**

Calling the ```-r requirements.txt``` is assuming you are running the terminal FROM your project base AND the
requirements file exists in the project base. If you would like to put your requirements file in folder you would have
to make sure you specify that folder ```-r folder/requirements.txt```

### Exporting a requirements file

```
pip freeze > requirements.txt
```

Running the above code in your command line terminal will create a file with all libraries previously installed followed
by the version.

*FOR EXAMPLE*
> pandas==1.2.4

## Built-In Libraries

[SEE HERE FOR MORE](https://docs.python.org/3/library/)

When you create your [virtual environment]() you are creating a folder structure for python's built-in functions and
libraries as well as a python compiler. Built-In functions include ```print()``` and ```import``` which don't require
importing, while built-in libraries require each python script you write to import them before use.
