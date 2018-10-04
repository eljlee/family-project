###### model file - create tables ##### 

from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

##### Model definitions #####

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


class Event(db.Model):
    """Event."""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(128), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    note = db.Column(db.String(64), nullable=True)

    
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "< Event event_id={} title={} location={} date={} note={} >".format(
        																		   self.event_id, 
                                                                                   self.title, 
                                                                                   self.location,
                                                                                   self.date, 
                                                                                   self.note,
                                                                                   )


class Picture(db.Model):
    """Posting picture."""

    __tablename__ = 'pictures'

    pic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    filename = db.Column(db.String(64), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))

    uploader = db.relationship('User')
    event = db.relationship('Event', backref='pictures')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "< Picture pic_id={} filename={} uploader_id={} event_id={} >".format(self.pic_id, 
                                                                                     self.filename, 
                                                                                     self.uploader_id, 
                                                                                     self.event_id
                                                                                     )
