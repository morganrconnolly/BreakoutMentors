import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
GOOGLE_LOGIN_CLIENT_ID = "54559040817-07a179t8qq7hh3ca2o53i9jjpha7m3oq.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "ms69tlDjVP6hquivmiYZCr1-"
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '283787298678211',
        'secret': 'e712ddc80caed08d39920a653eec4624'
    },
    'google': {
        'id': '54559040817-07a179t8qq7hh3ca2o53i9jjpha7m3oq',
        'secret': 'ms69tlDjVP6hquivmiYZCr1-'
    }
}
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'