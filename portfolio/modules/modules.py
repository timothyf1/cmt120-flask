from flask import Blueprint, render_template, url_for
from portfolio.models import Module, Post

bp_modules = Blueprint('bp_modules', __name__, template_folder='templates')

@bp_modules.route("/module")
def module_list():
    modules = Module.query.all()
    return render_template('module-list.html',title='Modules', modules=modules)

@bp_modules.route("/module/<string:name>")
def module_page(name):
    module = Module.query.filter_by(name=name).first_or_404()
    print(module.id)
    posts = Post.query.filter_by(module_id=module.id)
    return render_template('module-posts.html', title='name', module=module, posts=posts)
