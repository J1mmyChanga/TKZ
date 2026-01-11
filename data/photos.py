import sqlalchemy
from sqlalchemy import orm
from datetime import datetime

from .db_session import SqlAlchemyBase


class Photos(SqlAlchemyBase):
    __tablename__ = 'photos'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    item_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id'), nullable=False)
    filepath = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Путь на сервере
    thumbnail_path = sqlalchemy.Column(sqlalchemy.String, nullable=True) # Путь к миниатюре

    item = orm.relationship("Items", back_populates='photo')