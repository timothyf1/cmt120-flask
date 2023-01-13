from flask import Blueprint, redirect, render_template, url_for
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required

from .. import db
from ..models import Experience

from .form import Experience as Experience_form

bp_experience = Blueprint('bp_experience', __name__, template_folder='templates', static_folder='static')

@bp_experience.route("/")
@register_breadcrumb(bp_experience, '.', 'Experience')
def experience():
    experiences = Experience.query.all()
    return render_template('experience.html', title='Experience', experiences=experiences)

@bp_experience.route("/new-experience", methods=['GET', 'POST'])
@register_breadcrumb(bp_experience, '.new', 'New Experience')
@login_required
def new_experience():
    form = Experience_form()
    if form.validate_on_submit():
        experience = Experience(
            title = form.title.data,
            employer = form.employer.data,
            location = form.location.data,
            start = form.start.data,
            end = form.end.data,
            current = form.current.data,
            description = form.description.data
        )
        db.session.add(experience)
        db.session.commit()
        return redirect(url_for('bp_experience.experience'))
    return render_template('new-experience.html', form=form)

@bp_experience.route("/<string:title>/edit", methods=['GET', 'POST'])
@register_breadcrumb(bp_experience, '.edit', 'Edit Experience')
@login_required
def edit_experience(title):
    form = Experience_form()
    experience = Experience.query.filter_by(title=title).first_or_404()
    if form.validate_on_submit():
        experience.title = form.title.data
        experience.employer = form.employer.data
        experience.location = form.location.data
        experience.start = form.start.data
        experience.end = form.end.data
        experience.current = form.current.data
        experience.description = form.description.data
        db.session.commit()
        return redirect(url_for('bp_experience.experience'))
    else:
        form.title.data = experience.title
        form.employer.data = experience.employer
        form.location.data = experience.location
        form.start.data = experience.start
        form.end.data = experience.end
        form.current.data = experience.current
        form.description.data = experience.description
    return render_template('new-experience.html', form=form)