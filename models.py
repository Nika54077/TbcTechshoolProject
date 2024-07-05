from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String())
    username = db.Column(db.String())
    role = db.Column(db.String())

    def __init__(self, username, password, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role


    def check_password(self, password):
        return check_password_hash(self.password, password)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)













