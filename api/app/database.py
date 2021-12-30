from sqlalchemy import exc

from api.app import db

from dictalchemy import DictableModel


class Base(db.Model, DictableModel):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


def try_commit():
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
