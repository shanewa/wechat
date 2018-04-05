#coding=utf8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import requests, json
import aiml
import os


reload(sys)
sys.setdefaultencoding( "utf-8" )

# When recieve the following msg types, trigger the auto replying.
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True, isMpChat=True, isGroupChat=True)
def text_reply(msg):
    print msg['Content']

# Main
if __name__ == '__main__':
    # Set the hot login
    itchat.auto_login(enableCmdQR=True, hotReload=True)

    # Get your own UserName
    #myUserName = itchat.get_friends(update=True)[0]["UserName"]
    #print myUserName

    itchat.run()
