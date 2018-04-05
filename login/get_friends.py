#coding=utf8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import os


# Handle Chinese
reload(sys)
sys.setdefaultencoding('utf8')


itchat.auto_login(enableCmdQR=True, hotReload=True)
user_list=itchat.get_friends(update=True)

for i in user_list:
    if i['RemarkName'] == u'Lerro':        
        _to_user=i['UserName']
        print i
	print _to_user
