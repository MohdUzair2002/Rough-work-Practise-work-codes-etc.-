import scrapy


class SpidernSpider(scrapy.Spider):
    name = 'spidern'
    allowed_domains = ['www.xyz.com']
    start_urls = ['http://www.xyz.com/']

    def parse(self, response):
        pass
