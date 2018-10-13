##### server file ######
# import ipdb; ipdb.set_trace()

#################
#### imports ####
#################
import os
from flask import Flask, render_template, redirect, request, flash, session, jsonify, url_for

from flask_debugtoolbar import DebugToolbarExtension
from werkzeug import secure_filename
import datetime
from model import User, Event, Picture, connect_to_db, db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'EVENTFULL'


################
#### routes ####
################

# NEED TO BE LOGGED IN BEFORE BEING ABLE TO DO ANYTHING?

@app.route('/')
def homepage():
    """Show homepage."""
    # if 'user_id' in session:
    #     return redirect('/user')

    # else:
    return render_template('homepage.html')