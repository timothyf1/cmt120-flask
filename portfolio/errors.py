from markupsafe import Markup
from flask import render_template
from portfolio import app

@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', title="400", error=error), 400

@app.errorhandler(401)
def bad_request(error):
    return render_template('errors/401.html', title="400", error=error), 401

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title="404", error=Markup(error)), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/405.html', title="405", error=error), 405
