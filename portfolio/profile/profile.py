from flask import Blueprint, render_template, url_for, redirect, flash
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required, current_user

from .. import db
from ..models import User
from .forms import Change_password, Change_Username, Display_Settings

bp_profile = Blueprint('bp_profile', __name__, template_folder='templates', static_folder='static')

@bp_profile.route('/change-password', methods=['GET', 'POST'])
@register_breadcrumb(bp_profile, '.change-pass', 'Change Password')
@login_required
def change_password():
    form = Change_password()
    if form.validate_on_submit():
        if current_user.verify_password(form.current_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            return redirect(url_for('bp_profile.user_profile'))
        form.current_password.errors = ['Password Incorrect']
    return render_template('changepassword.html', title='Change Password', form=form)

@bp_profile.route('/change-username', methods=['GET', 'POST'])
@register_breadcrumb(bp_profile, '.change-user', 'Change Username')
@login_required
def change_username():
    form = Change_Username()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            current_user.username = form.username.data
            db.session.commit()
            return redirect(url_for('bp_profile.user_profile'))
        form.password.errors = ['Password Incorrect']
    else:
        form.username.data = current_user.username
        form.current_username.data = current_user.username
    return render_template('changeusername.html', title='Change Username', form=form)

@bp_profile.route('/display-settings', methods=['GET', 'POST'])
@register_breadcrumb(bp_profile, '.display', 'Display Settings')
@login_required
def dark_mode_setting():
    form = Display_Settings()
    if form.validate_on_submit():
        current_user.accessibility = form.accessibility.data
        current_user.dark_mode = form.dark.data
        db.session.commit()
        return redirect(url_for('bp_profile.user_profile'))

    else:
        form.accessibility.default = current_user.accessibility
        # Change radio button default dynamically
        # This code was adapted from Stack Overflow post by jeinarsson 2015-01-15
        # accessed on 2023-01-05
        # https://stackoverflow.com/a/34820107/
        form.dark.default = current_user.dark_mode
        # end of referenced code
        form.process()

    return render_template('display-settings.html', title='Change Display Settings', form=form)

@bp_profile.route('/')
@register_breadcrumb(bp_profile, '.', 'Profile')
@login_required
def user_profile():
    return render_template('profile.html', title='Profile')

@bp_profile.route('/settings')
def anonymous_settings():
    return render_template('anonymoussettings.html', title='Profile')
