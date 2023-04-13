from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from enum import Enum
from datetime import datetime
from app import db

class Bread(db.Model):
    __tablename__ = "breads"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    # Parent
    # purchase = relationship("Purchase", back_populates="bread")

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price