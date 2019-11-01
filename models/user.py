from server import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(256), nullable=False)
    hashed_password = db.Column(db.String(94), nullable=False)
    class_year = db.Column(db.Integer, nullable=False)

    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmation_code = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)