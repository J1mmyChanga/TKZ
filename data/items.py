import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Items(SqlAlchemyBase):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)    
    size = sqlalchemy.Column(sqlalchemy.String, nullable=False)  
    amount_per_meter = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  
    weight = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    color_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("colors.id"), nullable=False)
    facture_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("factures.id"), nullable=False)
    typee_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("types.id"), nullable=False)
    price_package = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    price_no_package = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    color = orm.relationship("Colors", back_populates='items')
    facture = orm.relationship("Factures", back_populates='items')
    typee = orm.relationship("Types", back_populates='items')
    photo = orm.relationship("Photos", back_populates='item')