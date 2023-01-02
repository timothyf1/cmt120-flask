from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from .. import db
from ..models import Course, Module, Post

from .forms import New_post

import markdown

bp_posts = Blueprint('bp_posts', __name__, template_folder='templates')

@bp_posts.route("/")
def posts_list():
    posts = Post.query.all()
    return render_template('post-list.html',title='Posts', posts=posts)

@bp_posts.route("/<string:title>")
def view_post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    content = markdown.markdown(post.content)
    print(content)
    return render_template('post-view.html', title=post.title, post=post, content=content)

@bp_posts.route("/<string:module_code>/new-post", methods=['GET', 'POST'])
def new_post(module_code):
    module = Module.query.filter_by(code=module_code).first_or_404()
    form = New_post()

    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            content = form.content.data,
            author_id = current_user.id,
            module = module
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('bp_posts.view_post', title=post.title))
    return render_template('new-post.html', title='New post', form=form, module=module)
