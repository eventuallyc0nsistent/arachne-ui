from app import app
from flask.ext.sqlalchemy import SQLAlchemy
from helpers.config_reader import GLOBAL_PATH, DBNAME

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + GLOBAL_PATH + DBNAME + '.db'
db = SQLAlchemy(app)

class Scrapers(db.Model):
    __tablename__ = 'scrapers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    spidercls = db.Column(db.String(200))

    def __init__(self, name, description, spidercls):
        self.name = name
        self.description = description
        self.spidercls = spidercls

    def __repr__(self):
        return '<Scrapers : id=%r, name=%s, description=%s, spidercls=%s>'\
               % (self.id, self.name, self.description, self.spidercls)
