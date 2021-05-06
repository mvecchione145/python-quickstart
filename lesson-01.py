## If you would like to use an outside library you would need to
## pip install in the command line to first save it to your virtual
## environment.
#
# > pip install {library_name}
#
## Once the library is saved in your projects virtual environment
## you can call it at the top of your script through an import line.

import pandas
# pandas is a tabular data


file_path = ""
df = pandas.read_excel(file_path)
print(df)
