# RocPlanner
RocPlanner is a course-planner website that assists University of Rochester students in planning out their 4-year college academic plan.

#### Website URL: https://rocplanner.herokuapp.com/

## Supported features
- Majors/Courses Searching, College Study Planning
- Course Recommendation Engine (in development)

## Technologies used
- [Python](https://www.python.org/) 
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- [Node.js](https://nodejs.org/en/)
- [Vue.js](https://vuejs.org/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
## Setup
1. Install [Node.js + npm](https://www.npmjs.com/get-npm) and [MongoDB](https://docs.mongodb.com/manual/installation/) on your machine

2. Clone this repository on your local machine
```
$ git clone https://github.com/dle8/RocPlanner.git
$ cd RocPlanner
```

3. Install client side dependencies
```
$ cd client
$ npm install
```

4. Create environment file for backend and install dependencies
```
$ virtualenv venv
$ pip install -r requirements.txt
```

## Run locally (default port 5000)
```
$ python main.py
```

2. In other terminal, run the Node.js application
```
$ cd client
$ npm run serve
```

## Todo:
- Course recommendation engine using topological sorting and [Google Recommendations AI](https://cloud.google.com/recommendations)


## Contacts:
Feel free to contact [me](dle8@u.rochester.edu) or [Hoang Le](hle7@u.rochester.edu) with any questions, comments,
suggestions, bug reports, etc.
