from .main import main
from .user import user
#封装函数，完成蓝本注册
DEFAULT_BLUEPRINT = (
    (main, ""),
    (user, '')
)
def config_blueprint(app):
    for blueprint,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint,url_prefix=prefix)