import scrapy

class JobSpider(scrapy.Spider):
    name = "job_spider"
    start_urls = ["google.com"]