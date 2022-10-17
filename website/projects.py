from flask import Blueprint, render_template, request
from flask_login import current_user
from .models import Temperature
from . import db
import flask
import serial

projects = Blueprint('projects', __name__)

"""serialcomm = serial.Serial('COM8', 115200)
serialcomm.timeout = 1
def ledOn():
    serialcomm.write(str('on')).encode()

def ledOff():
    serialcomm.write(str('off')).encode()
"""
@projects.route('/projects/1', methods=['GET', 'POST'])
def proj1():
    """if request.method == 'POST':
        if 'on' in request.form.to_dict():
            ledOn()
        elif 'off' in request.form.to_dict():
            ledOff()"""
    return render_template('proj1.html', user=current_user, temperature = Temperature.query.get(0))

@projects.route('/projects/1/push', methods=['GET','POST'])
def post():
    message = flask.request.data.decode('UTF-8')
    temp = Temperature.query.get(0)

    temp.temperature = message
    db.session.commit()

    return flask.Response(status=204)

def stream():
    temp = Temperature.query.get(0)

@projects.route('/projects/1/stream')
def stream():
    return flask.Response()