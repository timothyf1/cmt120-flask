from flask import render_template, url_for
from portfolio import app

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html',title='Home')
