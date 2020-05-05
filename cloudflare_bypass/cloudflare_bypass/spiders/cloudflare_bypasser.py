# -*- coding: utf-8 -*-
from scrapy import Spider, Request

import cfscrape

class CloudflareBypasserSpider(Spider):
    name = 'cloudflare_bypasser'

    start_urls = []

    def __init__(self, url, file_path, *args, **kwargs):
        self.start_urls = [url]
        self.path = file_path
        self.scraper = cfscrape.create_scraper()

    def start_requests(self):
        html = self.scraper.get(self.start_urls[0]).content
        with open(self.path, 'wb') as f_in:
            f_in.write(html)

        return []
