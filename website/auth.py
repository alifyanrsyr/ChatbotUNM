from . import db
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')

      user = User.query.filter_by(email=username).first()
      if User :
         if ( user.password == password):
            print("login succes")
            return redirect(url_for('views.main'))
         else:
            print("password salah")
      else:
         print("email tidak terdaftar")

   return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
   return "<p>Logout</P>"
