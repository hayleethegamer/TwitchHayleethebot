import socket
import string
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
from Read import getUser, getMessage, getTime

def openSocket():
	
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
