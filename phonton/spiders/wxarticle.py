# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from urllib.parse import urlparse, parse_qs

class WxarticleSpider(RedisCrawlSpider):
    name = 'wxarticle'
    redis_key = 'wxarticle:start_urls'

    def parse(self, response):

        param_dict = parse_qs(urlparse(response.url).query)
        user_biz = param_dict['__biz'][0]
        user_name = response.xpath('//div[@class="rich_media_meta_list"]/a/text()').extract_first().strip()
        user_id = response.xpath('//*[@id="js_profile_qrcode"]/div/p[1]/span/text()').extract_first()
        title = response.xpath('//h2/text()').extract_first().strip()
        date = response.xpath('//em[@id="post-date"]/text()').extract_first()
        content_list = response.xpath('//*[@id="js_content"]/p/text()').extract()
        content = '\n'.join(content_list)

        return {
            'user_biz': user_biz,
            'user_name': user_name,
            'user_id': user_id,
            'title': title,
            'date': date,
            'content': content,
            'origin_url': response.url,
        }