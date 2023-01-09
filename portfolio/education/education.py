import markdown
import bleach

from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required
from .. import db
from ..models import Course, Module, Post

from .form import *

bp_education = Blueprint('bp_education', __name__, template_folder='templates', static_folder='static')
allowed_tags = ['a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li',
                'code', 'strong', 'blockquote', 'em']

@bp_education.route("/")
def course_list():
    courses = Course.query.all()
    return render_template('courses/course-list.html',title='Education', courses=courses)

@bp_education.route("/course/<string:name>")
def course_page(name):
    course = Course.query.filter_by(name=name).first_or_404()
    return render_template('courses/course-modules.html', title=name, course=course)

@bp_education.route("/course/new-course", methods=['GET', 'POST'])
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
@login_required
def delete_course(name):
    course = Course.query.filter_by(name=name).first_or_404()
    form = Delete_Course()
    if form.validate_on_submit():
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('bp_education.course_list'))

    return render_template('courses/delete-course.html', title='Edit a course', form=form, course=course)

@bp_education.route("/modules")
def module_list():
    modules = Module.query.all()
    return render_template('modules/module-list.html',title='Modules', modules=modules)

@bp_education.route("/module/<string:code>")
def module_page(code):
    module = Module.query.filter_by(code=code).first_or_404()
    return render_template('modules/module-posts.html', title='module.name', module=module)

@bp_education.route("/course/<string:course>/new-module", methods=['GET', 'POST'])
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
        return redirect(url_for('bp_education.module_page', code=module.code))
    return render_template('modules/new-module.html', title='Add a module', form=form, course=course)

@bp_education.route("/module/<string:code>/edit-module", methods=['GET', 'POST'])
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
        return redirect(url_for('bp_education.module_page', code=module.code))

    form.name.data = module.name
    form.code.data = module.code
    form.year.data = module.year
    form.description.data = module.description

    return render_template('modules/edit-module.html', title='Add a module', form=form, module=module)

@bp_education.route("/module/<string:code>/delete", methods=['GET', 'POST'])
@login_required
def delete_module(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = Delete_Module()
    if form.validate_on_submit():
        db.session.delete(module)
        db.session.commit()
        return redirect(url_for('bp_education.module_list'))

    return render_template('modules/delete-module.html', title='Delete a module', form=form, module=module)

@bp_education.route("/topics")
def posts_list():
    posts = Post.query.all()
    return render_template('topics/topic-list.html',title='Topics', posts=posts)

@bp_education.route("/topic/<string:title>")
def view_post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    content = bleach.clean(markdown.markdown(post.content), tags=allowed_tags)
    return render_template('topics/topic-view.html', title=post.title, post=post, content=content)

@bp_education.route("/module/<string:module_code>/new-post", methods=['GET', 'POST'])
@login_required
def new_post(module_code):
    module = Module.query.filter_by(code=module_code).first_or_404()
    form = New_post()

    if form.validate_on_submit():
        check_title = Post.query.filter_by(title=form.title.data).first()
        if check_title is None:
            post = Post(
                title = form.title.data,
                content = form.content.data,
                author_id = current_user.id,
                module = module
            )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('bp_education.view_post', title=post.title))
        form.title.errors = ["This title has been used, please enter a different title"]
    return render_template('topics/new-topic.html', title='New topic', form=form, module=module)

@bp_education.route("/topic/<string:title>/edit", methods=['GET', 'POST'])
@login_required
def edit_post(title):
    post = Post.query.filter_by(title=title).first_or_404()

    form = Edit_post()

    if form.validate_on_submit():
        if post.title != form.title.data:
            check_title = Post.query.filter_by(title=form.title.data).first()
        else:
            check_title = None
        if check_title is None:
            post.title = form.title.data
            post.content = form.content.data
            db.session.commit()
            return redirect(url_for('bp_education.view_post', title=post.title))
        form.title.errors = ["This title has been used, please enter a different title"]
    else:
        form.title.data = post.title
        form.content.data = post.content

    return render_template('topics/edit-topic.html', title='Edit topic', form=form, post=post)

@bp_education.route("/topic/<string:title>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    form = Delete_Post()
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('bp_education.posts_list'))

    return render_template('topics/delete-topic.html', title='Delete topic', form=form, post=post)

@bp_education.route("/topics/preview", methods=['POST'])
@bp_education.route("/topic/<string:title>/preview", methods=['POST'])
def preview(title):
    mkd = request.json['markdown']
    title = f"<h1>{request.json['title']}</h1>"
    html = title + bleach.clean(markdown.markdown(mkd), tags=allowed_tags)
    return {"html": html}
