from helpers.database import db, Scrapers


def get_all_spiders():
    return Scrapers.query.all()

def get_spidercls_name(spider_name):
    return Scrapers.query.filter_by(name=spider_name).first().spidercls

def delete_spider(spider_name):
    record =  Scrapers.query.filter_by(name=spider_name).first()
    db.session.delete(record)
    db.session.commit()
