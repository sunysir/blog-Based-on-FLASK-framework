from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import Length


class PostsForm(FlaskForm):
    content = TextAreaField('',render_kw={'placeholder':'此时的想法...'},validators=[Length(5,128,message="至少5字")])
    submit = SubmitField("发表")