import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com'
    ]
    def parse(self,response):

        all_div_quotes = response.css('div.quote')
        for results in all_div_quotes:
            title = results.css('span.text::text').extract()
            author = results.css ('.author::text').extract()
            tag = results.css('.tag::text').extract()
            yield {'title' : title,
                   'author' : author,
                   'tags' :tag
                   }
