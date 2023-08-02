import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'webapp.db')
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/webapp'
    DBURL = 'webapp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'wvMEy<_2Y#<p.§#@#%Y(dD,6tU6B:S~gH>U.,6wP2xA~Mt<3xv&:E(Mjr@:sT:8{'
    JWT_ERROR_MESSAGE_KEY = 'message'
