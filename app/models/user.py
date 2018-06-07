from app.extensions import db
from flask import flash,url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import JSONWebSignatureSerializer as Serializer,BadSignature,SignatureExpired
import os
from app.extensions import login_manage

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique=True)
    passwd_hash = db.Column(db.String(128),unique=True)
    birthday = db.Column(db.DATE,unique=True)
    email = db.Column(db.String(32))
    head_picture = db.Column(db.String(128),default="fish.png")
    confirmed = db.Column(db.Boolean,default=False)
    post = db.relationship('Posts',backref="user",lazy="dynamic")
    favorite = db.relationship('Posts',secondary="collections",backref=db.backref('users',lazy="dynamic"),lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('不可访问属性')
    #密码加密
    @password.setter
    def password(self,passwd):
        self.passwd_hash = generate_password_hash(passwd)
    #密码校验
    def verify_password(self, passwd):
        return check_password_hash(self.passwd_hash,passwd)
    def generate_token(self):
        serializer = Serializer(os.environ.get('SECRET_KEY') or '123456')
        token = serializer.dumps({'id':self.id})
        return token
    @staticmethod
    def check_token(token):
        serializer = Serializer(os.environ.get('SECRET_KEY') or '123456')
        try:
            data = serializer.loads(token)
        except BadSignature:
            flash(message='无效token')
            return False
        except SignatureExpired:
            flash(message='token以过期')
            return False
        user = User.query.get(data.get('id'))
        if not user:
            flash(message='用户不存在')
            return False
        if not user.confirmed:
            user.confirmed = True
            db.session.add(user)
        return True
@login_manage.user_loader
def load_user(uid):
    return User.query.get(uid)