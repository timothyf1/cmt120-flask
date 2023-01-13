import os
import markdown
import bleach
from datetime import datetime

from flask import Blueprint, render_template, url_for, redirect, request, abort
from flask_login import login_required, current_user
from flask_breadcrumbs import register_breadcrumb
from werkzeug.utils import secure_filename

from .. import db, app
from ..models import Course, Module, Topic, Tag, ImageUpload
from .form import *
from.breadcrumbs import *

bp_education = Blueprint('bp_education', __name__, template_folder='templates', static_folder='static')

allowed_tags = ['a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li',
                'code', 'strong', 'blockquote', 'em', 'img']
allowed_attributes = {'a': ['href', 'title'],
                      'abbr': ['title'],
                      'acronym': ['title'],
                      'img': ['alt', 'src']}
allowed_img_extensions = ['.png', '.jpg', '.jpeg', '.gif']

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
@register_breadcrumb(bp_education, '.module.edit', 'Edit Module', dynamic_list_constructor=module_edit_breadcrumb)
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
@register_breadcrumb(bp_education, '.module.delete', 'Delete Module', dynamic_list_constructor=module_delete_breadcrumb)
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
@register_breadcrumb(bp_education, '.topics', 'Topic')
def topics_list():
    topics = Topic.query.order_by(Topic.date).all()
    return render_template('topics/topic-list.html',title='Topics', topics=topics)

@bp_education.route("/topic/<string:title>")
@register_breadcrumb(bp_education, '.topic', '', dynamic_list_constructor=topic_breadcrumb)
def view_topic(title):
    topic = Topic.query.filter_by(title=title).first()
    if topic:
        if topic.draft and not current_user.is_authenticated:
            abort(401)
        content = bleach.clean(markdown.markdown(topic.content), tags=allowed_tags, attributes=allowed_attributes)
        return render_template('topics/topic-view.html', title=topic.title, topic=topic, content=content)
    abort(404, description=f"Topic '{title}' does not exists. Please go to <a href='{url_for('bp_education.topics_list')}'>topics list</a> to view available topics.")


def create_tag_list(tags_string):
    tags = tags_string.lower().split()
    tag_list = []
    for tag in tags:
        tag_db = Tag.query.filter_by(name=tag).first()
        if tag_db:
            tag_list.append(tag_db)
        else:
            tag_db = Tag(name=tag)
            tag_list.append(tag_db)
            db.session.add(tag_db)
    return tag_list

