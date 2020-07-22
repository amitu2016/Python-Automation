import ezgmail

#https://developers.google.com/gmail/api/quickstart/python

unread = ezgmail.unread()
summaries = ezgmail.summary(unread)

print(unread[0].messages[0].body)
#print(summaries)