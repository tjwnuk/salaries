import scrapy


class SalariesSpider(scrapy.Spider):
    name = "salaries"
    allowed_domains = ["4programmers.net"]
    start_urls = ["http://4programmers.net/"]

    def parse(self, response):
        pass
