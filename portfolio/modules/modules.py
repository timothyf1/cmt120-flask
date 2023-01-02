from flask import Blueprint, render_template, url_for
from ..models import Module, Post

bp_modules = Blueprint('bp_modules', __name__, template_folder='templates')

@bp_modules.route("/")
def module_list():
    modules = Module.query.all()
    return render_template('module-list.html',title='Modules', modules=modules)

@bp_modules.route("/<string:code>")
def module_page(code):
    module = Module.query.filter_by(code=code).first_or_404()
    return render_template('module-posts.html', title='module.name', module=module)
