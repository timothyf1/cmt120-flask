from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required, current_user
from .. import db
from ..models import User
from .forms import Change_password, Dark_mode

bp_profile = Blueprint('bp_profile', __name__, template_folder='templates', static_folder='static')

@bp_profile.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
    form = Change_password()
    if form.validate_on_submit():
        if current_user.verify_password(form.current_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            return redirect(url_for('bp_home.home'))
        form.current_password.errors = ['Password Incorrect']
    return render_template('changepassword.html', title='Change Password', form=form)

@bp_profile.route('/darkmode', methods=['GET', 'POST'])
@login_required
def dark_mode_setting():
    form = Dark_mode()
    if form.validate_on_submit():
        current_user.dark_mode = form.pref.data
        db.session.commit()
        return redirect(url_for('bp_profile.user_profile'))
    form.pref.default = current_user.dark_mode
    form.process()
    return render_template('darkmode.html', title='Change Dark Mode Setting', form=form)

@bp_profile.route('/profile')
@login_required
def user_profile():
    return render_template('profile.html', title='Profile')