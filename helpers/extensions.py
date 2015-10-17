from scrapy import signals
from models.spiders import add_stats, get_spider
from helpers.database import ScrapyStats, db
from helpers.config_reader import SERVER_NAME


class StatsCollectorExt(object):
    """
    Collect stats for each spider in DB
    """

    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        """
        Assign methods to run for the spider signals
        """
        ext = cls(crawler.stats)
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_opened(self, spider):
        spider_ = get_spider(spider.name)
        spider_.is_running = 1
        db.session.commit()

    def spider_closed(self, spider, reason):
        """
        When the spider closes then
        store the stats(start time, end time, items scraped,
        pages crawled) into the database for each scraper.
        """
        items_scraped_count = 0
        start_time = self.stats._stats['start_time']
        finish_time = self.stats._stats['finish_time']
        if 'item_scraped_count' in self.stats._stats:
            items_scraped_count = self.stats._stats['item_scraped_count']
        spider_name = spider.name
        pages_crawled_count = self.stats._stats[
            'downloader/request_method_count/GET']

        # add the scrapy stats to DB
        stats = ScrapyStats(scrapername=spider_name,
                            start_time=start_time,
                            finish_time=finish_time,
                            items_scraped=items_scraped_count,
                            pages_crawled=pages_crawled_count,
                            servername=SERVER_NAME)
        add_stats(stats)

        # update column to db when it stops running
        spider_ = get_spider(spider_name)
        spider_.is_running = 0
        print spider_
        db.session.commit()
