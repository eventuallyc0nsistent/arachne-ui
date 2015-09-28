import logging
from datetime import datetime
from scrapy.log import ScrapyFileLogObserver
from scrapy.utils.misc import load_object
from twisted.python import logfile, log as tlog
from flask import Blueprint, render_template, send_file
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from helpers.spider_mapping import SPIDERS
from helpers.config_reader import GLOBAL_PATH

spiders_bp = Blueprint('spiders_bp', __name__, template_folder='templates')

def create_crawler_object(spider_, settings_):
    """
    For the given scrapy settings and spider create a crawler object

    Args:
        spider_ (class obj): The scrapy spider class object
        settings_(class obj): The scrapy settings class object

    Returns:
        A scrapy crawler class object
    """
    crwlr = Crawler(settings_)
    crwlr.configure()
    crwlr.crawl(spider_)
    return crwlr


def get_spider_settings():
    """
    For the given spider_pipelines(dict) create a scrapy Settings object with
    the common settings for each spider/crawler.

    Returns:
        Scrapy settings class instance
    """
    settings = Settings()
    pipelines = {
        'helpers.pipelines.ExportCSV': 100,
        'helpers.pipelines.ExportJSON': 100,
    }
    settings.set("TELNETCONSOLE_PORT", None)
    settings.set("DOWNLOAD_TIMEOUT", 800)
    settings.set("ITEM_PIPELINES", pipelines)
    settings.set("USER_AGENT", "Kiran Koduru (+http://github.com/kirankoduru)")
    return settings

def start_crawler(spider_name):
    spidercls_name = SPIDERS[spider_name]['spidercls']
    spider_location = 'spiders'+ '.'  + \
                      '.'.join([spidercls_name, spidercls_name])
    spider = load_object(spider_location)
    settings = get_spider_settings()
    crawler = create_crawler_object(spider(), settings)
    crawler.start()

def start_logger(spider_name):
    filename = datetime.now().strftime("%Y-%m-%d." + spider_name + ".log")
    logfile_ = logfile.LogFile(filename,
                               GLOBAL_PATH + '/logs')
    logger = ScrapyFileLogObserver(logfile_, logging.DEBUG)
    tlog.addObserver(logger.emit)

# URLs
@spiders_bp.route('/')
def list_spiders():
    return render_template('list-spiders.html', spiders=SPIDERS)

@spiders_bp.route('/run/<spider_name>/')
def run_spider(spider_name):
    if spider_name in SPIDERS:
        start_logger(spider_name)
        start_crawler(spider_name)
    return render_template('list-spiders.html',
                           spiders=SPIDERS,
                           running=spider_name)

@spiders_bp.route('/log/<spider_name>/')
def read_log(spider_name):
    if spider_name in SPIDERS:
        filename = datetime.now().strftime("%Y-%m-%d." + spider_name + ".log")
        with open(GLOBAL_PATH + 'logs/' + filename) as logf:
            data = logf.read()
    return render_template('read-log.html', data=data)

@spiders_bp.route('/<file_type>/<spider_name>')
def export_json(file_type, spider_name):
    if spider_name in SPIDERS:
        file_ = '%sexports/%s/%s.%s' % (GLOBAL_PATH, file_type, spider_name, file_type)
        return send_file(file_, as_attachment=True)
