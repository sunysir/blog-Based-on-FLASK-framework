import os
class Config:
    #秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    #数据库相关配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #邮件发送
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "a694190253@gmail.com"
    MAIL_PASSWORD = "sy3523802"
    #图片上传字体大小
    MAX_CONTENT_LENGTH = 2*1024*1024
    #图片保存地址
    UPLOADED_PHOTOS_DEST = os.getcwd()+'/app/static/img/'



    @staticmethod
    def init_app():
        pass
#开发环境配置
class DevelopmentConfig(Config):
    #数据库地址
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/development'

#测试环境配置
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/testing'
#生产环境配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/production'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}