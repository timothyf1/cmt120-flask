from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required
from .. import db
from ..models import Course, Module

from .form import New_Course, Edit_Course, Delete_Course

bp_education = Blueprint('bp_education', __name__, template_folder='templates')

@bp_education.route("/")
def course_list():
    courses = Course.query.all()
    return render_template('course-list.html',title='Education', courses=courses)

@bp_education.route("/<string:name>")
def course_page(name):
    course = Course.query.filter_by(name=name).first_or_404()
    # print(module.id)
    modules = Module.query.filter_by(course_id=course.id)
    return render_template('course-modules.html', title=name, course=course, modules=modules)

@bp_education.route("/new-course", methods=['GET', 'POST'])
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

@bp_education.route("/<string:name>/edit", methods=['GET', 'POST'])
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

@bp_education.route("/<string:name>/delete", methods=['GET', 'POST'])
@login_required
def delete_course(name):
    course = Course.query.filter_by(name=name).first_or_404()
    form = Delete_Course()
    if form.validate_on_submit():
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('bp_education.course_list'))

    return render_template('delete-course.html', title='Edit a course', form=form, course=course)
