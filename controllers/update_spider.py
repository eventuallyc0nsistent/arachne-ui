from flask import Blueprint, render_template, redirect, request, url_for
from helpers.database import db, Scrapers
from models.spiders import get_spider

ALLOWED_EXTENSIONS = set(['py'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

updatespider_bp = Blueprint('updatespider_bp', __name__, template_folder='templates')

@updatespider_bp.route('/add-spider-form/')
def add_spider_form():
    return render_template('add-spider.html', update=False, spider={})

@updatespider_bp.route('/update-spider-form/<spider_name>')
def update_spider_form(spider_name):
    spider = get_spider(spider_name)
    return render_template('add-spider.html', update=True, spider=spider)

@updatespider_bp.route('/add-spider-post/', methods=['POST'])
def add_spider_post():
    """
    Upload file to spiders/ directory and save the mapping
    in the spider_mapping file
    """
    spider_name = request.form['spider-name']
    spider_desc = request.form['spider-desc']
    spider_cls = request.form['spider-cls']

    # add spider to db
    new_spider = Scrapers(name=spider_name, description=spider_desc,
                          spidercls=spider_cls)
    db.session.add(new_spider)
    db.session.commit()

    return redirect(url_for('spiders_bp.list_spiders'))

@updatespider_bp.route('/update-spider-post/', methods=['POST'])
def update_spider_post():
    """
    Upload file to spiders/ directory and save the mapping
    in the spider_mapping file
    """
    spider_name = request.form['spider-name']
    spider_desc = request.form['spider-desc']
    spider_cls = request.form['spider-cls']

    # add spider to db
    spider = get_spider(spider_name)
    spider.name = spider_name
    spider.description = spider_desc
    spider.spidercls = spider_cls
    db.session.commit()

    return redirect(url_for('spiders_bp.list_spiders'))
