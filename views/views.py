import random
from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import time
from sqlalchemy import Column, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

basedir = os.path.abspath(os.path.dirname(__file__))

application  = Flask(__name__)
application.config.from_object('config')
application.config.from_pyfile('config.py')
application.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@application.route("/")
def main():
    return render_template('/index.jade')

@application.route("/about")
def about():
    return render_template('/about.jade')

@application.route("/contact")
def contact():
    return render_template('/contact.jade')
