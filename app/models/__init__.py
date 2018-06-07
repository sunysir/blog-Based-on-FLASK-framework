from app.extensions import db
from .user import User
from .post import Posts
collections = db.Table('collections',
    db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('posts_id', db.Integer, db.ForeignKey('posts.id'))
)