import string
import datetime

def getUser(line):
	#split = line.split(" :",2)
	#tags = split[0]
	#print(tags)
	#users = split[1:2]
	#users = " :".join(users)
	#print(users)
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	#split = line.split(" :",2)
	#tags = split[0]
	#print("Tags")
	#print(tags)
	#users = split[1:2]
	#users = " :".join(users)
	#print("Users")
	#print(users)
	separate = line.split(":", 2)
	#print("Seperate")
	#print(separate)
	#print(separate[2])
	message = separate[2]
	#print("getMessage Debug" + message)
	#print ("Got Message at " + getTime)
	return message
	#return tags
def getTime():
	now = datetime.datetime.now()
	hour = str(now.hour)
	minute = str(now.minute)
	second = str(now.second)
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	result = (month + " " + day + " " + year + ", " + hour + ":" + minute + ":" + second)
	return result
