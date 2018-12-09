import datetime
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_caching import Cache

# 初始化第三方插件
def init_ext(app):
    # 全局配置session信息
    init_session(app)
    #  全局配置cookie信息
    init_cookie(app)
    # 初始化数据库
    init_db(app)
    # 初始化登录模块
    init_login(app)
    # 初始化缓存
    init_caching(app)
    # 初始化文件上传
    init_upload(app)




db = SQLAlchemy()
migrate = Migrate()


# 初始化数据库
def init_db(app):
    # 数据的连接的路径
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flask_api?charset=utf8'
    # 打印sql语句
    app.config['SQLALCHEMY_ECHO'] = True
    # 自动提交事务
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 禁用更新信号,
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app=app, db=db)


# 实例化登录对象
lm = LoginManager()
"""
session
cookie

"""


def init_login(app: Flask):
    lm.login_view = '/account/login/'
    # basic   strong  None
    lm.session_protection = 'strong'
    lm.init_app(app)


# 其他配置
"""
session 存储的位置
# cookie 相关配置
"""

cache = Cache()

"""
pip install redis

CACHE_DEFAULT_TIMEOUT 连接redis超时时间
CACHE_KEY_PREFIX     redis缓存key的前缀
CACHE_REDIS_HOST       ip
CACHE_REDIS_PORT       端口
CACHE_REDIS_PASSWORD   密码
CACHE_REDIS_DB         redis数据库的索引号
CACHE_REDIS_URL        使用url连接地址的方式配置连接数据
"""


# session配置
def init_session(app: Flask):
    # 配置加密session数据的秘钥
    app.config['SECRET_KEY'] = '1AFDASFDSFSDFSafdsfds1111'
    # 表示使用redis来存储session数据
    app.config['SESSION_TYPE'] = 'redis'
    # 设置 session过期时间 默认是关闭浏览器 session失效
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=7)


"""
cookie包含
键
值
过期时间
限制
域名 
路径
只允许http协议访问cookie信息
secure



"""


def init_cookie(app: Flask):
    app.config['REMEMBER_COOKIE_NAME'] = ''
    # 默认是365天 时间对象
    app.config['REMEMBER_COOKIE_DURATION'] = datetime.timedelta(days=7)
    app.config['REMEMBER_COOKIE_PATH'] = '/'
    # app.config['REMEMBER_COOKIE_DOMAIN'] = '.baidu.com'
    # app.config['REMEMBER_COOKIE_HTTPONLY'] = True


"""
模板使用
视图使用

"""
CACHE_CONFIG = {
    # 使用redis数据库作为缓存
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': '6379',
    'CACHE_REDIS_DB': '1',
    # 'CACHE_REDIS_PASSWORD': '123456',
}


def init_caching(app: Flask):
    cache.init_app(app, config=CACHE_CONFIG)


"""
文件上传配置
pip install flask-uploads
"""

"""
post请求 form-data

UploadSet 文件上传的核心对象

"""
from flask_uploads import UploadSet, IMAGES, DOCUMENTS, configure_uploads

# media
"""
name 上传文件的子目录 默认是files  
extensions  上传文件的类型(扩展名),默认是 TEXT + DOCUMENTS + IMAGES + DATA
default_dest 配置文件上传的根目录 例如D:\work\PycharmProjects\1805\flask_cache\apps\media
"""
# 上传图片
img_set = UploadSet(name='images', extensions=IMAGES)
# 上传文档文件
doc_set = UploadSet(name='doc', extensions=DOCUMENTS)

"""
 config_uploads 初始化UploadSet对象
"""
# 优秀的程序员应该专注的是模型设计
# 垃圾的程序员专注于解决bug


BASE_DIR = os.path.dirname(__file__)
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'static/upload/')


def init_upload(app: Flask):
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    # 配置文件上传的最大长度
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
    # 生成图片的url地址 默认x/_uploads/images/user/1/2_1.jpg
    app.config['UPLOADS_DEFAULT_URL'] = '/static/upload/'
    # 初始化img_set
    configure_uploads(app, img_set)
    # patch_request_class(app,size=32 * 1024 * 1024)
    configure_uploads(app, doc_set)
