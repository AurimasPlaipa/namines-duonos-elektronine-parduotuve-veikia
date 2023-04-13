from app import db
from flask_login import UserMixin
from datetime import datetime
from enum import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Purchase(db.Model):
    __tablename__ = "purchases"
    id = db.Column(db.Integer, primary_key=True)
    paid = db.Column(db.Boolean, nullable=False)

    # Relationships
    purchaser_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bread_id = db.Column(db.Integer, db.ForeignKey("breads.id"))
    
# with app.app_context():
    db.create_all()

Base = declarative_base()

class Bread(Base):
    __tablename__ = 'bread'
    id = Column(Integer, primary_key=True)
    # ... kitos modelio laukai

