from bleach import clean
from markdown import markdown
from markdown.extensions.tables import TableExtension
from markupsafe import Markup

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required

from .. import app, db
from ..models import PageText
from .form import Edit_Home

bp_home = Blueprint('bp_home', __name__, template_folder='templates', static_folder='home-static')


@bp_home.route("/")
@register_breadcrumb(bp_home, '.', 'Home')
def home():
    page = PageText.query.filter_by(page_name='home').first()

    # Convert Markdown to HTML
    raw_html = markdown(
        page.content,
        extensions=app.config['MARKDOWN_EXTENSIONS']
    )

    # Clean the HTML to escape unapproved tags
    sanitized_html = Markup(clean(
        raw_html,
        tags=app.config['ALLOWED_TAGS'],
        attributes=app.config['ALLOWED_ATTRIBUTES']
    ))

    return render_template('home.html',title='Home', heading=page.title, content=sanitized_html)


@bp_home.route("/edit", methods=['GET', 'POST'])
@register_breadcrumb(bp_home, '.edit', 'Edit Home')
@login_required
def edit_home():
    page = PageText.query.filter_by(page_name='home').first()
    form = Edit_Home()

    if form.validate_on_submit():
        page.title = form.title.data
        page.content = form.content.data
        db.session.commit()
        flash("Home page updated successfully", category="info")
        return redirect(url_for('bp_home.home'))
    else:
        form.title.data = page.title
        form.content.data = page.content

    return render_template('edit-home.html', title='Edit Home', page=page, form=form)


@bp_home.route("/preview", methods=['POST'])
@login_required
def preview():
    # Read markdown and title from request
    mkd = request.json['markdown']
    title = f"<div class='heading'><h1>{request.json['title']}</h1></div>"

    # Convert Markdown to HTML
    raw_html = markdown(
        mkd,
        extensions=app.config['MARKDOWN_EXTENSIONS']
    )

    # Clean the HTML to escape unapproved tags
    sanitized_html = title + clean(
        raw_html,
        tags=app.config['ALLOWED_TAGS'],
        attributes=app.config['ALLOWED_ATTRIBUTES']
    )

    return {"html": sanitized_html}
