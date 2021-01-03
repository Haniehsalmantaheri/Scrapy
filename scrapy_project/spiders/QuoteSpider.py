import scrapy

class QuoteSpider(scrapy.spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    def parse(self,response):
        title = response.css('title').extract
        yield {'titletext' : title}