from flask import jsonify, render_template
from forms import LoginForm, RegisterForm
from models.user import UserModel
from werkzeug.security import generate_password_hash, check_password_hash
from server import application, db
import random


@application.route('/auth', methods=['GET', 'POST'])
def authenticate():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = None
        password = form.password.data
        form.password.data = None
        print('{} {}'.format(email, password))
        return jsonify('ok')

    return render_template('login.html', form=form)


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

        user = UserModel.query.filter_by(email=email).one_or_none()
        if user:  # email already in used by another user
            pass
        hashed_password = generate_password_hash(password=password)
        user = UserModel(email=email, hashed_password=hashed_password, class_year=class_year)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)

        send_user_confirmation_code(name=name, email=email)

        return jsonify(message='Account confirmation email sent'), 201


@application.route('/users', methods=['POST'])
def register():
    return jsonify('ok')


def send_user_confirmation_code(name=None, email=None):
    user = UserModel.query.filter_by(email=email).one_or_none()
    user.confirmation_code = random.randrange(100000, 999999)
    db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
    pass
