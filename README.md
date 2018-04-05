# wechat</br>
This repo is created for WeChat related features.</br>
Author: Shane Wang</br>
Contact: shanewa@qq.com</br>

Platform: Ali Cloud</br>
System: CentOS release 6.5 (Final)</br>
Script: Shell & Python3</br>


1. alarm

This subproject aims to send the alarm messages to the specific WeChat users. 

(a)File lerro_bk</br>

This scenario is sending the message to non-yourself users. It uses the Python library 'itchat'. File lerro_alarm_detect.sh is the alarm detected script which send the message to lerro_alarm.msg when the alarm timer fires. File lerro_alarm_send.py sends message to WeChat user if the lerro_alarm.msg has the message. So lerro_alarm.msg is looks like a message queue.

(b)alarm.cnfg</br>

This is the alarm configuration file. It definites like the following example:</br>

common_test_time="10:10"</br>
common_test="This is a test message." </br>

Key 'common' prefix is used to mark which user should the message sent to. Key 'time' marks the time.</br>

2. auto_reply</br>
This subproject aims to send the messages automatically like QQ.

3. monitor</br>
This subproject will print any incoming or outgoing text messages of your Wechat.

4. robort</br>
This subproject will use the Turing Robort instead of yourself to reply the WeChat messages.

5. withdraw</br>
THis subproject will detecte the withdraw messages and send them to 'filehelper'.



