# pylint:disable=missing-docstring,line-too-long,super-init-not-called

__author__ = 'Afroze Khan'
__modified__ = 'Kiran Koduru'

import json
from scrapy import Spider, Field
from helpers.items import BaseItem

class OpenStatesItem(BaseItem):
    bill_id = Field()
    chamber = Field()
    session = Field()
    subjects = Field()
    action = Field()

class OpenStatesSpider(Spider):
    name = 'openstates'
    allowed_domains = ["openstates.org"]

    def __init__(self, quick_flag=False):
        self.quick_flag = quick_flag
        self.start_urls = []
        self.subjects = ["Energy", "Agriculture and Food",
                         "Budget, Spending, and Taxes", "Commerce",
                         "Environmental", "Government Reform",
                         "Federal, State, and Local Relations",
                         "Transportation", "Technology and Communication",
                         "Municipal and County Issues", "State Agencies",
                         "Resolutions", "Public Services", "Other"]
        self.states = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de',
                       'dc', 'fl', 'ga', 'hi', 'id', 'in', 'ia', 'ks',
                       'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms',
                       'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny',
                       'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'pr', 'ri',
                       'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa',
                       'wv', 'wi', 'wy']

        self.pages_to_scrape = 500
        self.api_key = '7a1c932f618c41039e27d5af035bfdde'

        # search in all subjects
        for subject in self.subjects:
            for page in xrange(1, self.pages_to_scrape):
                self.start_urls.append('http://openstates.org/api/v1/bills/?subject=%s&per_page=1000&page=%d&fields=id,bill_id,created_at,title,session,summary,chamber,subjects,actions,type,sources,state&apikey=%s'%(subject, page, self.api_key))

        # search in all states
        for state in self.states:
            for page in xrange(1, self.pages_to_scrape):
                self.start_urls.append('http://openstates.org/api/v1/bills/?state=%s&per_page=1000&page=%d&fields=id,bill_id,created_at,title,session,summary,chamber,subjects,actions,type,sources,state&apikey=%s'%(state, page, self.api_key))

    def parse(self, response):
        bills = json.loads(response.body_as_unicode())
        for bill in bills:
            item = OpenStatesItem()
            item['id'] = '-'.join(['OS', bill['id']])
            item['bill_id'] = bill['bill_id']

            # we are not storing all the URLs. Just the first one
            item['url'] = bill['sources'][-1]['url']

            item['ekwhere'] = bill['state'].upper()
            item['publishdate'] = bill['created_at']
            item['type'] = ','.join(bill['type'])
            item['chamber'] = bill['chamber']

            if 'subjects' in bill:
                item['subjects'] = ','.join(bill['subjects'])

            # bill['summary'] is present only in some json responses
            if 'summary' in bill:
                item['summary'] = bill['summary']
            item['session'] = bill['session']
            item['title'] = bill['title']
            item['action'] = bill['actions'][-1]['action']
            yield item
