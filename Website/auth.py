from flask import Blueprint, render_template , request , flash
from .models import Mentor
from werkzeug.security import generate_password_hash , check_password_hash
from . import db 


auth = Blueprint('auth', __name__)

@auth.route('/signUp' , methods=['GET' , 'POST'])
def signUp():
  if request.method =='POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email)<4:
        flash('Invalied email , must be grater than 3 charectirs' , category='error')
       
    elif len(firstName)<2:
         flash('First name must be greater than 1 character.', category='error')
    elif password1 != password2:
        flash('Passwords don\'t match.', category='error')
    elif len(password1)<7:
        flash('Password must be at least 7 characters.', category='error')
    else: 
        new_Mentor= Mentor(email=email, firstName=firstName,password=generate_password_hash(password1, method='pbkdf2:sha256'))
        db.session.add(new_Mentor)
        db.session.commit()
        flash('Account created!', category='success')
        
        
  return render_template("signUp.html")