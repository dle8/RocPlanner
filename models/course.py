from server import db


class CourseModel(db.Model):
    __tablename__ = 'courses'

    code = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    credits = db.Column(db.String(4), nullable=False)
    term = db.Column(db.String(64), nullable=False)
    prerequisite = db.Column(db.String(1024))
    description = db.Column(db.Text())
    cluster = db.Column(db.String(512))