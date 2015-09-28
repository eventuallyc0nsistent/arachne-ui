import logging
from datetime import datetime
from scrapy.log import ScrapyFileLogObserver
from scrapy.utils.misc import load_object
from twisted.python import logfile, log as tlog
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from models.spiders import get_spidercls_name
from helpers.config_reader import GLOBAL_PATH

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
    spidercls_name = get_spidercls_name(spider_name)
    spider_location = 'spiders'+ '.'  + \
                      '.'.join([spidercls_name, spidercls_name])
    spider = load_object(spider_location)
    settings = get_spider_settings()
    crawler = create_crawler_object(spider(), settings)
    crawler.start()

def start_logger(spider_name):

    # TODO: FIX read for files like spidername.log.1
    filename = datetime.now().strftime("%Y-%m-%d." + spider_name + ".log")
    logfile_ = logfile.LogFile(filename,
                               GLOBAL_PATH + '/logs')
    logger = ScrapyFileLogObserver(logfile_, logging.DEBUG)
    tlog.addObserver(logger.emit)
