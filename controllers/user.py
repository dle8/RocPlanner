from flask import render_template, flash, redirect, url_for, request, jsonify
from forms import LoginForm, RegisterForm, ResetPasswordForm, ConfirmationForm, ForgetPasswordForm
from models.user import UserModel
from werkzeug.security import generate_password_hash, check_password_hash
from server import application, db, celery, mail, login_manager
from flask_mail import Message
from flask_login import login_user, logout_user, current_user
import os
from config import config
import random


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

@application.route('/hidden')
def hidden():
    if current_user.is_authenticated:
        #return redirect("http://rocplanning.s3-website.us-east-2.amazonaws.com/")
        return redirect("http://localhost:8080")
    return redirect(url_for('home'))

@application.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('hidden'))
    return redirect(url_for('authenticate'))


@application.route('/auth', methods=['GET', 'POST'])
def authenticate():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = None
        remember_me = form.remember_me.data
        password = form.password.data
        form.password.data = None

        if (len(password)<6 or len(password)>15):
            flash('Password length must be between 6 and 15!')
            return redirect(url_for('authenticate'))


        user = UserModel.query.filter_by(email=email).one_or_none()
        if not user:
            flash('Email not existed. Please try again or register first!')
            #form = LoginForm()
            #return render_template('template.html', form=form, login=True, register=False, confirmation_code=False)
            return redirect(url_for('authenticate'))

        if not user.confirmed:
            flash('Account is not yet confirmed. Please check your email for confirmation code.')
            return redirect(url_for('validate_confirmation_code'))

        if not check_password_hash(password=password, pwhash=user.hashed_password):
            flash('Invalid email or password. Please try again!')
            #form = LoginForm()
            #return render_template('template.html', form=form)
            return redirect(url_for('authenticate'))

        login_user(user, remember=remember_me)
        flash('Success!')
        return redirect(url_for('hidden'))

    return render_template('template.html', form=form, login=True, register=False, confirmation_code=False)


@application.route('/confirmation_codes', methods=['GET','POST'])
def validate_confirmation_code():
    ##data = request.form.to_dict()
    #print(data)
    #user = UserModel.query.filter_by(id=data.get('user_id')).one_or_none()
    #if not user or user.confirmation_code != data['confirmation_code']:
    #    return jsonify({"message": "Verification failed"}), 401
    #return jsonify({"message": "Verification succeeded"}), 200
    form = ConfirmationForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = None
        confirmation_code = form.confirmation_code.data
        form.confirmation_code.data = None

        user = UserModel.query.filter_by(email=email).one_or_none()
        if user is None:  # email already in used by another user
            flash('No such user.')
            return redirect(url_for('validate_confirmation_code'))
        else:
            if (str(user.confirmation_code) == confirmation_code):
                user.confirmed = True
                db.session.add(user)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                flash('Account Confirmed!')
                return redirect(url_for('authenticate'))
            else:
                flash('Incorrect Code!')
    return render_template('template.html', form=form, register=False, confirmation_code=True, login=False)



@application.route('/users', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = None
        email = form.email.data
        form.email.data = None
        password = form.password.data
        form.password.data = None
        class_year = form.class_year.data
        form.class_year.data = None

        if (class_year<2019 or class_year>2023):
            flash('Class year must be between 2019 and 2023!')
            return redirect(url_for('register'))

        if (len(password)<6 or len(password)>15):
            flash('Password length must be between 6 and 15!')
            return redirect(url_for('register'))

        user = UserModel.query.filter_by(email=email).one_or_none()
        if user:  # email already in used by another user
            flash('Account or email already in used.')
            return redirect(url_for('authenticate'))

        hashed_password = generate_password_hash(password=password)
        user = UserModel(email=email, name=name, hashed_password=hashed_password, class_year=class_year)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)

        send_user_confirmation_code(name=name, email=email)

        flash('Account registered! Please check your email for confirmation code!')
        #return redirect(url_for('authenticate'))
        return redirect(url_for('validate_confirmation_code'))


    return render_template('template.html', form=form, register=True, confirmation_code=False, login=False)


@application.route('/forget', methods=["GET", 'POST'])
def forget_password():
    form = ForgetPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = None
        user = UserModel.query.filter_by(email=email).one_or_none()
        if not user:
            flash('Email not existed. Please try again or register first!')
            return redirect(url_for('forget_password'))
        else :
            send_user_confirmation_code(name=user.name, email=email)
            return redirect(url_for('reset_password'))

    return render_template('template.html',form=form, forget_password=True, confirmation_code=False, login=False)


@application.route('/reset', methods=["GET", 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = None
        confirmation_code = form.confirmation_code.data
        form.confirmation_code.data = None
        new_password = form.new_password.data
        form.new_password.data = None
        new_password_confirm = form.new_password_confirm.data
        form.new_password_confirm.data = None
        user = UserModel.query.filter_by(email=email).one_or_none()

        if not user:
            flash('Email not existed.')
            return redirect(url_for('reset_password'))
        if (new_password!=new_password_confirm):
            flash('Passwords not match!')
            return redirect(url_for('reset_password'))
        if (len(new_password)<6 or len(new_password)>15):
            flash('Passwords length must be between 6 and 15!')
            return redirect(url_for('reset_password'))
        else:
            if (str(user.confirmation_code) == confirmation_code):
                user.confirmed = True
                hashed_password = generate_password_hash(password=new_password)
                user.hashed_password = hashed_password
                db.session.add(user)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                flash('Password reset success!')
                return redirect(url_for('authenticate'))
            else:
                flash('Incorrect Code or Email!')



    return render_template('template.html',form=form, reset_password=True, confirmation_code=False, login=False)



def send_user_confirmation_code(name=None, email=None):
    user = UserModel.query.filter_by(email=email).one_or_none()
    confirmation_code = random.randrange(100000, 999999)
    user.confirmation_code = confirmation_code
    db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:
        print(e)

    send_email_via_gmail_smtp(
        from_email=config.MAIL_DEFAULT_SENDER,
        to_email=email,
        subject='Confirm your account',
        template='account_confirmation.html',
        name=name,
        confirmation_code=confirmation_code,
    )


@application.route('/logout')
def log_out():
    logout_user()
    return redirect(url_for('home'))


# @celery.task
def send_email_via_gmail_smtp(from_email, to_email, subject, template, **template_args):
    """Back ground task to send email with flask mail"""
    with application.app_context():
        msg = Message(
            'RocPlanner ' + subject,
            sender=from_email,
            recipients=[to_email]
        )
        template_path = os.path.join('', template)
        msg.html = render_template(template_path, **template_args)
        mail.send(msg)
