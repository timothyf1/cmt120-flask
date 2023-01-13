from flask import redirect, render_template, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required

from .. import db
from ..models import Topic, Tag

from .breadcrumbs import *
from .education import bp_education
from .form import Delete_Tag

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
