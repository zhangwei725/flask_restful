from apps.ext import db


class Banner(db.Model):
    bid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    path = db.Column(db.String(100), nullable=False)
