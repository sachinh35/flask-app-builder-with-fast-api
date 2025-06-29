from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


app = Flask(__name__)
app.config.from_object('fab_app.config')

db = SQLA(app)

app_builder = AppBuilder(app, db.session)

# Import views after appbuilder init to avoid circular imports
from . import views
