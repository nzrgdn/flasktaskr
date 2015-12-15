import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktask.db'
#USERNAME = 'admin'
#PASSWORD = 'admin'
'''
The WTF_CSRF_ENABLED config setting is used for cross-site request forgery 
prevention, which makes your app more secure. 
This setting is used by the Flask-WTF exten-sion.
'''
WTF_CRSR_ENABLED = True
'''
The SECRET_KEY config setting is used in conjunction with the WTF_CSRF_ENABLED 
setting in order to create a cryptographic token that is used to validate a form. 
It’s also used for the same reason in conjunction with sessions. 
Always make sure to set the secret key to something that is nearly impossible to guess. 
Use a random key generator.
'''
SECRET_KEY = 'nzrgdn'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

DEBUG = False