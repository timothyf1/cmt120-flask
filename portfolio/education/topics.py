import markdown
import bleach
from datetime import datetime

from flask import abort, redirect, render_template, request, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import current_user, login_required

from .. import app, db
from ..models import Module, Topic, Tag, ImageUpload

from .breadcrumbs import *
from .education import bp_education
from .form import New_Topic, Edit_Topic, Delete
from .imageupload import save_image


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
        # Check to see if the topic is a draft and if admin isn't logged in
        if topic.draft and not current_user.is_authenticated:
            abort(401)

        content = bleach.clean(markdown.markdown(topic.content), tags=app.config['ALLOWED_TAGS'], attributes=app.config['ALLOWED_ATTRIBUTES'])
        return render_template('topics/topic-view.html', title=topic.title, topic=topic, content=content)

    abort(404, description=f"Topic '{title}' does not exists. Please go to <a href='{url_for('bp_education.topics_list')}'>topics list</a> to view available topics.")


@bp_education.route("/module/<string:code>/new-topic", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.module.new-topic', '', dynamic_list_constructor=topic_new_breadcrumb)
@login_required
def new_topic(code):
    module = Module.query.filter_by(code=code).first_or_404()
    form = New_Topic()

    if form.validate_on_submit():
        topic = Topic(
            title = form.title.data,
            content = form.content.data,
            tags = create_tag_list(form.tags.data),
            author_id = current_user.id,
            module = module,
            draft = False if form.submit.data else True
        )
        db.session.add(topic)
        db.session.commit()

        # Check to see if image uploaded
        if form.upload.data:
            upload_status = save_image(form.image.data, topic.id)
            if not upload_status['status']:
                flash(upload_status['message'], 'error')
            else:
                flash(upload_status['message'], 'info')
            return redirect(url_for('bp_education.edit_topic', title=topic.title))

        return redirect(url_for('bp_education.view_topic', title=topic.title))

    return render_template('topics/new-topic.html', title='New topic', form=form, module=module)


@bp_education.route("/topic/<string:title>/edit", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.topic.edit', '', dynamic_list_constructor=topic_edit_breadcrumb)
@login_required
def edit_topic(title):
    topic = Topic.query.filter_by(title=title).first_or_404()
    images = ImageUpload.query.filter_by(topic_id=topic.id)
    form = Edit_Topic()

    if form.validate_on_submit():
        topic.title = form.title.data
        topic.content = form.content.data
        topic.tags = create_tag_list(form.tags.data)
        topic.last_updated = datetime.utcnow()
        topic.draft = False if form.submit.data else True
        db.session.commit()
        return redirect(url_for('bp_education.view_topic', title=topic.title))

    if request.method == 'GET':
        form.title.data = topic.title
        form.current_title.data = topic.title
        form.tags.data = " ".join([tag.name for tag in topic.tags])
        form.content.data = topic.content

    return render_template('topics/edit-topic.html', title='Edit topic', form=form, topic=topic, images=images)


@bp_education.route("/topic/<string:title>/delete", methods=['GET', 'POST'])
@register_breadcrumb(bp_education, '.topic.delete', '', dynamic_list_constructor=topic_delete_breadcrumb)
@login_required
def delete_topic(title):
    topic = Topic.query.filter_by(title=title).first_or_404()
    form = Delete()

    if form.validate_on_submit():
        db.session.delete(topic)
        db.session.commit()
        return redirect(url_for('bp_education.topics_list'))

    return render_template('delete.html', title='Delete topic', form=form, topic=topic)


@bp_education.route("/module/<string:code>/preview", methods=['POST'])
@bp_education.route("/topic/<string:title>/preview", methods=['POST'])
@login_required
def preview(title=None, code=None):
    mkd = request.json['markdown']
    title = f"<h1>{request.json['title']}</h1>"
    html = title + bleach.clean(markdown.markdown(mkd), tags=app.config['ALLOWED_TAGS'], attributes=app.config['ALLOWED_ATTRIBUTES'])
    return {"html": html}
