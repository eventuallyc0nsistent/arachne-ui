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
    is_running = db.Column(db.Boolean)
    time_to_run = db.Column(db.DateTime)

    def __init__(self, name, description, spidercls, is_running, time_to_run):
        self.name = name
        self.description = description
        self.spidercls = spidercls
        self.is_running = is_running
        self.time_to_run = time_to_run

    def __repr__(self):
        return '<Scrapers : id=%r, name=%s, description=%s, spidercls=%s, is_running=%d, time_to_run=%s>'\
               % (self.id, self.name, self.description, self.spidercls, self.is_running, self.time_to_run)

class ScrapyStats(db.Model):
    __tablename__ = 'scrapystats'

    id = db.Column(db.Integer, primary_key=True)
    scrapername = db.Column(db.String(600))
    start_time = db.Column(db.DateTime)
    finish_time = db.Column(db.DateTime)
    items_scraped = db.Column(db.Integer)
    pages_crawled = db.Column(db.Integer)
    servername = db.Column(db.String(300))

    def __init__(self, id=None, scrapername=None, start_time=None, finish_time=None, items_scraped=None, pages_crawled=None, servername=None):
        self.id = id
        self.scrapername = scrapername
        self.start_time = start_time
        self.finish_time = finish_time
        self.items_scraped = items_scraped
        self.pages_crawled = pages_crawled
        self.servername = servername

    def __repr__(self):
        return "<ScrapyStats: id='%r', scrapername='%s', start_time='%s', finish_time='%s', items_scraped='%r', pages_crawled='%r', servername='%s'>" % (self.id, self.scrapername, self.start_time, self.finish_time, self.items_scraped, self.pages_crawled, self.servername)
