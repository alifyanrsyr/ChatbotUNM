from flask import Blueprint, render_template, request, jsonify
from .process import generate_response, preparation

preparation()

views = Blueprint('views', __name__)

@views.route('/')
def home():
   return render_template("home.html")

@views.route('/main', methods=['GET', 'POST'])
def main():
   inputUsr = None
   if request.method == 'POST':
      inputUsr = request.form.get('input-user')
      print(inputUsr)
      
   return render_template("main.html")

@views.route("/get", methods=["GET", "POST"])
def get_bot_response():
   user_input = request.form.get('message')
   print(user_input)
   bot_response = generate_response(user_input)
   return bot_response
