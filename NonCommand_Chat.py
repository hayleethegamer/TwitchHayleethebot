from Functions import sendMessage, varChange, fileRead, fileWrite
#import discord
import random

async def noncommandChat(message,message2,client,user,platform,channel=None):
	puncutation = [",",".","?","!","'",'"',"*",":","`","~","_","@","#",";",":"]
	puncutation = "".join(puncutation)
	tableNumEnd = 3
	personFlipNumEnd = 5
	if platform == "discord":
		if message2.lower().startswith("hayleethebot"):
			if " how are you" in message2.lower():
				await sendMessage(message,client,platform,"I'm fine, just botting around, and you " + user.format(message))
			elif " what's up" in message2.lower():
				await sendMessage(message,client,platform,"Nothing much, just doing bot things.")
			elif " why are you so buggy" in message2.lower():
				await sendMessage(message,client,platform,"I'm not buggy!")
			elif " get it together" in message2.lower():
				await sendMessage(message,client,platform,"I do have it together! Don't judge me!")
	
		elif ("(╯°□°）╯︵ ┻━┻" in message2) or ("(ﾉಥ益ಥ）ﾉ﻿ ┻━┻" in message2) or ("(ノಠ益ಠ)ノ彡┻━┻" in message2):
			pickUpTableNum = random.randint(1,tableNumEnd)
			if pickUpTableNum == 1:
				await sendMessage(message,client,platform,"┬─┬﻿ ノ( ゜-゜ノ)")
			flipPersonNum = random.randint(1,personFlipNumEnd)
			if flipPersonNum == 1:
				await sendMessage(message,client,platform,"(╯°□°）╯︵( /o°o)/")
		elif "┻━┻ ︵﻿ ¯\(ツ)/¯ ︵ ┻━┻" in message2:
			pickUpTableNum = random.randint(1,tableNumEnd)
			if pickUpTableNum == 1:
				await sendMessage(message,client,platform,"┬─┬﻿ ノ( ゜-゜ノ)\n┬─┬﻿ ノ( ゜-゜ノ)")
			flipPersonNum = random.randint(1,personFlipNumEnd)
			if flipPersonNum == 1:
				await sendMessage(message,client,platform,"(╯°□°）╯︵( /o°o)/")
		
	#For the bot to say hi to people saying hi to the server
	person = "null"
	try:
		split = message2.split()
		greeting = split[0].strip(puncutation)
		person = split[1].strip(puncutation)
	except IndexError:
		try:
			split = message2.split()
			greeting = split[0].strip(puncutation)
		except IndexError:
			greeting = "null"
			person = "null"

	if (greeting.lower() in fileRead("Greetings.txt").split()) and (person.lower() in fileRead("Persons.txt").split()) or (person.lower() in fileRead("Greetings.txt").split()) and (greeting.lower() in fileRead("Persons.txt").split()):
			if user.format(message) != "Hayleethebot":
				if (platform == "twitch") and (user not in fileRead(channel + '/Greeted.txt')):
					toHi = fileRead("Greetings.txt").split()
					await sendMessage(message,client,platform,random.choice(toHi).title() + " " + user.format(message) + " welcome to the stream")
					fileWrite(channel + "/Greeted.txt", user)
				elif platform == "discord":
					toHi = fileRead("Greetings.txt").split()
					await sendMessage(message,client,platform,random.choice(toHi).title() + " " + user.format(message))
	elif (greeting.lower() == "night") and (person.lower() in fileRead("Persons.txt").split()) or (person.lower() == "night") and (greeting.lower() in fileRead("Persons.txt").split()):
			if user.format(message) != "Hayleethebot":
				if platform == "discord":
					await sendMessage(message,client,platform,"Night " + user.format(message))
