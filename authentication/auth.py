from flask import Blueprint
from ..models import User
from .. import db
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


# User service model


class UserClass:
    success = True
    error = None


    def sign_up(self, fnane, lname, email, password):
        user = User(first_name=fnane,last_name=lname,email=email,password=generate_password_hash(password, method='sha256'))
        db.session.add(user)
        db.session.commit()
        return self.success


    def sign_in(self, email, password):
        try:
            user = User.query.filter_by(email=email).first()
            check_password_hash(user.password, password)
            login_user(user)
            return self.success

        except not user or not check_password_hash(user.password, password):
            return self.error


    def sign_out(self):
        logout_user()

    
    def check(self, email, password):
        user = User.query.filter_by(email=email).first()
        password = check_password_hash(user.password, password)
        if user and password:
            return self.success
        else:
            return self.error


