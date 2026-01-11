import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Types(SqlAlchemyBase):
    __tablename__ = 'types'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    typee = sqlalchemy.Column(sqlalchemy.String)

    items = orm.relationship("Items", back_populates='typee')