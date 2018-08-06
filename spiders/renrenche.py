# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapyrenrenche.items import renrencheItem


class RenrencheSpider(CrawlSpider):
    name = 'renrenche'
    allowed_domains = ['www.renrenche.com']
    start_urls = ['https://www.renrenche.com/nn/ershouche/']

    rules = (
        Rule(LinkExtractor(allow=r'car\/.*', restrict_xpaths='//ul[@class="row-fluid list-row js-car-list"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="pagination js-pagination"]//a[@rrc-event-name="switchright"]'))
    )

    def parse_item(self, response):
        item = renrencheItem()
        item['title'] = response.xpath('//div[@class="title"]/h1/text()').extract_first()
        item['price'] = response.xpath('//div[@class="list price-list"]/p/text()').extract_first()
        item['new_car_price'] = response.xpath('//*[@id="basic"]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/span/text()').extract_first()
        item['deposit'] = response.xpath('//div[@class="middle-content"]//div[@class="list payment-list"]//p[2]/text()').extract_first()
        item['payment'] = response.xpath('//div[@class="middle-content"]//div[@class="list payment-list"]//p[3]/text()').extract_first()
        item['service_pay'] = response.xpath('//*[@id="js-service-wrapper"]/div[1]/p[2]/text()').extract_first()
        item['city'] = response.xpath('//*[@id="car-licensed"]/text()').extract_first()
        item['car_summary'] = response.xpath('//li[@class="span5 car-fluid-standard"]/div/p[1]/strong/text()').extract_first()
        item['gearbox'] = response.xpath('//*[@id="basic"]/div[2]/div[2]/div[1]/div[4]/ul/li[5]/div/p[1]/strong/text()').extract_first()
        item['transfer_record'] = response.xpath('//li[@class="car-transfer"]/p[1]/strong/text()').extract_first()
        item['url'] = response.url





        yield item
