from server import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(256), nullable=False)
    hashed_password = db.Column(db.String(94), nullable=False)
    class_year = db.Column(db.Integer, nullable=False)

    is_authenticated = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    confirmation_code = db.Column(db.Integer)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)

    def get_id(self):
        return self.id

    def is_active(self):
        return self.is_active

    def is_authenticated(self):
        return self.is_authenticated
