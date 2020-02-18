from app import *
import models

db.drop_all()
db.create_all()
db.session.commit()