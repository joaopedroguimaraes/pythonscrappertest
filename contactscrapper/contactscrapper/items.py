from scrapy import Item, Field


class ContactItem(Item):
    url = Field()
    logo_url = Field()
    phones = Field()
