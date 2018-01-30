# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from cordisnews.items import CordisnewsItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['cordis.europa.eu']
    start_urls = ['http://cordis.europa.eu/news/rcn/%d_en.html' %(n) for n in range(128792, 128793)]

    def parse(self, response):

        l = ItemLoader(item=CordisnewsItem(), response=response)
        l.add_xpath('Title', '//*[@id="dynamiccontent"]/div[1]/h1/text()')
        l.add_xpath('Teaser', '//*[@id="dynamiccontent"]/div[2]/div[1]/div[1]/text()')
        l.add_xpath('Article', '//*[@id="dynamiccontent"]/div[2]/div[1]/div[3]/text()')
        l.add_xpath('Subject', '/*[@id="subjects"]/a/text()')
        l.add_xpath('Countries', '//*[@id="Country"]/div[2]/ul/li/text()')

        return l.load_item()
