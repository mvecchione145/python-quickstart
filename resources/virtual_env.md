# Virtual Environment

Starting a project in Pycharm will automatically build a python virtual environment contained within the "venv" folder.
If you plan on working on a project outside of Pycharm you will need to understand [how to set up a virtual environment
in command line terminal](
https://github.com/mvecchione145/python-quickstart/blob/main/resources/virtual_env.md#create-venv-in-command-line).

[MORE ON virtual environment](https://docs.python.org/3/tutorial/venv.html)

## Components of venv

- /bin: files that interact with the virtual environment
- /include: C headers that compile the Python packages
- /lib: a copy of the Python version along with a site-packages folder where each dependency is installed

## Create venv in command line
### Install venv

```
pip install virtualenv
```

Virtualenv must be installed before using.

### Build venv

```
virtualenv venv
```

There are optional parameters involved in creating a virtual environment but the code above is the minimum required to
successfully create a virtual environment. "venv" can be named anything but that is the proper convention.
