import scrapy
from ..items import ScrapyProjectItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    def parse(self,response):
        items = ScrapyProjectItem()

        all_div_quotes = response.css('div.quote')
        for results in all_div_quotes:
            title = results.css('span.text::text').extract()
            author = results.css ('.author::text').extract()
            tag = results.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
