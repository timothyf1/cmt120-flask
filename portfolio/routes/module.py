from flask import render_template, url_for
from portfolio import app
from portfolio.models import Module

@app.route("/module")
def module():
    modules = Module.query.all()
    return render_template('module-list.html',title='Modules', modules=modules)