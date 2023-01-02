from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required
from .. import db
from ..models import Course, Module

from .form import New_Course

bp_education = Blueprint('bp_education', __name__, template_folder='templates')

@bp_education.route("/education")
def course_list():
    courses = Course.query.all()
    return render_template('course-list.html',title='Education', courses=courses)

@bp_education.route("/course/<string:name>")
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