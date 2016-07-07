import datetime

async def sendMessage(message,client,platform,sentMessage,CHANNEL=None):
	#check if default function value work (def func(perm=none))
	#for twitch, message is message, client is s, and sentmessage is the message to send
	print (platform)
	if platform == "discord":
		msg = await client.send_message(message.channel, sentMessage)
	elif platform == "twitch":
		import Socket
		from Settings import CHANNEL
		s = client
		#Socket.sendMessage(client,sentMessage)
		messageTemp = "PRIVMSG #" + CHANNEL + " :" + sentMessage
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


#Questioned Functions
def removeLine(file, removed):
        f = open("Files/" + file, "r")
        lines = f.readlines()
        f.close()
        f = open("Files/" + file, "w")
        for line in lines:
                if line != removed + "\n":
                        f.write(line)
        f.close()


def fileReadLine(file):
        result = open("Files/" + file).readline()
        return result
		
def quit(s):
	sendMessage(s, "OK, I'm being pulled way, see you later!")
	sys.exit()

def addUser(message):
	split = message.split()
	foundUser = split[1]
	return foundUser

def countCaps(message):
	count = sum(1 for c in message if c.isupper())
	return count
