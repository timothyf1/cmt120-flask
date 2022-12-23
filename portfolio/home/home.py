from flask import Blueprint, render_template

bp_home = Blueprint('bp_home', __name__, template_folder='templates')

@bp_home.route("/")
def home():
    return render_template('home.html',title='Home')
