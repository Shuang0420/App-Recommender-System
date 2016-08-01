# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from appstore.items import AppstoreItem
from scrapy_splash import SplashRequest
from scrapy_redis.spiders import RedisSpider


# class HuaweiSpider(scrapy.Spider):
class HuaweiSpider(RedisSpider):
    name = "huawei"
    redis_key = 'huawei:start_urls'

    allowed_domains = ["huawei.com"]

    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.html',
                                args=splash_args)

    def parse(self, response):
        rule = re.compile('http://appstore.huawei.com:80/app/C[0-9]{8}')
        hrefs = rule.findall(response.body)
        # print hrefs
        page = Selector(response)
        #hrefs = page.xpath('//h4[@class="title"]/a/@href')
        if not hrefs:
            return
        for href in hrefs:
            #url = href.extract()
            yield scrapy.Request(href, callback=self.parse_item)
        # find next page
        nextpage = page.xpath(
            '//div[@class="page-ctrl ctrl-app"]/a/em[@class="arrow-grey-rt"]/../@href').extract_first()
        if nextpage:
            yield scrapy.Request(nextpage, callback=self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse_item(self, response):
        # print response.url
        page = Selector(response)
        item = AppstoreItem()

        item['title'] = page.xpath(
            '//ul[@class="app-info-ul nofloat"]/li/p/span[@class="title"]/text()').extract_first().encode('utf-8')
        item['url'] = response.url
        appid = re.match(r'http://.*/(.*)', item['url']).group(1)
        item['app_id'] = appid
        item['intro'] = page.xpath(
            '//meta[@name="description"]/@content').extract_first().encode('utf-8')
        item['thumbnail_url'] = page.xpath(
            '//ul[@class="app-info-ul nofloat"]/li[@class="img"]/img[@class="app-ico"]/@lazyload').extract_first().encode('utf-8')
        item['developer'] = page.xpath(
            '//ul[@class="app-info-ul nofloat"]/li[@class="ul-li-detail"]/span/@title').extract_first().encode('utf-8')
        spans = page.xpath(
            '//ul[@class="app-info-ul nofloat"]/li/p/span/@class').extract()
        for s in spans:
            if s.startswith('score'):
                item['score'] = s.split('_')[1].encode('utf-8')
                break
        divs = page.xpath('//div[@class="open-info"]')
        recomm = ""

        for div in divs:
            url = div.xpath('./p[@class="name"]/a/@href').extract_first()
            recommended_appid = re.match(r'http://.*/(.*)', url).group(1)
            name = div.xpath(
                './p[@class="name"]/a/text()').extract_first().encode('utf-8')
            recomm += "{0}:{1},".format(recommended_appid, name)
        item['recommended'] = recomm
        yield item
