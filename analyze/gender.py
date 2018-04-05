import itchat

# login wechat
itchat.login()

# get the friend list
friends = itchat.get_friends(update=True)[0:]

# initial the counter
male = female = other = 0

# Go trhouth the list. Notice that the first node is self
# 1: male, 2: female
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# caclate the percete
total = len(friends[1:])

# print 
print u"Male   : %.2f%" % male
print u"Female : %.2f%" % female
print u"Other  : %.2f%" % other
