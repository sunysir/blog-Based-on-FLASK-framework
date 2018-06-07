from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.forms import PostsForm
from flask_login import current_user
from app.extensions import db
main = Blueprint('main',__name__)
from app.models import Posts

@main.route("/" ,methods=['GET', 'POST'])
def index():
    form = PostsForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            u = current_user._get_current_object()
            p = Posts(content=form.content.data, user=u)
            db.session.add(p)
        else:
            flash('需要登录才能发表')
            redirect("user.login")
        return redirect(url_for('main.index'))
    page = request.args.get("page", default=1, type=int)
    pagination = Posts.query.filter_by(rid=0).paginate(page, per_page=2,error_out=False)
    posts = pagination.items
    return render_template('user/index.html', form=form,posts=posts,pagination=pagination)