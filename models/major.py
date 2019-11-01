from server import db


class MajorModel(db.Model):
    __tablename__ = 'majors'

    code = db.Column(db.String(4), primary_key=True)
    title = db.Column(db.Text())
    premajor = db.Column(db.Text())
    core = db.Column(db.Text())
    elective = db.Column(db.Text())
    writing = db.Column(db.Text())

    def __init__(self, *args, **kwargs):
        super(MajorModel, self).__init__(*args, **kwargs)