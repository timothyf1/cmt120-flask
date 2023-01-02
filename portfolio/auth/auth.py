from datetime import datetime
from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, logout_user, current_user, login_user
from .. import db, login_manager
from ..models import User
from .forms import Login_form, Signup_form, Change_password, Dark_mode

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
            db.session.commit()
            return redirect(url_for('bp_home.home'))
        flash('Invalid username and password combination')
        # return redirect(url_for('bp_auth.login'))
    return render_template('login.html', title='Login', form=form)


@bp_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('bp_home.home'))
    form = Signup_form()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username = form.username.data).first()

        if existing_user is None:
            user = User(username = form.username.data)
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            login_user(user)
            current_user.last_login = datetime.utcnow
            db.session.commit()
            flash('Login Successful')
            return redirect(url_for('bp_home.home'))
        flash('Username already used')
    return render_template('signup.html', title='Signup', form=form)

@bp_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout Successful')
    return redirect(url_for('bp_home.home'))

@bp_auth.route('/changepassword', methods=['GET', 'POST'])
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

@bp_auth.route('/darkmode', methods=['GET', 'POST'])
@login_required
def dark_mode_setting():
    form = Dark_mode()
    if form.validate_on_submit():
        current_user.dark_mode = form.pref.data
        db.session.commit()
        return redirect(url_for('bp_auth.user_profile'))
    return render_template('darkmode.html', title='Change Dark Mode Setting', form=form)

@bp_auth.route('/profile')
@login_required
def user_profile():
    return render_template('profile.html', title='Profile')

@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None
    return User.query.get(int(user_id))

