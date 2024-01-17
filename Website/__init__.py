from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'sdjedfbjfb dfbciejdskmcwakdinfnk'  # for cryptography
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)
  
  from .views import views
  from .auth import auth 

  #register blueprint 
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  
  from .models import Mentor, Image
  create_database(app)

  return app 
  
#database creation
def create_database(app):
   with app.app_context():
     db.create_all()
     print('DB is created succesfully')
    