from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required
from flask_breadcrumbs import register_breadcrumb

from .. import db, app
from ..models import Course, Module

from .form import New_Course, Edit_Course, Delete_Course

bp_education = Blueprint('bp_education', __name__, template_folder='templates')

def course_list_breadcrumb(*args, **kwargs):
    return [{'text': 'Courses', 'url': url_for("bp_education.course_list")}]

@bp_education.route("/")
@register_breadcrumb(app, '.course_list', 'Courses', dynamic_list_constructor=course_list_breadcrumb)
def course_list():
    courses = Course.query.all()
    return render_template('course-list.html',title='Education', courses=courses)

def course_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    print(url_for("bp_education.course_page", name=course_name))
    return [{'text': course_name, 'url': url_for("bp_education.course_page", name=course_name)}]

@bp_education.route("/<string:name>")
@register_breadcrumb(app, '.course', '', dynamic_list_constructor=course_breadcrumb)
def course_page(name):
    course = Course.query.filter_by(name=name).first_or_404()
    return render_template('course-modules.html', title=name, course=course)

def course_new_breadcrumb(*args, **kwargs):
    return [{'text': 'New Course', 'url': url_for("bp_education.new_course")}]

@bp_education.route("/new-course", methods=['GET', 'POST'])
@register_breadcrumb(app, '.courses', 'New Course', dynamic_list_constructor=course_new_breadcrumb)
@login_required
def new_course():
    form = New_Course()
    if form.validate_on_submit():
        course = Course(
            name = form.name.data,
            location = form.location.data,
            year = int(form.year.data),
            description = form.description.data
            )
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('bp_education.course_page', name=course.name))

    return render_template('new-course.html', title='Add a course', form=form)

def course_edit_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    return [{'text': 'Edit', 'url': url_for("bp_education.edit_course", name=course_name)}]

@bp_education.route("/<string:name>/edit", methods=['GET', 'POST'])
@register_breadcrumb(app, '.course.edit', 'Edit Course', dynamic_list_constructor=course_edit_breadcrumb)
@login_required
def edit_course(name):
    course = Course.query.filter_by(name=name).first_or_404()
    form = Edit_Course()

    if form.validate_on_submit():
        course.name = form.name.data
        course.location = form.location.data
        course.year = form.year.data
        course.description = form.description.data
        db.session.commit()
        return redirect(url_for('bp_education.course_page', name=course.name))

    form.name.data = course.name
    form.location.data = course.location
    form.year.data = course.year
    form.description.data = course.description
    return render_template('edit-course.html', title='Edit a course', form=form, course=course)

def course_delete_breadcrumb(*args, **kwargs):
    course_name = request.view_args['name']
    return [{'text': 'Delete Course', 'url': url_for("bp_education.delete_course", name=course_name)}]

@bp_education.route("/<string:name>/delete", methods=['GET', 'POST'])
@register_breadcrumb(app, '.course.delete', 'Delete Course', dynamic_list_constructor=course_delete_breadcrumb)
@login_required
def delete_course(name):
    course = Course.query.filter_by(name=name).first_or_404()
    form = Delete_Course()
    if form.validate_on_submit():
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('bp_education.course_list'))

    return render_template('delete-course.html', title='Edit a course', form=form, course=course)
