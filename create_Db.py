from ext import nag, db
from modelebi import Meme , User

with nag.app_context():
    
    db.drop_all()
    db.create_all()
