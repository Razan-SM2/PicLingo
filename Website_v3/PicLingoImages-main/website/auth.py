from flask import Blueprint, render_template , request , flash ,redirect, url_for,Response
from .models import Mentor,Img
from werkzeug.security import generate_password_hash , check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename



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
        login_user(new_Mentor, remember=True)
        flash('Account created!', category='success')
        
        
  return render_template("signUp.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        mentor = Mentor.query.filter_by(email=email).first()
        if mentor:
            if check_password_hash(mentor.password, password):
                flash('Logged in successfully!', category='success')
                login_user(mentor, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200


@auth.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)