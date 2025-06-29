from sqlalchemy import Column, Integer, String
from . import db


class MyModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))

    def __repr__(self):
        return self.name
