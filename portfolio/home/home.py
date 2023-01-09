from flask import Blueprint, render_template
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

bp_home = Blueprint('bp_home', __name__, template_folder='templates')

@bp_home.route("/")
@register_breadcrumb(bp_home, '.', 'Home')
def home():
    return render_template('home.html',title='Home')
