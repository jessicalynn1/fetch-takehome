from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    f_name = db.Column(db.String, unique=False)
    l_name = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User id={self.id} f_name={self.f_name} l_name={self.l_name}>'


class Partner(db.Model):
    """A Partner."""

    __tablename__ = 'partners'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, unique=False)

    def __repr__(self):
        return f'<Partner id={self.id} name={self.name}>'


class UserPartner(db.Model):
    """Join table for User and Partner"""

    __tablename__ = 'userpartner'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    partner_id = db.Column(db.Integer, db.ForeignKey("partner.id"), nullable=False)
    points = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    user = db.relationship("User", backref="userpartner")
    partner = db.relationship("Partner", backref="userpartner")

    def __repr__(self):
        return f'<UserPartner id={self.id} points={self.points} timestamp={self.timestamp}'


def connect_to_db(app, db_uri="postgresql:///results", echo=False):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
