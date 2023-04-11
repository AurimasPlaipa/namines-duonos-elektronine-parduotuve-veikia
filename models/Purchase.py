from app import db
from flask_login import UserMixin

class Purchase(db.Model):
    __tablename__ = "purchases"
    id = db.Column(db.Integer, primary_key=True)
    paid = db.Column(db.Boolean, nullable=False)

    # Relationships
    purchaser_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # purchaser = relationship("User", back_populates="purchases")

    # bread_id = db.Column(db.Integer, db.ForeignKey("breads.id"))
    # bread = relationship("Item", back_populates="purchase")

with app.app_context():
    db.create_all()