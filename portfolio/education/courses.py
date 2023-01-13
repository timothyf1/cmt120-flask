from flask import redirect, render_template, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required

from .. import db
from ..models import Course

from .breadcrumbs import *
from .education import bp_education
from .form import New_Course, Edit_Course, Delete_Course

@bp_education.route("/courses")
@register_breadcrumb(bp_education, '.', 'Education')
def course_list():
    courses = Course.query.order_by(Course.year.desc()).all()
    return render_template('courses/course-list.html',title='Education', courses=courses)

@bp_education.route("/course/<string:name>")
@register_breadcrumb(bp_education, '.course', '', dynamic_list_constructor=course_breadcrumb)
def course_page(name):
    course = Course.query.filter_by(name=name).first()
    if course:
        return render_template('courses/course-modules.html', title=name, course=course)
    abort(404, description=f"Course {name} does not exists. Please go to <a href='{url_for('bp_education.course_list')}'>courses list</a> to view available courses.")

@bp_education.route("/course/new-course", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.new', 'New Course')
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

    return render_template('courses/new-course.html', title='Add a course', form=form)

@bp_education.route("/course/<string:name>/edit", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.course.edit', '', dynamic_list_constructor=course_edit_breadcrumb)
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
    return render_template('courses/edit-course.html', title='Edit a course', form=form, course=course)

@bp_education.route("/course/<string:name>/delete", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.course.delete', '', dynamic_list_constructor=course_delete_breadcrumb)
@login_required
def delete_course(name):
    course = Course.query.filter_by(name=name).first_or_404()
    form = Delete_Course()
    if form.validate_on_submit():
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('bp_education.course_list'))

    return render_template('courses/delete-course.html', title='Edit a course', form=form, course=course)
