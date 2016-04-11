import string
import sys
import subprocess
#from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Quote_and_Dictionary import quote, dictionary
from sys import argv


def chatCommands(readbuffer,s,message,temp,line,user,greeting,person,wgreeted,greeted,trusted,mods,tempWhitelist):
                        print(user + ": " + message)
			#all users
			if ("hey haylee" in message.lower()) or ("hey chat" in message.lower()) or ("hi haylee" in message.lower()) or ("hi chat" in message.lower()) or ("hello haylee" in message.lower()) or ("hello chat" in message.lower()):
				if (user not in fileRead('Greeted.txt')) and (user not in greeted):
					sendMessage(s, "Hello " + user + ", welcome to the stream!")
					greeted.append(user)
					fileWrite("Greeted.txt", user)
			if message == "!timeoutm\r":
                                sendMessage(s, "/timeout " + user + " 1")
                                sendMessage(s, "Really? Why did you time yourself out?")
			#Truested
			if (user in fileRead("Trusted.txt")) or (user in trusted) or (user in fileRead("Mods.txt")) or (user in mods):
				if "!quote" in message:
        	                        quote(message,user,s)
	                        if "!dictionary" in message:
                	                dictionary(message,user,s) 
				if message == "!credit\r":
					sendMessage(s, "The base of this code was thanks to Bad Nidalee on Youtube. Here's the Video: https://www.youtube.com/watch?v=T8DLwACpe3o")
				if message == "!test\r":
					sendMessage(s, "Yes, Hi, I'm working " + user)
				if message == "!bed\r":
					sendMessage(s, "Bed? What is a bed? Sleep? What's sleep? Who needs it?")
				if message == "!commands\r":
					sendMessage(s, "!bed, !test, !credit, !timeoutm, !quote, !dictionary, !trusted, !bot")
				if message == "!rules\r":
					sendMessage(s, fileRead("Rules.txt"))
				if message == "!trusted\r":
					sendMessage(s, "Trusteds are users whome I trust more then the random viewer, they get access to commands and immunity from some of my automated modderating")
				if message == "!bot\r":
					sendMessage(s, "I am Hayleethegamer's bot, I am all hard coded by Haylee with some base code from someone else (check credit command). I enjoy watching chat and Haylee. And don't call me an it, I'm a she.")
				
			#Moderators
			if (user in fileRead("Mods.txt")) or (user in mods):
				if "!addtrusted" in message:
					foundUser = addUser(message)
					trusted.append(foundUser)
					fileWrite("Trusted.txt", foundUser)
					sendMessage(s, foundUser + " was added to Trusted list")
				if "!whitelist " in message:
					whitelisted = addUser
					tempWhitelist.append(whitelisted)
					sendMessage(s, whitelisted + " May now post one link in chat")
				if "!removetrusted " in message:
					removeUser = addUser(message)
					removeLine("Trusted.txt", removeUser)
					sendMessage(s, removeUser + " was removed from the trusted list.")
			#broadcaster
			if user == "hayleethegamer":
				if (message == "!exit\r"):
                                	quit(s) 
				if "!addmod" in message:
					foundUser = addUser(message)
					print(foundUser)
					mods.append(foundUser)
					fileWrite("Mods.txt", foundUser)
					sendMessage(s, foundUser + " was added to the Moderators list")
				if (message == "!reloadbot\r"):
					print("Restarting...")
					varChange("Reload.txt", "reload = 1")
					subprocess.call("Files/RestartBot.sh")
					quit(s)
			#Bot Moding
			if (user not in trusted) and (user not in fileRead("Trusted.txt")) and (user not in mods) and (user not in fileRead("Mods.txt")):
				capsCount = countCaps(message)
				if (capsCount >= 10) and (capsCount <= 15):
					sendMessage(s,"Easy on the caps " + user)
				if (capsCount >= 15):
					sendMessage(s, "/timeout " + user + " 30")
					sendMessage(s, user + " Chill for half a minute")
				if ("http" in message) and (user not in tempWhitelist):
					sendMessage(s, "/timeout " + user + " 1")
					sendMessage(s, "Sorry " + user + " but no links without permission")
					if user in tempWhitelist:
						tempWhitelist.remove(user)
				if message in fileRead(BlackList.txt):
					sendMessage(s, "/timeout " + user + " 30")
					sendMessage(s, "Watch it, Don't be offensive. Chill for half a minute.")


def quit(s):
	sendMessage(s, "OK, I'm being pulled way, see you later!")
	sys.exit()

def fileRead(file):
	result = open("Files/" + file).read()
	return result

def fileWrite(file, write):
	result = open('Files/' + file,"a").write(write + "\n")
	return result

def addUser(message):
	split = message.split()
	foundUser = split[1]
	return foundUser

def countCaps(message):
	count = sum(1 for c in message if c.isupper())
	return count

def varChange(file, write):
        result = open('Files/Vars/' + file,"w").write(write)
        return result
def removeLine(file, removed):
	f = open("Files/" + file, "r")
	lines = f.readlines()
	f.close()
	f = open("Files/" + file, "w")
	for line in lines:
		if line != removed + "\n":
			f.write(line)
	f.close()
