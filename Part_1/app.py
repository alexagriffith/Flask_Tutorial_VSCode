from flask import Flask
from datetime import datetime
from flask import render_template
import re

app = Flask(__name__)

# Home function
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

"""
The first exercise in the Flask Tutorial
@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

#flask part is only concerned with data values, while the html contains the markup and formatting 

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")"""