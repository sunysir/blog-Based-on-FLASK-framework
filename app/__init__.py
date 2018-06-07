from app.config import config
from flask import Flask,render_template
from app.views import config_blueprint
from app.extensions import config_extensions
def create_app(config_name):
    app = flask = Flask(__name__)
    app.config.from_object(config.get(config_name) or config['default'])
    config[config_name or 'default'].init_app()
    config_extensions(app)
    config_blueprint(app)
    config_errorhandler(app)
    return app

def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_find(e):
        return render_template('error/404.html')

