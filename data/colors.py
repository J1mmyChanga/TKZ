import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Colors(SqlAlchemyBase):
    __tablename__ = 'colors'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    color = sqlalchemy.Column(sqlalchemy.String)

    items = orm.relationship("Items", back_populates='color')