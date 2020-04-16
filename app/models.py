from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(6), unique=True)
    email = db.Column(db.String(50))
    location = db.Column(db.String(40))
    biography = db.Column(db.String(190))
    photo = db.Column(db.String(80))
    datejoined = db.Column(db.String(255))

    def __init__(self, firstname, lastname, email, gender, location, biography, photo, date):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender
        self.location = location
        self.biography = biography
        self.photo = photo
        self.datejoined = date
        
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
