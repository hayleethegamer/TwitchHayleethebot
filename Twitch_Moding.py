from Functions import sendMessage, varChange, fileRead, fileWrite,removeLine, capsModding
async def twitchModing(message,message2,client,user,platform,trusted,tempWhitelist,mods,channel,autoCounter):
	if " n.i.g.g.e.r" in message:
		await sendMessage(message,client,platform, "/ban " + user)
	elif "ACTION" in message:
		if "donated" in message.lower(): #("has donated " in message.lower()) and ("to the stream with message" in message.lower()) or ("has donated" in message.lower() or 
			await sendMessage(message,client,platform, "/timeout " + user + " 600")
			await sendMessage(message,client,platform, "Don't do fake donations please, chill for 10 mintues")
	elif (user not in trusted) and (user not in mods):
		if user not in tempWhitelist:
			linkKey = fileRead("LinkKeys.txt").split()
			count = 0
			while count <= len(linkKey)-1:
				if linkKey[count] in message.lower():
					await sendMessage(message,client,platform, "/timeout " + user + " 1")
					await sendMessage(message,client,platform, "Sorry, no links please, if you want to post a link ask a mod")
					break
				count = count + 1
		if len(message2) >= 10:
			split = message2.split()
			noSpaceMessage = "".join(split)
			#print (noSpaceMessage)
			messageLen = len(noSpaceMessage)
			capCount = sum(1 for c in noSpaceMessage if c.isupper())
			#print(messageLen)
			#print(capCount)
			percent = (int(capCount) * 100)/int(messageLen)
			#print (str(percent) + "%")
			if (len(message2) >= 10) and (percent >= 90) or (len(message2) >= 15) and (percent >= 80) or (len(message2) >= 20) and (percent >= 70):
				await capsModding(message,message2,client,user,platform,channel)
	puncutation = [",",".","?","!","'",'"',"*",":","`","~","_","@","#",";",":"]
	puncutation = "".join(puncutation)
	blacklist = fileRead("BlackList.txt").split()
	count = 0
	messCount = 0
	splitMessage = message.lower().split()
	#print(splitMessage)
	while messCount <= len(splitMessage)-1:
		#print("mess" + str(messCount))
		filteredMessage = splitMessage[messCount].strip(puncutation)
		filteredSplit = list(filteredMessage)
		#print(filteredSplit)
		filterCount = 0
		filteredMessageArray = []
		while filterCount <= len(filteredSplit)-1:
			if filteredSplit[filterCount] not in puncutation:
				filteredMessageArray.append(filteredSplit[filterCount])
				#print(filteredMessageArray)
				#print(filterCount)
				#print("filteredwhile")
			filterCount = filterCount + 1
		filteredMessage = "".join(filteredMessageArray)
		while count <= len(blacklist)-1:
			#print(len(splitMessage))
			#print("count" + str(count))
			#print(blacklist[count])
			if blacklist[count] == filteredMessage:
				await sendMessage(message,client,platform, "/timeout " + user + " 10")
				await sendMessage(message,client,platform, "Don't say that, take 10 seconds to chill.")
				break
			count = count + 1
		messCount = messCount + 1
	#automated responces
	if channel == "John":
		if ("can i join" in message.lower()) or ("could i join" in message.lower()) or ("can i play" in message.lower()) or ("can i play with you" in message.lower() or ("may I join" in message.lower())):
			if autoCounter[0] == 0:
				await sendMessage(message,client,platform, "Sorry " + user + ", but this is a solo world")
				autoCounter[0] = 10
		elif ("can i be mod" in message.lower()) or ("may i be mod" in message.lower()) or ("how do i become a mod" in message.lower()):
			if autoCounter[1] == 0:
				await sendMessage(message,client,platform, "you want to be a mod " + user + "? try to lift mjolnir. Can't do it? Didn't think so. Foolish mortals")
				autoCounter[1] = 10
		elif ("what should john do" in message.lower()):
			if autoCounter[2] == 0:
				await sendMessage(message,client,platform, "CALL THE AVENGERS")
				autoCounter[2] = 10




async def twitchOnlyCommands(message,message2,client,user,platform,trusted,channel,commandCounter):
	if (message == "!timeoutm\r") and (commandCounter[0] == 0):
		await sendMessage(message,client,platform, "/timeout " + user + " 1")
		await sendMessage(message,client,platform, "Really? Why did you time yourself out?")
		commandCounter[0] = 10
	if user in trusted:
		if message == "!credit\r":
			await sendMessage(message,client,platform, "The base of this code was thanks to Bad Nidalee on Youtube. Here's the Video: https://www.youtube.com/watch?v=T8DLwACpe3o")
		elif message == "!test\r":
			await sendMessage(message,client,platform, "Yes, Hi, I'm working " + user)
		elif message == "!commands\r":
			await sendMessage(message,client,platform, "!bed, !test, !credit, !timeoutm, !quote, !dictionary, !trusted, !bot, !social")
		elif message == "!rules\r":
			await sendMessage(message,client,platform, fileRead("Rules.txt"))
		elif message == "!trusted\r":
			await sendMessage(message,client,platform, "Trusteds are users whome I trust more then the random viewer, they get access to commands and immunity from some of my automated modderating")
		elif message == "!bot\r":
			await sendMessage(message,client,platform, "I am Hayleethegamer's bot, I am all hard coded by Haylee with some base code from someone else (check credit command). I enjoy watching chat and Haylee. And don't call me an it, I'm a she.")
		elif message == "!social\r":
			await sendMessage(message,client,platform, "At the moment I do not have any social media I'm linking with this twitch account, but I may in the future")
		elif message == "!games\r":
			await sendMessage(message,client,platform, "Games " + channel + " has are " + fileRead(channel + "/Games.txt"))