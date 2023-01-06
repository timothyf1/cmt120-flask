from datetime import datetime
from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required, logout_user, current_user, login_user
from ..models import User
from .forms import Login_form, Signup_form

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
