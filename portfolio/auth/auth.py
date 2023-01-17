from datetime import datetime

from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, logout_user, current_user, login_user

from .. import db
from ..models import User
from .forms import Login_form, New_password

bp_auth = Blueprint('bp_auth', __name__, template_folder='templates', static_folder='static')

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bp_home.home'))
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.verify_password(password = form.password.data):
            login_user(user)
            current_user.last_login = datetime.utcnow()
            if current_user.default_password:
                return redirect(url_for('bp_auth.new_password'))
            db.session.commit()
            flash('Login Successful', 'info')
            return redirect(url_for('bp_home.home'))
        flash('Invalid username and password combination', 'error')
        # return redirect(url_for('bp_auth.login'))
    return render_template('login.html', title='Login', form=form)

@bp_auth.route('/new-password', methods=['GET', 'POST'])
@login_required
def new_password():
    form = New_password()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        current_user.default_password = False
        db.session.commit()
        flash('Password updated', 'info')
        return redirect(url_for('bp_home.home'))
    return render_template('newpassword.html', form=form)

@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Successful', 'info')
    return redirect(url_for('bp_home.home'))
