from flask import Flask, render_template
import mentions

app = Flask(__name__)

results = [] 

@app.route('/')
def index(): 
    results = mentions.getCoins() # grab data from reddit API 
    return render_template("index.jinja2", entries=results) # format into index.html 

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/contact')
def contact(): 
    return render_template("contact.html")
