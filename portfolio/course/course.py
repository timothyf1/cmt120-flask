from flask import Blueprint, render_template, url_for
from portfolio.models import Course, Module

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
