import datetime

async def sendMessage(message,client,platform,sentMessage,CHANNEL=None):
	#check if default function value work (def func(perm=none))
	#for twitch, message is message, client is s, and sentmessage is the message to send
	#print (platform)
	if platform == "discord":
		msg = await client.send_message(message.channel, sentMessage)
	elif platform == "twitch":
		import Socket
		from Settings import CHANNEL
		s = client
		#Socket.sendMessage(client,sentMessage)
		#messageTemp = "PRIVMSG #" + CHANNEL + " :" + sentMessage
		messageTemp = "PRIVMSG #" + Socket.usedChannel + " :" + sentMessage
		messageSend = messageTemp + "\r\n"
		s.send(messageSend.encode('utf-8'))
		print(getTime() + " Hayleethebot: " + messageTemp)
def getTime():
	now = datetime.datetime.now()
	hour = str(now.hour)
	minute = str(now.minute)
	second = str(now.second)
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	time = (month + " " + day + " " + year + ", " + hour + ":" + minute + ":" + second)
	return time
def getPartTime(toGet):
	valid = ["hour","minute","second","year","month","day"]
	toGetString = toGet
	now = datetime.datetime.now()
	hour = str(now.hour)
	minute = str(now.minute)
	second = str(now.second)
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	toGet = eval(toGet)
	if toGetString in valid:
		return toGet
	else:
		raise NameError("Invalid Time")

def varChange(file, write):
	result = open('Files/Vars/' + file,"w").write(write)
	return result

def fileRead(file):
	result = open("Files/" + file).read()
	return result
	
def fileWrite(file, write):
	result = open('Files/' + file,"a").write(write + "\n")
	return result

def codeWrite(file, write):
	result = open(file,"a").write(write + "\n")
	return result
def printFile(message, client, file):
	file = Greeting.txt
	#result = open("Files/" + file).read()
	result = fileRead(file).split().strip()
	#result = result.split()
	result = ", ".join(result)
	sendMessage(message,client,result)

def addUser(message):
	split = message.split()
	foundUser = split[1]
	return foundUser

#Questioned Functions
def removeLine(file, removed):
	f = open("Files/" + file, "r")
	lines = f.readlines()
	f.close()
	f = open("Files/" + file, "w")
	for line in lines:
		if line != removed + "\n":
			#print(line)
			f.write(line)
	f.close()

def fileReadLine(file):
	result = open("Files/" + file).readline()
	return result
		
def quit(s):
	sendMessage(s, "OK, I'm being pulled way, see you later!")
	sys.exit()

async def capsModding(message,message2,client,user,platform,channel):
	warning = channel + "/CapsCheck/Warning"
	warning1 = fileRead(warning + "1.txt").split()
	warning2 = fileRead(warning + "2.txt").split()
	warning3 = fileRead(warning + "3.txt").split()
	warning4 = fileRead(warning + "4.txt").split()
	warning5 = fileRead(warning + "5.txt").split()
	if user in warning1:
		await sendMessage(message,client,platform,"STOP YELLING PLEASE! (Warning 2 " + user + ")")
		fileWrite(warning + "2.txt",user)
		removeLine(warning + "1.txt",user)
	elif user in warning2:
		await sendMessage(message,client,platform,"STOP YELLING PLEASE! (Warning 3, next is timeout " + user + ")")
		fileWrite(warning + "3.txt",user)
		removeLine(warning + "2.txt",user)
	elif user in warning3:
		await sendMessage(message,client,platform,"/timeout " + user + " 1 To Many Caps")
		await sendMessage(message,client,platform,"I warned you to not yell " + user + ".")
		fileWrite(warning + "4.txt",user)
		removeLine(warning + "3.txt",user)
	elif user in warning4:
		await sendMessage(message,client,platform,"/timeout " + user + " 10 To Many Caps")
		await sendMessage(message,client,platform,"Really? A one second timeout wasn't enough? Take 10 seconds " + user + ".")
		fileWrite(warning + "5.txt",user)
		removeLine(warning + "4.txt",user)
	elif user in warning5:
		await sendMessage(message,client,platform,"/timeout " + user + " 60 To Many Caps")
		await sendMessage(message,client,platform,"Really? A ten second timeout wasn't enough? Chill for a minute " + user + ".")
	else:
		await sendMessage(message,client,platform,"STOP YELLING PLEASE! (Warning 1 " + user + ")")
		fileWrite(warning + "1.txt",user)
		
class MessageObject:
	def __init__(self,user,message):
		self.user = user
		self.message = message
		self.timeStamp = datetime.datetime.now()