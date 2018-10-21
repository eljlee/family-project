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

        return "< Picture pic_id={} filename={} uploader_id={} event_id={} >".format(
                                                                                     self.pic_id, 
                                                                                     self.filename, 
                                                                                     self.uploader_id, 
                                                                                     self.event_id
                                                                                     )




class Family_Relation(db.Model):
    """Who's related to who."""

    __tablename__ = 'relations'

    relation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    relation_1_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    relation_2_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "< relation_1_id={} relation_2_id={} >".format(
                                                           self.relation_1_id, 
                                                           self.relation_2_id
                                                           )



#########################################################################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///family'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."



