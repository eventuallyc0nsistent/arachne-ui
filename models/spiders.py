from helpers.database import db, Scrapers, ScrapyStats
from helpers.config_reader import SERVER_NAME

def get_all_spiders():
    return Scrapers.query.all()

def delete_spider(spider_name):
    record =  Scrapers.query.filter_by(name=spider_name).first()
    db.session.delete(record)
    db.session.commit()

def get_spider(spider_name):
    return Scrapers.query.filter_by(name=spider_name).first()

def add_stats(stats):
    db.session.add(stats)
    db.session.commit()

def get_stats(spider_name):
    stats = ScrapyStats.query.filter_by(scrapername=spider_name,
                                        servername=SERVER_NAME).all()
    return stats
