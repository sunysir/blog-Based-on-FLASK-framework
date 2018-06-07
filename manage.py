from app import create_app
from app.extensions import config_extensions
from flask_script import Manager,Command
from app.views import config_blueprint
from flask_migrate import MigrateCommand
import os
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(config_name)
manage = Manager(app)
manage.add_command('db',MigrateCommand)


if __name__ == "__main__":
    manage.run()