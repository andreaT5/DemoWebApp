from extension import db
from datetime import date
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    fullname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def hash_password(cls, password):
        return pbkdf2_sha256.hash(password)
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def verify_password(cls, password, hashed):
        return pbkdf2_sha256.verify(password, hashed)