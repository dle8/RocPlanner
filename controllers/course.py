from server import application
from flask_login import login_required
from flask import jsonify
import json
import os

courses = json.load(open(os.path.abspath('') + '/dataset/courses.json'))


@application.route('/api/course-list')
def course_list():
    return jsonify(
        [{'name': course[0]['name'], 'code': code, 'credits': course[0]['credit_points']}
         for code, course in courses.items()])


@application.route('/api/course-detail/<course_code>')
def course_details(course_code):
    return jsonify(courses[course_code][0])
