import scrapy
from scrapy_splash import SplashRequest

from .helpers.urls import get_urls


class SalariesSpider(scrapy.Spider):
    name = "salaries"
    allowed_domains = ["4programmers.net"]
    # start_urls = ["http://4programmers.net/"]
    start_urls = []

    def __init__(self):
        # at 14.04.2023 there's 376 pages
        self.start_urls = get_urls(1)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args = {'wait': 5 })

    def parse(self, response):
        posts = response.css('.card.card-post')

        for post in posts:

            author = post.xpath(".//*[contains(@class, 'post-author')]/text()").get()

            print("-------------")
            print(author)
            print("-------------")

            yield {
                # 'post': post.css("::text")
                'author': author,
            }
