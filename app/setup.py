from app import *
from models import users, tasks


db.drop_all()
db.create_all()
db.session.commit()