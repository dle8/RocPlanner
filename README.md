# RocPlanner
RocPlanner is a website that help students pick the right courses and extract the most out of academic courses. This 
projects assists University of Rochester students to plan and organize their coursework wisely over 4 years of college. 

## Supported features
- Majors searching, courses dragging

## Technologies used
- [Python](https://www.python.org/) 
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Vue js](https://vuejs.org/)
- [Selenium](https://www.seleniumhq.org/)
- [Amazon Web Services S3](https://aws.amazon.com/s3/)


## Setup
1. Install [Node.js + npm](https://www.npmjs.com/get-npm) on your machine

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
$ python application.py
```

2. In other terminal, run the the Node.js application
```
$ cd client
$ npm run serve
```

## Todo:
- Course recommendation engine using topological sorting and [AWS Personalize](https://aws.amazon.com/personalize/)


## Contacts:
Feel free to contact [me](dle8@u.rochester.edu) or [Hoang Le](hle7@u.rochester.edu) with any questions, comments,
suggestions, bug reports, etc.
