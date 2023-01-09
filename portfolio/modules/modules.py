from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required
from flask_breadcrumbs import register_breadcrumb

from .. import db, app
from ..models import Course, Module, Post

from .forms import New_Module, Edit_Module, Delete_Module

bp_modules = Blueprint('bp_modules', __name__, template_folder='templates')

@bp_modules.route("/")
@register_breadcrumb(bp_modules, '.', 'Modules')
def module_list():
    modules = Module.query.all()
    return render_template('module-list.html',title='Modules', modules=modules)

def module_breadcrumb(*args, **kwargs):
    try:
        module_code = request.view_args['code']
        module = Module.query.filter_by(code=module_code).first()
        return [{'text': module.course.name, 'url': url_for("bp_education.course_page", name=module.course.name)},
                {'text': module.code, 'url': url_for("bp_modules.module_page", code=module.code)}]
    except:
        return []

@bp_modules.route("/<string:code>")
@register_breadcrumb(app, '.module', '', dynamic_list_constructor=module_breadcrumb)
def module_page(code):
    module = Module.query.filter_by(code=code).first_or_404()
    return render_template('module-posts.html', title='module.name', module=module)

@bp_modules.route("/<string:course>/new-module", methods=['GET', 'POST'])
@login_required
def new_module(course):
    course = Course.query.filter_by(name=course).first_or_404()
    form = New_Module()
    if form.validate_on_submit():
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
    return render_template('new-module.html', title='Add a module', form=form, course=course)

@bp_modules.route("/<string:code>/edit-module", methods=['GET', 'POST'])
@login_required
def edit_module(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = Edit_Module()
    if form.validate_on_submit():
        module.name = form.name.data,
        module.code = form.code.data,
        module.year = form.year.data,
        module.description = form.description.data,

        db.session.commit()
        return redirect(url_for('bp_modules.module_page', code=module.code))

    form.name.data = module.name
    form.code.data = module.code
    form.year.data = module.year
    form.description.data = module.description

    return render_template('edit-module.html', title='Add a module', form=form, module=module)

@bp_modules.route("/<string:code>/delete", methods=['GET', 'POST'])
@login_required
def delete_module(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = Delete_Module()
    if form.validate_on_submit():
        db.session.delete(module)
        db.session.commit()
        return redirect(url_for('bp_modules.module_list'))

    return render_template('delete-module.html', title='Delete a module', form=form, module=module)
