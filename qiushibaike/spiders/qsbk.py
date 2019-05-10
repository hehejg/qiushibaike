# -*- coding: utf-8 -*-
import scrapy

from qiushibaike.items import QiushibaikeItem


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = [f'https://www.qiushibaike.com/8hr/page/{i}/' for i in range(1,11)]
    def parse(self, response):
        item = QiushibaikeItem()

        infos = response.xpath(
            '//*[@id="content"]/div/div[2]/div/ul//div/a[@class="recmd-content"]/text()').extract()
        names = response.xpath(
            '//*[@id="content"]/div/div[2]/div/ul//div/a[@class="recmd-user"]/img/@alt').extract()
        for (info,name)in zip(infos,names):

            item['name'] = name.strip()
            item['info'] = info.strip()
            yield item
