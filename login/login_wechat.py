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


# Set the hot login
itchat.auto_login(enableCmdQR=True, hotReload=True)
#itchat.auto_login(hotReload=True)
itchat.send(u'Login Wechat Successfully.', u'filehelper')

itchat.run()

