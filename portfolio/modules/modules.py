from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required
from .. import db
from ..models import Course, Module, Post

from .forms import New_Module

bp_modules = Blueprint('bp_modules', __name__, template_folder='templates')

@bp_modules.route("/")
def module_list():
    modules = Module.query.all()
    return render_template('module-list.html',title='Modules', modules=modules)

@bp_modules.route("/<string:code>")
def module_page(code):
    module = Module.query.filter_by(code=code).first_or_404()
    return render_template('module-posts.html', title='module.name', module=module)

@bp_modules.route("/new-module/<int:course_id>", methods=['GET', 'POST'])
@login_required
def new_module(course_id):
    form = New_Module()
    if form.validate_on_submit():
        course = Course.query.filter_by(id=course_id).first_or_404()
        module = Module(
            name = form.name.data,
            code = form.code.data,
            year = form.year.data,
            description = form.description.data,
            course_id = course.id,
            course = course
        )
        db.session.add(module)
        db.session.commit()
        return redirect(url_for('bp_modules.module_page', code=module.code))
    return render_template('new-module.html', title='Add a module', form=form)
