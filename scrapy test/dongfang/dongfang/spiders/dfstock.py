# -*- coding: utf-8 -*-
import scrapy

from dongfang.items import DongfangItem


class DfstockSpider(scrapy.Spider):
    name = 'dfstock'
    allowed_domains = ['stock.eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/center/gridlist.html#sh_a_board']

    def parse(self, response):
        item=DongfangItem()
        item['code']=response.xpath('//*[@id="table_wrapper-table"]/table/tr[1]/td[3]/a/text()')
        print("code=",item['code'])
        pass
