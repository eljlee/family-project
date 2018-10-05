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