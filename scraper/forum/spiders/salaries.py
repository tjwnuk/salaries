import scrapy
from scrapy import Selector
import time
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .helpers.urls import get_urls

def get_driver():
    time.sleep(3)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
   
    driver = webdriver.Remote(
    command_executor='http://browser:3000/webdriver',
        options=chrome_options,
    )
    return driver

class SalariesSpider(scrapy.Spider):
    name = "salaries"
    allowed_domains = ["4programmers.net"]
    # start_urls = ["http://4programmers.net/"]
    start_urls = []

    def __init__(self):
        # at 14.04.2023 there's 376 pages
        # at 26.04.2023 there's 377 pages
        self.start_urls = get_urls(377)
        self.driver = get_driver()

        # reset after every 200 posts
        # in order to do that you must create the counter
        self.pages_counter = 0

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        '''
        parse method processess all the forum posts
        '''
        
        # reset the connection every 10 pages
        if (self.pages_counter % 10 == 0):
            self.driver = get_driver()
        self.pages_counter += 1

        self.driver.get(response.url)

        sel = Selector(text=self.driver.page_source)
        
        time.sleep(1)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'post-author'))
        )

        posts = sel.xpath("//*[contains(@class, 'card-post')]")


        for post in posts:

            author = post.xpath(".//*[@class='mb-0 post-author']/*/text()").get()
            date = post.xpath(".//time/text()").get()
            post_id = post.xpath(".//@id").get()
            url = post.xpath(".//time/../@href").get()
            vote_count = post.xpath(".//*[contains(@class, 'vote-count')]/text()").get()
            post_content = post.xpath(".//*[contains(@class, 'post-content')]").get()

            yield {
                'author': author,
                'date': date,
                'post_id': post_id,
                'url': url,
                'vote_count': vote_count,
                'post_content': post_content,
            }

    def closed(self, reason):
        self.driver.quit()