# pylint:disable=missing-docstring,invalid-name
from scrapy.item import Field, Item

class BaseItem(Item):
    id = Field()
    submittedby = Field()
    title = Field()
    url = Field()
    type = Field()
    ekwhere = Field()
    summary = Field()
    publishdate = Field()
    sourceid = Field()
    subsector = Field()
    dashboard = Field()
