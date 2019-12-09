from server import application
from flask_login import login_required
from flask import jsonify
import json
import os

majors = json.load(open(os.path.abspath('') + '/dataset/majors.json'))


@application.route('/api/major-list')
def major_list():
    return jsonify([{
        'name': major['title'],
        'code': major['code'],
        'value': major['code'] + ' - ' + major['title'],
        'label': major['code'] + ' - ' + major['title']
    } for major in majors])


@application.route('/api/major-detail/<major_code>')
def major_details(major_code):
    return jsonify([
                       major
                       for major in majors
                       if major['code'] == major_code
                   ][0])
