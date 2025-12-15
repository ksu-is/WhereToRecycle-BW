# import Flask and other modules
from flask import Flask, render_template, request

# create a Flask application instance
app = Flask(__name__)

# create a route for the home page
@app.route('/')
def home():  
    return render_template("WhereToRecycle.html")

# run the application
if __name__=="__main__":
    app.run(debug=True)
    