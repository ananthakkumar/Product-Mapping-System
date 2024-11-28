from . import db

class ProductMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(200), unique=True, nullable=False)
    standardized_name = db.Column(db.String(200), nullable=False)
