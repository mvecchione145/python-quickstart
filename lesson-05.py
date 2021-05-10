# --STEP LIST--
# 1. Run this script.
#     In your command line terminal window execute the following line:
#     python lesson-05.py

# 2. In a browser window go to the path http://127.0.0.1:5000/:
#     You should see some text that says "HELLO WORLD!"

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# The results should look like this:
#  * Serving Flask app "lesson-05" (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: {some pin number}

from flask import Flask
# flask has many functions and object for utilizing the flask structure but "Flask" is what is used to create the app.


app = Flask(__name__)
# setting name of app object == __name__ of file


# "@" denotes a function decorator
# original function -> decorator => new function
# decorator takes in a function runs something with context to the function and returns a new function

# for more on decorators look up lesson 7

@app.route('/')
def main():
    return "HELLO WORLD!"

# lines 15-17 compiles to >> on our application server when we get a request to http://127.0.0.1:5000/ return the text
# "HELLO WORLD!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # this will start our server and it will not stop running until YOU press CTRL+C to quit
