from flask_login import LoginManager , UserMixin
from ext import db , login_manager

class Meme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    img = db.Column(db.String())
    

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @staticmethod
    def save():
        db.session.commit()

class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())        
    password = db.Column(db.String())
    
  
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @staticmethod
    def save():
        db.session.commit()
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)