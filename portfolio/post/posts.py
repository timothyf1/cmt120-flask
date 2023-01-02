from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required
from .. import db
from ..models import Course, Module, Post

bp_posts = Blueprint('bp_posts', __name__, template_folder='templates')

@bp_posts.route("/")
def posts_list():
    posts = Post.query.all()
    return render_template('post-list.html',title='Posts', posts=posts)

@bp_posts.route("/<string:title>")
def view_post(title):
    post = Post.query.filter_by(title=title).first_or_404()
    return render_template('post-view.html', title=post.title, post=post)