@bp_education.route("/module/<string:code>/new-topic", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.module.new-topic', '', dynamic_list_constructor=topic_new_breadcrumb)
@login_required
def new_topic(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = New_Topic()

    if form.validate_on_submit():
        check_title = Topic.query.filter_by(title=form.title.data).first()
        if check_title is None:
            topic = Topic(
                title = form.title.data,
                content = form.content.data,
                tags = create_tag_list(form.tags.data),
                author_id = current_user.id,
                module = module
            )
            if not form.submit.data:
                topic.draft = True
            db.session.add(topic)
            db.session.commit()
            if form.upload.data:
                print(form.image.data)
                save_image(form.image.data, topic.id)
                return redirect(url_for('bp_education.edit_topic', title=topic.title))
            return redirect(url_for('bp_education.view_topic', title=topic.title))
        form.title.errors = ["This title has been used, please enter a different title"]
    return render_template('topics/new-topic.html', title='New topic', form=form, module=module)

@bp_education.route("/topic/<string:title>/edit", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.topic.edit', '', dynamic_list_constructor=topic_edit_breadcrumb)
@login_required
def edit_topic(title):
    topic = Topic.query.filter_by(title=title).first_or_404()
    images = ImageUpload.query.filter_by(topic_id=topic.id)
    print(images)
    form = Edit_Topic()

    if form.validate_on_submit():
        if topic.title != form.title.data:
            check_title = Topic.query.filter_by(title=form.title.data).first()
        else:
            check_title = None
        if check_title is None:
            topic.title = form.title.data
            topic.content = form.content.data
            topic.tags = create_tag_list(form.tags.data)
            topic.last_updated = datetime.utcnow()
            if form.draft.data:
                topic.draft = True
            else:
                topic.draft = False
            db.session.commit()
            return redirect(url_for('bp_education.view_topic', title=topic.title))
        form.title.errors = ["This title has been used, please enter a different title"]
    else:
        form.title.data = topic.title
        form.tags.data = " ".join([tag.name for tag in topic.tags])
        form.content.data = topic.content

    return render_template('topics/edit-topic.html', title='Edit topic', form=form, topic=topic, images=images)

@bp_education.route("/topic/<string:title>/delete", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.topic.delete', '', dynamic_list_constructor=topic_delete_breadcrumb)
@login_required
def delete_topic(title):
    topic = Topic.query.filter_by(title=title).first_or_404()
    form = Delete_Topic()
    if form.validate_on_submit():
        db.session.delete(topic)
        db.session.commit()
        return redirect(url_for('bp_education.topics_list'))

    return render_template('topics/delete-topic.html', title='Delete topic', form=form, topic=topic)

@bp_education.route("/module/<string:code>/preview", methods=['POST'])
@bp_education.route("/topic/<string:title>/preview", methods=['POST'])
@login_required
def preview(title=None, code=None):
    mkd = request.json['markdown']
    title = f"<h1>{request.json['title']}</h1>"
    html = title + bleach.clean(markdown.markdown(mkd), tags=allowed_tags, attributes=allowed_attributes)
    return {"html": html}

@bp_education.route("/tags")
@register_breadcrumb(bp_education, '.topics.tags', 'Tags')
def tag_list():
    tags = Tag.query.order_by(Tag.name).all()
    return render_template('tags/tag-list.html', title='Tags', tags=tags)

@bp_education.route("/tag/<string:tag>")
@register_breadcrumb(bp_education, '.topics.tags.tag', '', dynamic_list_constructor=tag_breadcrumb)
def tag_topics(tag):
    tag_a = Tag.query.filter_by(name=tag).first()
    if tag_a:
        return render_template('tags/tag-topics.html', title=f'{tag_a.name} - Tag', tag=tag_a)
    abort(404, description=f"Tag '{tag}' does not exists. Please go to <a href='{url_for('bp_education.tag_list')}'>tags list</a> to view available tags.")

@bp_education.route("/tag/<string:tag>/delete", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.topics.tags.tag.delete', '', dynamic_list_constructor=tag_delete_breadcrumb)
def delete_tag(tag):
    tag = Tag.query.filter_by(name=tag).first_or_404()
    form = Delete_Tag()
    if form.validate_on_submit():
        db.session.delete(tag)
        db.session.commit()
        return redirect(url_for('bp_education.tag_list'))
    return render_template('tags/delete-tag.html', title=f'Delete {tag.name}', form=form, tag=tag)

@bp_education.route("/file-upload", methods=['GET', 'POST'])
@login_required
def file_upload():
    form = Image_Upload()
    if form.validate_on_submit():
        file_up = form.file_up.data
        print(type(file_up))
        print(file_up.__dir__())
        print(file_up.content_type)
        print('image' in file_up.content_type)
        file_up.save(os.path.join(app.config['FILE_UPLOAD'], secure_filename(file_up.filename)))
    return render_template('image-upload.html', form=form)

def save_image(image, topic_id):
    # Check to see if the file is an image
    if 'image' not in image.content_type:
        return {
            "status" : False,
            "message" : "File is not an image, allowed extensions are .png, .jpg, .jpeg and .gif"
        }

    # Check to see if topic directory exists
    if not os.path.exists(os.path.join(app.config['FILE_UPLOAD'], str(topic_id))):
        os.makedirs(os.path.join(app.config['FILE_UPLOAD'], str(topic_id)))

    # Check to see if the filename exists
    if os.path.exists(os.path.join(app.config['FILE_UPLOAD'], str(topic_id), secure_filename(image.filename))):
        return {
            "status" : False,
            "message" : "File name already in use, please check the uploaded images below to see if it has been already uploaded."
        }

    # Save the image
    image.save(os.path.join(app.config['FILE_UPLOAD'], str(topic_id), secure_filename(image.filename)))

    # Add details to the db for the image
    image = ImageUpload(
        user_id = current_user.id,
        topic_id = topic_id,
        filename = secure_filename(image.filename)
    )
    db.session.add(image)
    db.session.commit()

    return {
        "status" : True,
        "message" : "Image uploaded successfully",
        "name" : secure_filename(image.filename),
        "path" : url_for('static',filename=f'upload/{topic_id}/{secure_filename(image.filename)}')
    }

@bp_education.route("/module/<string:code>/image-upload", methods=['POST'])
def image_upload_new_topic(code):
    pass

@bp_education.route("/topic/<string:title>/image-upload", methods=['POST'])
@login_required
def image_upload_topic(title):
    topic = Topic.query.filter_by(title=title).first_or_404()
    file_up = request.files['image']
    return save_image(file_up, topic.id)
