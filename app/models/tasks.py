from app import *

class Tasks(db.Model):
    __tablename__:'tasks'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    rating = db.Column(db.Integer, nullable = False)
    
    def __init__(self, name, description, rating):
        self.name = name
        self.description = description
        self.rating = rating
        
    def set_name(self, name):
        self.name = name  
        
    def set_description(self, description):
        self.description = description  
        
    def set_rating(self, rating):
        self.rating = rating  