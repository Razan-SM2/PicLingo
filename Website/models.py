from . import db
from flask_login import UserMixin 



# database schema 
class Mentor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    Images = db.relationship('Image')
    
class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  width =  db.Column(db.Integer)
  high =  db.Column(db.Integer)
  #foriegn key
  creator_id = db.Column(db.Integer, db.ForeignKey('mentor.id'))

  