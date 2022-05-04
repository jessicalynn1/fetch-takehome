from flask import (Flask, request, session, jsonify)
from model import connect_to_db, db, User, Partner, UserPartner
from datetime import datetime

from jinja2 import StrictUndefined
import webbrowser

app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


user_points = []


# @app.route("/")
# def welcome_page():
#     """Show the Welcome page"""

#     return render_template("homepage.html")

# @app.route("/login", methods=["POST"])
# def log_in():
#     """Existing user log in."""
    
#     email = request.form.get("email")
#     password = request.form.get("password")
    
#     user = User.query.filter_by(email=email).first()
    
#     if not user or user.password != password:
#         flash("Your input does not match our records. Please try again.")

#     else:
#         session["user"] = user.id
#         flash(f"Welcome, {user.email}!")
#         return redirect("/points_page")
   
#     return redirect("/")

class Transaction:
    """Payers, points, and timestamp"""

    def __init__(self, payer, points, timestamp):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp


@app.route("/add_points", methods=["POST"])
def add_points():
    """Adds points to user's account."""


    #need to get the info below in json, might need to parse the date
    payer = request.form.get('payer')
    points = request.form.get('points')
    timestamp = DateTime.json #this needs to be in json

    new_transaction = Transaction(payer, points, timestamp)
    user_points.append(new_transaction)


@app.route("/spend_points", methods=["POST"])
def spend_points():
    """Spends points in user's account."""

    email = request.form.get("email")
    p_name = request.form.get("partner")
    
    user = User.query.filter_by(email=email).first()
    partner = Partner.query.filter_by(p_name=name).first()
    points = #Not sure how to calculate points

    #if user does something to prompt points being removed from their account
    

@app.route("/points_balance", methods=["GET"])
def points_balance():
    for x in user_points:
        points_dict = {}
        # if payer is not already in dict
        points_dict[x.payer] = x.points
        # if payer is in dictionary, just add points

        return points_dict
    
# @app.route("/user_homepage", methods=["POST"])
# def user_homepage():
#     """Shows user their current point balance."""
#     email = request.form.get("email")
#     password = request.form.get("password")

#     if email == "" or password == "":
#         flash ("Not a valid email/password combination.")
#     else:
#         user_exist = User.query.filter_by(email=email).first()

#         if user_exist:
#             flash ("This email is already registered on our website. Please log in.")
#         else:
#             user = User(email=email, password=password)
#             db.session.add(user)
#             db.session.commit()
#             flash ("Account created! Please log in.")
    
#     return render_template("/user_homepage")


# if __name__ == "__main__":
#     connect_to_db(app)
#     app.run(host="0.0.0.0", debug=True)