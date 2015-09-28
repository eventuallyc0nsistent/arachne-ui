import os
import sys
import logging
from flask import Flask, session, render_template
from datetime import timedelta, datetime
from logging.handlers import RotatingFileHandler, SMTPHandler
from helpers.config_reader import (FLASK_DEBUG, GLOBAL_PATH, SECRET_KEY,
                                   SUPPORT_EMAIL, SERVER_NAME, SMTP_HOST,
                                   SMTP_TO_ADDR, SMTP_USERNAME, MANDRILL_KEY)

# spider folder
UPLOAD_FOLDER = GLOBAL_PATH + 'spiders'

# Flask app
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=60)
app.debug = FLASK_DEBUG
app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:////arachne.db'

#Rotating log to a file with the current date - max size 1 MB
if not app.debug:
    today = datetime.now()

    # -------------
    # file logger
    # -------------
    file_handler = RotatingFileHandler(
        filename='%slogs/%s-%s-%s.log'
        %(GLOBAL_PATH, today.year, today.month, today.day),
        maxBytes=1024 * 1024 * 1000)
    file_formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    # -------------
    # SMTP logger
    # -------------
    mail_handler = SMTPHandler(
                        (SMTP_HOST, 587), SUPPORT_EMAIL, [SMTP_TO_ADDR],
                        '[%s] has a problem'
                        %(SERVER_NAME),
                        (SMTP_USERNAME, MANDRILL_KEY))
    mail_formatter = logging.Formatter('''
                    Message type:       %(levelname)s
                    Location:           %(pathname)s:%(lineno)d
                    Module:             %(module)s
                    Function:           %(funcName)s
                    Time:               %(asctime)s

                    Message:

                    %(message)s
                ''')
    mail_handler.setFormatter(mail_formatter)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# route controllers
import controllers
