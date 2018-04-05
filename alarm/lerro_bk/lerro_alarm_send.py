#coding=utf8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import os

# To user list: Lerro Li
# _to_user=u'@b8fd59ed2b9bd992fd171b0677c279b971aa49f70f0b3885dee185e02ef7c7d8'

# Message local queue file
queue_file=r'/home/shanewa/wechat/alarm/lerro_bk/lerro_alarm.msg'

# Handle Chinese
reload(sys)
sys.setdefaultencoding('utf8')

# Set the hot login
itchat.auto_login(enableCmdQR=True, hotReload=True)

# user = itchat.search_friends(name=r'Lerro')[0]
user_list=itchat.get_friends(update=True)
for i in user_list:
    if i['RemarkName'] == u'Lerro':        
        _to_user=i['UserName']
	print _to_user

# Start to monitor the alarm message 
while 1:
    with open(queue_file, 'r') as file_read:
        # Read the file
        all_the_text = file_read.read()        
        # Send the message and clear the file
        if all_the_text.strip() != '':
            # itchat.send_msg(all_the_text)        
            itchat.send_msg(all_the_text, _to_user)        
            # user.send(all_the_text)
            with open(queue_file, 'w') as file_write:
                file_write.truncate()
	else:
	    # print "File is none. So so msg to be sent."
	    time.sleep(10)
