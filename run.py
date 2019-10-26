from flask import Flask, jsonify
from flask_cors import CORS

import json

app = Flask(__name__, static_url_path='/static')

CORS(app)

courses = json.load(open('courses.json'))
majors = json.load(open('major_test.json'))


@app.route('/api/course-list')
def course_list():
    return jsonify(
        sorted(
            [
                {"name": course[0]['name'], 'code': code, 'credits': course[0]['credit_points']}
                for code, course in courses.items()
            ], key=lambda course: (str(course['code']).split(" ")[0], int(str(course['code']).split(" ")[1][:-1]))
        )
    )


@app.route('/api/major-list')
def major_list():
    return jsonify([{
        "name": major['title'],
        "code": major['code'],
        "value": major['code'] + ' - ' + major['title'],
        "label": major['code'] + ' - ' + major['title']
    } for major in majors])


@app.route('/api/course-detail/<course_code>')
def course_details(course_code):
    print(courses[course_code])
    return jsonify(courses[course_code][0])


@app.route('/api/major-detail/<major_code>')
def major_details(major_code):
    return jsonify([
                       major
                       for major in majors
                       if major['code'] == major_code
                   ][0])


if __name__ == '__main__':
    app.run(debug=True)
