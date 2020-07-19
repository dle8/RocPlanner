from flask import Flask,jsonify
from flask_cors import CORS
from pymongo import MongoClient

import json

app = Flask(__name__, static_url_path='/static')

CORS(app)

@app.route('/api/course-list')
def course_list():
    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")

    # database  
    db = myclient["school"]
    CollectionCourses = db["courses"]
    courses = CollectionCourses.find()

    results = []

    for course in courses:
        result = {
                "name": course['name'], 
                'code': course['code'], 
                'credits': course['credit_points']
        }
        results.append(result)
    return json.dumps(results)

@app.route('/api/major-list')
def major_list():
    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")

    # database  
    db = myclient["school"]
    CollectionMajors = db["majors"]

    majors = CollectionMajors.find()
    results = []

    for major in majors:
        result = {
            "name": major['title'],
            "code": major['code'],
            "value": major['code'] + ' - ' + major['title'],
            "label": major['code'] + ' - ' + major['title']
        }
        results.append(result)
    return json.dumps(results)


@app.route('/api/course-detail/<course_code>')
def course_details(course_code):
    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")

    # database  
    db = myclient["school"]
    CollectionCourses = db["courses"]
    course = list(CollectionCourses.find({"code" : course_code}))
    del course[0]["_id"]

    return json.dumps(course[0])

@app.route('/api/major-detail/<major_code>')
def major_details(major_code):
    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")

    # database  
    db = myclient["school"]
    CollectionMajors = db["majors"]

    major = list(CollectionMajors.find({"code" : major_code}))
    del major[0]["_id"]
    return json.dumps(major[0])

def process_data():
    # Making Connection 
    myclient = MongoClient("mongodb://localhost:27017/")  

    # Delete database if exist
    myclient.drop_database("school")

    # database  
    db = myclient["school"]
    CollectionCourses = db["courses"]
    CollectionMajors = db["majors"]

    courses = json.load(open('courses.json'))
    majors = json.load(open('majors.json'))

    CollectionMajors.insert_many(majors)
    CollectionCourses.insert_many(courses)

    myclient.close()

if __name__ == '__main__':
    process_data()
    app.run(host="0.0.0.0")
