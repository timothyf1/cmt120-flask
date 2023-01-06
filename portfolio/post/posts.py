from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
from .. import db
from ..models import Course, Module, Post

from .forms import New_post, Edit_post, Delete_Post

import markdown
import bleach

bp_posts = Blueprint('bp_posts', __name__, template_folder='templates', static_folder='static')
allowed_tags = ['a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li',
                'code', 'strong', 'blockquote', 'em']

@bp_posts.route("/")
def posts_list():
    posts = Post.query.all()
    return render_template('post-list.html',title='Posts', posts=posts)

@bp_posts.route("/<string:title>")
def view_post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    content = bleach.clean(markdown.markdown(post.content), tags=allowed_tags)
    return render_template('post-view.html', title=post.title, post=post, content=content)

@bp_posts.route("/<string:module_code>/new-post", methods=['GET', 'POST'])
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
            return redirect(url_for('bp_posts.view_post', title=post.title))
        form.title.errors = ["This title has been used, please enter a different title"]
    return render_template('new-post.html', title='New post', form=form, module=module)

@bp_posts.route("/<string:title>/edit", methods=['GET', 'POST'])
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
            return redirect(url_for('bp_posts.view_post', title=post.title))
        form.title.errors = ["This title has been used, please enter a different title"]
    else:
        form.title.data = post.title
        form.content.data = post.content

    return render_template('edit-post.html', title='Edit post', form=form, post=post)

@bp_posts.route("/<string:title>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    form = Delete_Post()
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('bp_posts.posts_list'))

    return render_template('delete-post.html', title='Delete a post', form=form, post=post)

@bp_posts.route("/preview", methods=['POST'])
@bp_posts.route("/<string:title>/preview", methods=['POST'])
def preview(title):
    mkd = request.json['markdown']
    title = f"<h1>{request.json['title']}</h1>"
    html = title + bleach.clean(markdown.markdown(mkd), tags=allowed_tags)
    return {"html": html}
