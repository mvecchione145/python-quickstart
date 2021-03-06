# --STEP LIST--
# 1. Run this script AS IS (error is expected: "ModuleNotFoundError: No module named 'pandas'")
#     In your command line terminal window execute the following line:
#     python lesson-02.py

# 2. Install the requirements file into your virtual environment.
#     In your command line terminal window execute the following line:
#     pip install -r requirements.txt

# 3. Retry executing this script
#     In your command line terminal window execute the following line:
#     python lesson-02.py

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# The results should look like this:
#    ID           FullName         DOB
# 0   1   Thomas Jefferson   4/13/1743
# 1   2  George Washington   2/22/1732
# 2   3       Ben Franklin   1/17/1706
# 3   4         John Adams  10/30/1735


import pandas
# import the pandas library

file_path = "exercise_files/example.xlsx"
# relative path of example excel file

df = pandas.read_excel(file_path)
# loading the excel file into a pandas.DataFrame

print(df)
# printing the pandas.DataFrame
