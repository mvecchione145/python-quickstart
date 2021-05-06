# If you would like to use an outside library you would need to
# pip install in the command line to first save it to your virtual
# environment.

# > pip install {library_name}

# Once the library is saved in your projects virtual environment
# you can call it at the top of your script through an import line.

import pandas
# import the pandas library


file_path = "example.xlsx"
# relative path of example excel file

df = pandas.read_excel(file_path)
# creating a dataframe from excel file

print(df)
# printing the dataframe
