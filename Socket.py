import socket
import string
import sys
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
from Read import getUser, getMessage, getTime
from Functions import fileRead, varChange

usedChannel = ""
def openSocket():
	global CHANNEL
	global usedChannel
	if fileRead("Vars/Reload.txt") == "reload = 1":
		CHANNEL = fileRead("Vars/PrevChannel.txt")
	else:
		channel = input("What Channel should I go to? ")
		if channel.lower() == "haylee":
			CHANNEL = CHANNEL[0]
		elif channel.lower() == "john":
			CHANNEL = CHANNEL[1]
		elif channel.lower() == "fuster":
			CHANNEL = CHANNEL[2]
		elif channel.lower() == "exit":
			print("Ok, stopping the bot before it starts")
			sys.exit()
		else:
			rightChannel = False
			while rightChannel == False:
				channel = input("What channel should I go to? (full name)")
				confirm = input("Are you sure " + channel + " is right?")
				if confirm.lower() == "yes":
					rightChannel == True
					CHANNEL = channel
	usedChannel = CHANNEL
	varChange("PrevChannel.txt",CHANNEL)
	
	s = socket.socket()
	s.connect((HOST, PORT))
	sendPass = "PASS " + PASS + "\r\n"
	s.send(sendPass.encode('utf-8'))
	sendNick = "NICK " + IDENT + "\r\n"
	s.send(sendNick.encode('utf-8'))
	sendJoin = "JOIN #" + CHANNEL + "\r\n"
	s.send(sendJoin.encode('utf-8'))
	sendTags = "CAP REQ :twitch.tv/tags\r\n"
	#s.send(sendTags.encode('utf-8'))
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	messageSend = messageTemp + "\r\n"
	s.send(messageSend.encode('utf-8'))
	print(getTime() + " Hayleethebot: " + messageTemp)
