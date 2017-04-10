from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    age_group = None
    if form.validate_on_submit():
        print form.age.data
        if int(form.age.data) < 30:
            age_group = '1'
        elif int(form.age.data) < 55:
            age_group = '2'
        elif int(form.age.data) > 55:
            age_group = '3'
        else:
            age_group='0'
        
        user = User(email=form.email.data,
                    username=form.username.data,
                    gender=form.gender.data,
                    age = form.age.data,
                    weight=form.weight.data,
                    age_group = age_group,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)