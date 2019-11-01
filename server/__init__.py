from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from forms.forms import LoginForm, RegisterForm
import os

import json

application = Flask(__name__, template_folder='../templates', static_url_path='', static_folder='../static')
application.config['SECRET_KEY'] = 'secret'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Adu230999@localhost:3306/rocplanner'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(application)
CORS(application)


def _register_subpackages():
    import models


db = SQLAlchemy()
db.init_app(application)
_register_subpackages()
db.create_all(app=application)

courses = json.load(open(os.path.abspath('') + '/dataset/courses.json'))
majors = json.load(open(os.path.abspath('') + '/dataset/majors.json'))


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


@application.route('/users', methods=['POST'])
def register():
    return jsonify('ok')


@application.route('/api/course-list')
def course_list():
    return jsonify(
        [{'name': course[0]['name'], 'code': code, 'credits': course[0]['credit_points']}
         for code, course in courses.items()])


@application.route('/api/major-list')
def major_list():
    return jsonify([{
        'name': major['title'],
        'code': major['code'],
        'value': major['code'] + ' - ' + major['title'],
        'label': major['code'] + ' - ' + major['title']
    } for major in majors])


@application.route('/api/course-detail/<course_code>')
def course_details(course_code):
    return jsonify(courses[course_code][0])


@application.route('/api/major-detail/<major_code>')
def major_details(major_code):
    return jsonify([
                       major
                       for major in majors
                       if major['code'] == major_code
                   ][0])
