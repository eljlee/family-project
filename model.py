from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()


class User(db.Model):
	"""Users."""

	__tablename__= "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)
	nickname = db.Column(db.String(64), nullable=True)
	birthday = db.Column(db.DateTime, nullable=False)


	def __repr__(self):
        """Provide helpful representation when printed"""

        return "< User user_id={} f_name={} l_name={} birthday={} >".format(
        																	self.user_id, 
        																	self.first_name, 
        																	self.last_name, 
        																	self.birthday
        																	)

