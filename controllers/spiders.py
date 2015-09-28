from datetime import datetime
from flask import Blueprint, render_template, send_file, redirect, url_for
from models.spiders import get_all_spiders, delete_spider
from helpers.scrapy_util import start_crawler, start_logger
from helpers.config_reader import GLOBAL_PATH

spiders_bp = Blueprint('spiders_bp', __name__, template_folder='templates')

@spiders_bp.route('/')
def list_spiders():
    spiders = get_all_spiders()
    return render_template('list-spiders.html', spiders=spiders)

@spiders_bp.route('/run/<spider_name>/')
def run_spider(spider_name):
    spiders = get_all_spiders()
    start_logger(spider_name)
    start_crawler(spider_name)
    return render_template('list-spiders.html',
                           spiders=spiders)

@spiders_bp.route('/log/<spider_name>/')
def read_log(spider_name):
    filename = datetime.now().strftime("%Y-%m-%d." + spider_name + ".log")
    with open(GLOBAL_PATH + 'logs/' + filename) as logf:
        data = logf.read()
    return render_template('read-log.html', data=data)

@spiders_bp.route('/<file_type>/<spider_name>')
def export_json(file_type, spider_name):
    file_ = '%sexports/%s/%s.%s' % (GLOBAL_PATH, file_type, spider_name, file_type)
    return send_file(file_, as_attachment=True)

@spiders_bp.route('/delete/<spider_name>')
def spider_del(spider_name):
    delete_spider(spider_name)
    return redirect(url_for('spiders_bp.list_spiders'))
