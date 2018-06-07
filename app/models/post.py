from app.extensions import db
from datetime import datetime
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    rid = db.Column(db.Integer,index=True,default=0)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))

