import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Factures(SqlAlchemyBase):
    __tablename__ = 'factures'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    facture = sqlalchemy.Column(sqlalchemy.String)

    items = orm.relationship("Items", back_populates='facture')