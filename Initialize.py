import string
from Chat_Commands import fileRead, varChange
from Socket import sendMessage
from Functions import getPartTime
lastHourStart = ""
lastMinuteStart = ""
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024).decode()
		#temp = string.split(readbuffer, "\n")
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	if "reload = 0" in fileRead("Vars/Reload.txt"):
		sendMessage(s, "Hello! I'm Hayleethebot, a bot made my Hayleethegamer!")
		varChange("Reload.txt", "reload = 0")
		lastHourStart = getPartTime("hour")
		lastMinuteStart = getPartTime("minute")
	else:
		sendMessage(s, "Bot Restarted")
		varChange("Reload.txt", "reload = 0")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
