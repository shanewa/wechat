# -*- coding: utf-8 -*-
import requests, json
import itchat, aiml, os
from itchat.content import *

@itchat.msg_register([TEXT, MAP, PICTURE, CARD, SHARING], isFriendChat=True)
def text_reply(msg):
    # cont = alice.respond(msg['Text'])
    cont = requests.get('http://www.tuling123.com/openapi/api?key=(replace_your_key)&info=%s' % msg['Content']).content
    m = json.loads(cont)
    itchat.send(m['text'], msg['FromUserName'])
    if m['code'] == 200000:
        itchat.send(m['url'], msg['FromUserName'])
    if m['code'] == 302000:
        itchat.send(m['list'], msg['FromUserName'])
    if m['code'] == 308000:
        itchat.send(m['list'], msg['FromUserName'])

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()
