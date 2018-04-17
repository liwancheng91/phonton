
#python版本： python 3

##项目分为两部分  微信消息和爬取数据

##1. wxpush.py
通过微信 itchat 获取公众号推送消息
手动运行后，使用手机微信扫码登录

##2. phonton
scrapy 爬虫，获取数据
scrapy-redis 将微信公众号获取的 url 动态添加到 start_urls
scrapy-mongodb 存储数据
