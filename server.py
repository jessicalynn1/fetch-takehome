from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db, User, Partner, UserPartner
from datetime import datetime

from jinja2 import StrictUndefined
import webbrowser

app = Flask(__name__, static_url_path='/static') 
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def welcome_page():
    """Show the Welcome page"""

    return render_template("homepage.html")

@app.route("/user_homepage", methods=["POST"])
def user_homepage():
    """Shows user their current point balance."""
    email = request.form.get("email")
    password = request.form.get("password")

    if email == "" or password == "":
        flash ("Not a valid email/password combination.")
    else:
        user_exist = User.query.filter_by(email=email).first()

        if user_exist:
            flash ("This email is already registered on our website. Please log in.")
        else:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash ("Account created! Please log in.")
    
    return render_template("/user_homepage")


@app.route("/login", methods=["POST"])
def log_in():
    """Existing user log in."""
    
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = User.query.filter_by(email=email).first()
    
    if not user or user.password != password:
        flash("Your input does not match our records. Please try again.")

    else:
        session["user"] = user.id
        flash(f"Welcome, {user.email}!")
        return redirect("/points_page")
   
    return redirect("/")

@app.route("/add_points", methods=["POST"])
def add_points():
    """Adds points to user's account."""

    email = request.form.get("email")
    p_name = request.form.get("partner")
    
    user = User.query.filter_by(email=email).first()
    partner = Partner.query.filter_by(p_name=name).first()
    points = #Not sure how to calculate points

    #if user does something to prompt points being added to their account
    
    save_points = UserPartner(user_id=user.id, partner_id=partner.id, points= , timestamp=datetime.now())
    db.session.add(save_points)
    db.session.commit()

    return redirect('user_homepage')


@app.route("/spend_points", methods=["POST"])
def spend_points():
    """Spends points in user's account."""

    email = request.form.get("email")
    p_name = request.form.get("partner")
    
    user = User.query.filter_by(email=email).first()
    partner = Partner.query.filter_by(p_name=name).first()
    points = #Not sure how to calculate points

    #if user does something to prompt points being removed from their account
    
    minus_points = UserPartner(user_id=user.id, partner_id=partner.id, points= , timestamp=datetime.now())
    db.session.add(minus_points)
    db.session.commit()

    return redirect('user_homepage')


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)