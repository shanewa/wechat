# wechat</br>
This repo is created for WeChat related features.</br>
Author: Shane Wang</br>
Contact: shanewa@qq.com</br>

Platform: Ali Cloud
System: CentOS release 6.5 (Final)# wechat
This repo is created for WeChat related features.
Author: Shane Wang
Contact: shanewa@qq.com

Platform: Ali Cloud
System: CentOS release 6.5 (Final)
Script: Shell & Python3


1. alarm

This subproject aims to send the alarm messages to the specific WeChat users. 

(a)File lerro_bk
This scenario is sending the message to non-yourself users. It uses the Python library 'itchat'. File lerro_alarm_detect.sh is the alarm detected script which send the message to lerro_alarm.msg when the alarm timer fires. File lerro_alarm_send.py sends message to WeChat user if the lerro_alarm.msg has the message. So lerro_alarm.msg is looks like a message queue.
(b)alarm.cnfg
This is the alarm configuration file. It definites like the following example:

common_test_time="10:10"
common_test="This is a test message." 

Key 'common' prefix is used to mark which user should the message sent to. Key 'time' marks the time.

2. auto_reply
This subproject aims to send the messages automatically like QQ.

3. monitor
This subproject will print any incoming or outgoing text messages of your Wechat.

4. robort
This subproject will use the Turing Robort instead of yourself to reply the WeChat messages.

5. withdraw
THis subproject will detecte the withdraw messages and send them to 'filehelper'.




Script: Shell & Python3


1. alarm

This subproject aims to send the alarm messages to the specific WeChat users. 

(a)File lerro_bk
This scenario is sending the message to non-yourself users. It uses the Python library 'itchat'. File lerro_alarm_detect.sh is the alarm detected script which send the message to lerro_alarm.msg when the alarm timer fires. File lerro_alarm_send.py sends message to WeChat user if the lerro_alarm.msg has the message. So lerro_alarm.msg is looks like a message queue.
(b)alarm.cnfg
This is the alarm configuration file. It definites like the following example:

common_test_time="10:10"
common_test="This is a test message." 

Key 'common' prefix is used to mark which user should the message sent to. Key 'time' marks the time.

2. auto_reply
This subproject aims to send the messages automatically like QQ.

3. monitor
This subproject will print any incoming or outgoing text messages of your Wechat.

4. robort
This subproject will use the Turing Robort instead of yourself to reply the WeChat messages.

5. withdraw
THis subproject will detecte the withdraw messages and send them to 'filehelper'.


