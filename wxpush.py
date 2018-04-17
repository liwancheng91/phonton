#coding: utf-8

import itchat
from itchat.content import *
import xml.etree.ElementTree as ET
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

@itchat.msg_register(SHARING, isMpChat=True)
def text_reply(msg):
    if msg.type == 'Sharing':
        appmsg = ET.fromstring(msg.content).find('appmsg')
        if appmsg is not None:
            urls = []
            if appmsg.find('url') is not None:
                urls.append(appmsg.find('url').text)
            for item in appmsg.findall('.//item'):
                if item.find('./url') is not None:
                    urls.append(item.find('./url').text)
            r.lpush("wxarticle:start_urls", *urls)

itchat.auto_login(hotReload=True)
itchat.run(True)