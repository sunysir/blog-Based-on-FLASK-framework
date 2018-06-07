from flask import Blueprint,render_template,flash,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from app.views.main import main
from app.models.user import User
# from app.models import Posts
from app.extensions import db
from app.emali import send_mail
from itsdangerous import JSONWebSignatureSerializer
from app.forms.user import RepasswdForms,LoginForms,RegisterForms,HeadForm,RemailForm
from flask_login import login_user,login_required,logout_user,current_user
from app.extensions import photos
import random
user = Blueprint('user',__name__)
@user.route("/user/", methods=['POST','GET'])
def register():
    form = RegisterForms()
    if form.validate_on_submit():
        u = User(username=form.username.data,password=form.passwd.data,birthday=form.data.data,email=form.email.data)
        db.session.add(u)
        db.session.commit()
        token = u.generate_token()
        send_mail(u.email, "账户激活", "/user/activate", token=token,username=form.username.data)
        flash("邮件已发送，请完成激活")
        return redirect(url_for("main.index"))
    return render_template('user/register.html',form=form)
@user.route('/activate/<token>')
def activate(token):
    if User.check_token(token=token):
        flash("用户激活成功")
        return redirect(url_for("main.index"))

@user.route("/login/",methods=['GET','POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        #返回一个User对象
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash("无效用户名")
        elif u.verify_password(form.passwd.data):
            if u.confirmed == True:
                flash("登录成功")
                u = login_user(u,remember=form.remember.data)
                return redirect(request.args.get('next') or url_for("main.index"))
            else:
                flash("用户没注册")
                token = u.generate_token()
                send_mail(u.email, "账户激活", "/user/activate", token=token, username=form.username.data)
                flash(str(u.confirmed))
                return redirect(url_for("main.index"))
        else:
            flash("密码错误")
    return render_template("user/login.html",form=form)

@user.route("/remail/",methods=['GET','POST'])
def remail():
    form = RemailForm()
    if form.validate_on_submit():
        u = current_user._get_current_object()
        send_mail(form.remail.data,'邮箱修改成功','user/activate')
        u.email = form.remail.data
        db.session.add(u)
        db.session.commit()
        flash("邮箱修改成功")
        return redirect(url_for("main.index"))
    return render_template("user/remail.html",form=form)
@user.route("/logout/")
def logout():
    logout_user()
    flash("您以退出登录")
    return redirect(url_for("main.index"))
@user.route("/test/")
@login_required
def test():
    return "hello"
@user.route("/profile/")
def profile():
    return render_template("user/profile.html")

@user.route("/passwd/",methods=['GET', 'POST'])
@login_required
def passwd():
    repasswdform = RepasswdForms()
    if repasswdform.validate_on_submit():
        u = User()
        u.password = repasswdform.old_passwd.data
        if  not current_user.verify_password(repasswdform.old_passwd.data):
            flash("原密码输入错误")
            return render_template("user/passwd.html", repasswdform=repasswdform)
        current_user.password = repasswdform.new_passwd.data
        db.session.add(current_user)
        db.session.commit()
        flash("密码修改成功")
        return redirect(request.args.get('next') or url_for("main.index"))
    return render_template("user/passwd.html",repasswdform=repasswdform)
def random_prefix(LENGTH=8):
    collect = "abcdefghigklmnopqrstuvwxyz0123456789"
    return "".join([random.choice(collect) for i in range(LENGTH)])
@user.route("head_portrait",methods=['GET','POST'])
def head_portrait():
    file = HeadForm()
    img_uri = None
    if file.validate_on_submit():
        suffix = file.photo.data.filename
        filename = random_prefix()+suffix
        current_user.head_picture = "../../static/img/"+filename
        db.session.add(current_user)
        db.session.commit()
        photos.save(file.photo.data,name=filename)
        render_template("common/base.html")
        print(img_uri)
        flash("头像修改成功")
    return render_template("user/head_portrait.html",file=file)