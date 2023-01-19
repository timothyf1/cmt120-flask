import markdown
from markdown.extensions.tables import TableExtension
import bleach

from flask import Blueprint, redirect, render_template, request, url_for
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
    content = bleach.clean(markdown.markdown(page.content, extensions=['tables', 'fenced_code']), tags=app.config['ALLOWED_TAGS'], attributes=app.config['ALLOWED_ATTRIBUTES'])
    return render_template('home.html',title='Home', heading=page.title, content=content)


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
        return redirect(url_for('bp_home.home'))
    else:
        form.title.data = page.title
        form.content.data = page.content

    return render_template('edit-home.html', title='Edit Home', page=page, form=form)


@bp_home.route("/preview", methods=['POST'])
@login_required
def preview():
    mkd = request.json['markdown']
    title = f"<h1>{request.json['title']}</h1>"
    html = title + bleach.clean(markdown.markdown(mkd, extensions=['tables', 'fenced_code']), tags=app.config['ALLOWED_TAGS'], attributes=app.config['ALLOWED_ATTRIBUTES'])
    return {"html": html}
