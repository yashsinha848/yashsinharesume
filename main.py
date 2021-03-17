from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy


local_server = True
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template('index2.html')
'''
@app.route("/about")
def about():
    return render_template('index.html')

@app.route("/experience")
def experience():
    return render_template('index.html',scrollToAnchor="skills")
'''
app.run(debug=True)