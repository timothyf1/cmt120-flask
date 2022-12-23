from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user
from portfolio import db, login_manager
from portfolio.auth.forms import Login_form, Signup_form
from portfolio.models import User

bp_auth = Blueprint('bp_auth', __name__, template_folder='templates')

@bp_auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.home'))
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.verify_password(password = form.password.data):
            login_user(user)
            return redirect(url_for('home_bp.home'))
        return redirect(url_for('bp_auth.login'))
    return render_template('login.html', title='Login', form=form)


@bp_auth.route('/auth/signup', methods=['GET', 'POST'])
def signup():
    form = Signup_form()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username = form.username.data).first()

        if existing_user is None:
            user = User(username = form.username.data)
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('home_bp.home'))

    return render_template('signup.html', title='Signup', form=form)

@bp_auth.route('/auth/logout')
def logout():
    logout_user()
    return redirect(url_for('home_bp.home'))


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return None
    return User.query.get(int(user_id))

