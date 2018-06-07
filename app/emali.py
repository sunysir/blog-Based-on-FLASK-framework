from flask_mail import Mail,Message
from flask import Flask,render_template,current_app
from threading import Thread
from app.extensions import mail

def send_mail(to,subject,template,**kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=subject,recipients=[to],sender=app.config["MAIL_USERNAME"])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target=Mail_send, args=((app,msg)))
    thr.start()
    return thr
def Mail_send(app,msg):
    with app.app_context():
        mail.send(msg)




