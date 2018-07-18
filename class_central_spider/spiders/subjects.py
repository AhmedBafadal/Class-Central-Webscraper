# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.http import Request


class SubjectsSpider(Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ['http://class-central.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath(
                '//*[contains(@title, "' + self.subject + '")]/@href').extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info('Scraping all subejcts.')
            subjects = response.xpath(
                '//*[@class="show-all-subjects view-all-courses"]/@href').extract()
            for subject in subjects:
                yield Request(response.urljoin(subject_url), callback=self.parse_subject)

    def parse_subject(self, response):
        subject_name = response.xpath('//title/texxt()').extract_first()
        subject_name = subject_name.split(' | ')[0]
