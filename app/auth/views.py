from flask import render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required


from . import auth
from .. import db
from ..models import NkRegister
from app.auth.managedb import AdminLoginPage


@auth.route('/', methods=['GET','POST']) #only for ui desktop
# @auth.route('/login', methods=['GET','POST'])
def login():
    email = request.form.get('username')
    password = request.form.get('password')


    if email != None and password != None:
        user = NkRegister.query.filter_by(username=email).first()

        if not user or not check_password_hash(user.password_hash, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.adminHome'))

    return render_template('auth/login.html')


@auth.route('/signup', methods=['GET', 'POST'])
# @auth.route('/', methods=['GET', 'POST'])
def signup():
    is_admin = True
    is_public = False

    company_name =  request.form.get('company-name')
    username =  request.form.get('username')
    password =  request.form.get('password')
    repeat_password = request.form.get('password1')


    if company_name != None and username != None and password != None:
        nkregirster =  NkRegister.query.filter_by(name=company_name, username=username).first()

        if nkregirster:
            flash('Email address already exists')
            return redirect(url_for('auth.signup')) 
            
        elif password == repeat_password:
            new_user = NkRegister(name=company_name, username=username, is_admin=True, is_public=False,
                    password_hash=generate_password_hash(password, method='sha256')) 
                     
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login')) 
        flash('Password did not match')
    return render_template('auth/signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))