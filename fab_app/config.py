import os


CSRF_ENABLED = True
SECRET_KEY = os.getenv('SECRET_KEY', 'this_is_a_secret_key_for_dev')


SQLALCHEMY_DATABASE_URI = 'sqlite:///./fab_database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH_TYPE = 1
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'