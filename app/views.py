from flask import Flask, redirect, url_for, render_template, g
from app import app, lm, db
from flask_login import LoginManager, UserMixin, login_user, logout_user,\
    current_user, login_required
from oauth import OAuthSignIn

from .forms import StudentForm
from .models import User, Student
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html',
                           title='Login')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.before_request
def before_request():
    g.user = current_user
#underconstruction
@app.route('/user/<nickname>', methods=['GET','POST'])
@login_required
def user(nickname):
    if g.user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    form = StudentForm()
    if form.validate_on_submit():
        print('one')
        student = Student(name=form.name.data, parent = g.user)
        print('2')
        db.session.add(student)
        print('3')
        db.session.commit()
        return redirect(url_for('index'))

    students = g.user.get_students()
    return render_template('user.html',
                            form = form,
                            students=students)
@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))
