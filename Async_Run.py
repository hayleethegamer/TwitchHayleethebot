import string
import time
from Read import getUser, getMessage, getTime
from Socket import openSocket, sendMessage
import Socket
from Initialize import joinRoom
from sys import argv
import sys
import asyncio
import Simple_Commands
import Chat_Commands
import NonCommand_Chat
import Admin_Commands
import Twitch_Moding
import sys
import importlib
import traceback
from Settings import CHANNEL
from Functions import codeWrite, fileRead

s = openSocket()
joinRoom(s)
readbuffer = ""

greeted = []
mods = []
trusted = []
tempWhitelist = []
platform = "twitch"
loop = asyncio.get_event_loop()
errors = 0
stopped = 0
osError = False
autoCounter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
commandCounter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


async def runningChat():
	while True:
		try:
			#print("startng try")
			global greeted
			global mods
			global trusted
			global platform
			global readbuffer
			global errors
			global stopped
			global osError
			global tempWhitelist
			global autoCounter
			global commandCounter
			addBlame = 0
			helped = 0
		
			readbuffer = readbuffer + s.recv(1024).decode()
			#print(readbuffer)
			#temp = string.split(readbuffer, "\n")
			temp = readbuffer.split("\n")
			readbuffer = temp.pop()
			for line in temp:
				#print("for loop")
				#print("Debug: " + line)
				if "PING" in line:
					s.send(line.replace("PING", "PONG").encode('utf-8'))
					print(getTime() + " " + line)
					print(getTime() + " " + line.replace("PING", "PONG"))
					sendMessage(s, "Debug: Ping found and responded too")
					continue
				user = getUser(line)
				messageStuff = getMessage(line)
				message = messageStuff
				#tags = messageStuff[0]
				message2 = message
				countAutoCount = 0
				countCommandCount = 0
				while countAutoCount <= len(autoCounter)-1:
					if autoCounter[countAutoCount] != 0:
						autoCounter[countAutoCount] = autoCounter[countAutoCount] - 1
					#print(countAutoCount)
					#print(autoCounter[countAutoCount])
					countAutoCount = countAutoCount + 1
				while countCommandCount <= len(commandCounter)-1:
					if commandCounter[countCommandCount] != 0:
						commandCounter[countCommandCount] = commandCounter[countCommandCount] - 1
					#print(countCommandCount)
					#print(commandCounter[countCommandCount])
					countCommandCount = countCommandCount + 1
				print(getTime() + " " + user + ": " + message)
				if (message.startswith("!reload")) and (user == "hayleethegamer"):
					try:
						importlib.reload(Simple_Commands)
						importlib.reload(Chat_Commands)
						importlib.reload(NonCommand_Chat)
						importlib.reload(Admin_Commands)
						importlib.reload(Twitch_Moding)
						helped = 1
						sendMessage(s,"Commands Reloaded " + user.format(message))
						errors = 0
						stopped = 0
					except:
						sendMessage(s,"```" + str(sys.exc_info()[1]) + "```")
				if Socket.usedChannel == "hayleethegamer":
					channel = "Haylee"
				elif Socket.usedChannel == "ibanezfanjohn":
					channel = "John"
				else:
					#sendMessage(s,"What the heck?")
					channel = "Other"
				mods = fileRead(channel + "/Mods.txt")
				trusted = fileRead(channel + "/Trusted.txt")
				if channel != "Other":
					await Twitch_Moding.twitchModing(message,message2,s,user,platform,trusted,tempWhitelist,mods,channel,autoCounter)
				if user in trusted or user in mods:
					await Simple_Commands.simpleCommands(message,message2,s,user,platform)
					await Chat_Commands.chatCommands(message,message2,s,user,addBlame,helped,platform)
				await Twitch_Moding.twitchOnlyCommands(message,message2,s,user,platform,trusted,channel,commandCounter)
				await NonCommand_Chat.noncommandChat(message,message2,s,user,platform,channel)
				await Admin_Commands.adminCommands(message,message2,s,user,platform,tempWhitelist,mods,channel)
		except KeyboardInterrupt:
			sendMessage(s,"I'm leaving now, later!")
			sys.exit()
		except (PermissionError, FileNotFoundError):
			errors += 1
			if (errors >= 5) and (stopped == 0):
				sendMessage(s,"Uh oh, I've sent to many errors, I'll stop now")
				codeWrite("Logs/Log1.txt", getTime() + " \r\n To many Error  D:\r\n")
				stopped = 1
			elif errors <= 5:
				errorLength = len(sys.exc_info())
				sendMessage(s,"There was a permissions Error or the file was not found, I do not have the rights to access this file.")
				sendMessage(s,"``` " + str(traceback.format_exc()) + " ```")
				try:
					codeWrite("Logs/Log1.txt", getTime() + " \r\n" + str(traceback.format_exc()) + "\r\n")
				except (PermissionError, FileNotFoundError):
					sendMessage(s,"Uh, I don't have permission to log this Error")
		except OSError:
			if osError == False:
				osError = True
				sendMessage(s,"There was an OSError, I am turning myself off now")
				errorLength = len(sys.exc_info())
				sendMessage(s,"``` " + str(sys.exc_info()[0:errorLength]) + " ```")
				#sendMessage(s,"``` " + str(traceback.format_exc()) + " ```")
				codeWrite("Logs/Log1.txt", getTime() + " \r\n" + str(traceback.format_exc()) + "\r\n")
				subprocess.call("Files/Kill-9.sh")
				while True:
					sys.exit(2)
		except:
			errors += 1
			if (errors >= 5) and (stopped == 0):
				sendMessage(s,"Uh oh, I've sent to many errors, I'll stop now")
				codeWrite("Logs/Log1.txt", getTime() + " \r\n To many Error  D:\r\n")
				stopped = 1
			elif errors <= 5:
				errorLength = len(sys.exc_info())
				sendMessage(s,"``` " + str(sys.exc_info()[0:errorLength]) + " ``` \n There was a bug")
				#sendMessage(s,"``` " + str(traceback.format_exc()) + " ```")
				try:
					codeWrite("Logs/Log1.txt", getTime() + " \r\n" + str(traceback.format_exc()) + "\r\n")
				except (PermissionError, FileNotFoundError):
					sendMessage(s,"Uh, I don't have permission to log this Error")
				

#loop.run_forever()
loop.run_until_complete(runningChat())
