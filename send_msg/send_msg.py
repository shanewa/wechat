#coding=utf8
import itchat
#from datetime import time,tzinfo
import time


if __name__ == '__main__':
    # Set the hot login
    itchat.auto_login(hotReload=True)

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.send(u"send the msg to shane\n")
    itchat.run()
