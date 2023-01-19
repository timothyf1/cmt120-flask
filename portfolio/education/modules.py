from flask import abort, redirect, render_template, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required

from .. import db
from ..models import Course, Module

from .breadcrumbs import *
from .education import bp_education
from .form import Edit_Module, Delete


@bp_education.route("/modules")
@register_breadcrumb(bp_education, '.modules', 'Modules')
def module_list():
    modules = Module.query.order_by(Module.year.desc()).all()
    return render_template('modules/module-list.html',title='Modules', modules=modules)


@bp_education.route("/module/<string:code>")
@register_breadcrumb(bp_education, '.module', '', dynamic_list_constructor=module_breadcrumb)
def module_page(code):
    module = Module.query.filter_by(code=code).first()
    if module:
        return render_template('modules/module-topics.html', title=f'{module.code} - {module.name}', module=module)
    abort(404, description=f"Module code '{code}' does not exists. Please go to <a href='{url_for('bp_education.module_list')}'>module list</a> to view available modules.")


@bp_education.route("/course/<string:name>/new-module", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.course.new-mod', '', dynamic_list_constructor=module_new_breadcrumb)
@login_required
def new_module(name):
    course = Course.query.filter_by(name=name).first_or_404()
    form = Edit_Module()

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
        return redirect(url_for('bp_education.module_page', code=module.code))

    return render_template('modules/edit-module.html', title='Add a module', form=form, course=course, new=True)


@bp_education.route("/module/<string:code>/edit-module", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.module.edit', 'Edit Module', dynamic_list_constructor=module_edit_breadcrumb)
@login_required
def edit_module(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = Edit_Module()

    if form.validate_on_submit():
        # Updating DB
        module.name = form.name.data,
        module.code = form.code.data,
        module.year = form.year.data,
        module.description = form.description.data,
        db.session.commit()
        return redirect(url_for('bp_education.module_page', code=module.code))

    if request.method == 'GET':
        form.name.data = module.name
        form.code.data = module.code
        form.current_code.data = module.code
        form.year.data = module.year
        form.description.data = module.description

    return render_template('modules/edit-module.html', title='Add a module', form=form, module=module)


@bp_education.route("/module/<string:code>/delete", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.module.delete', 'Delete Module', dynamic_list_constructor=module_delete_breadcrumb)
@login_required
def delete_module(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = Delete()

    if form.validate_on_submit():
        db.session.delete(module)
        db.session.commit()
        return redirect(url_for('bp_education.module_list'))

    return render_template('delete.html', title='Delete a module', form=form, module=module)
