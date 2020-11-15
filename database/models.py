from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class TestModel(db.Document):
    name = db.StringField(required=True)
