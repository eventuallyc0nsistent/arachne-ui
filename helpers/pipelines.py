from scrapy import signals
from helpers.config_reader import GLOBAL_PATH
from scrapy.contrib.exporter import CsvItemExporter, JsonItemExporter

class ExportCSV(object):

    """
    Exporting to export/csv/spider-name.csv file
    """

    def __init__(self):
        self.files = {}
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file_to_save = open(GLOBAL_PATH+'exports/csv/%s.csv' % spider.name, 'w+b')
        self.files[spider] = file_to_save
        self.exporter = CsvItemExporter(file_to_save)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file_to_save = self.files.pop(spider)
        file_to_save.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ExportJSON(object):

    """
    Exporting to export/json/spider-name.json file
    """

    def __init__(self):
        self.files = {}
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file_to_save = open(GLOBAL_PATH+'exports/json/%s.json' % spider.name, 'w+b')
        self.files[spider] = file_to_save
        self.exporter = JsonItemExporter(file_to_save)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file_to_save = self.files.pop(spider)
        file_to_save.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
