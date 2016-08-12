from app import db
from flask.ext.sqlalchemy import SQLAlchemy

class CurrentId(db.Model):
	__tablename__ = "current_image"

	id = db.Column(db.Integer, primary_key=True)
	curr_id = db.Column(db.Integer)

	def __init__(self, curr_id):
		self.curr_id = curr_id

	def __repr__(self):
		return self.curr_id