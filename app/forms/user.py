from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,SubmitField,DateField,PasswordField,BooleanField,RadioField,SelectMultipleField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from app.models.user import User
from app.extensions import photos

#注册
class RegisterForms(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(4,20,message='4~20')],render_kw={'placeholder':'请输入用户名'})
    passwd = PasswordField('密码',validators=[DataRequired(),Length(6,20,message='密码长度6~20')])
    repasswd = PasswordField('再次输入密码',validators=[EqualTo('passwd',message="两次密码不一致")])
    email = StringField("邮箱",validators=[Email(message="请输入正确的邮箱地址")])
    data = DateField('出生日期',validators=[DataRequired()])
    submit = SubmitField('提交')
    #自定义验证器
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(str(field.data))
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(str(field.data))

class LoginForms(FlaskForm):
    username = StringField('用户名',validators=([DataRequired(message='用户名不为空')]))
    passwd = PasswordField('密码',validators=([DataRequired(message=',密码不为空')]))
    remember = BooleanField("下次自动登录")
    submit = SubmitField('登录')

class RepasswdForms(FlaskForm):
    old_passwd = PasswordField('原密码', validators=[DataRequired(), Length(6, 20, message='密码长度6~20')])
    new_passwd = PasswordField('新密码', validators=[DataRequired(), Length(6, 20, message='密码长度6~20')])
    repasswd = PasswordField('再次输入密码', validators=[EqualTo('new_passwd', message="两次密码不一致")])
    submit = SubmitField('提交')

class HeadForm(FlaskForm):
    photo = FileField("请传入图片",validators=[FileAllowed(photos,message="图片格式不对")])
    submit = SubmitField("上传")

class RemailForm(FlaskForm):
    remail = StringField('邮箱', render_kw={'placeholder':'请输入新邮箱'},validators=[Email(message='请输入正确的邮箱地址')])
    submit = SubmitField('确认修改')