from app import *
import datetime

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    surname = db.Column(db.String, nullable = False)
    status = db.Column(db.String)
    last_activity = db.Column(db.DateTime, nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    access = db.Column(db.String, nullable = False)
    tags = db.Column(db.String)
    
    login = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    
    def __init__(self, login, password):
        self.name = ''
        self.surname = ''
        self.status = ''
        self.last_activity = datetime.datetime.now()
        self.rating = 0
        self.access = 'User'
        self.tags = ''
        self.login = login
        self.password = password
        
    def set_name(self, name):
        self.name = name    
    
    def set_surname(self, surname):
        self.surname = surname
        
    def set_last_activity(self, last_activity):
        self.last_activity = last_activity
        
    def set_rating(self, password):
        self.password = password
    
    def set_access(self, access):
        self.access = access
        
    def set_tags(self, tags):
        self.tags += f'{tags};'
    
    def set_password(self, password):
        self.password = password