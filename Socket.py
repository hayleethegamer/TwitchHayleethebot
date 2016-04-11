import socket
import string
from Settings import HOST, PORT, PASS, IDENT, CHANNEL
from Read import getUser, getMessage

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + IDENT + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Hayleethebot: " + messageTemp)
