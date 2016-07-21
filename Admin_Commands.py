from Functions import sendMessage, varChange, fileRead, codeWrite, printFile, addUser, fileWrite, removeLine
import subprocess
import sys
rating = "Family Friendly"
async def adminCommands(message,message2,client,user,platform,tempWhitelist,mods,channel):
	global rating
	#if (user in )
	if (user == "hayleethegamer"):
		if message2.startswith("!restart"):
			await sendMessage(message,client,platform,"Restarting...")
			varChange("Reload.txt","reload = 1")
			subprocess.call("Files/RestartBot.sh")
			sys.exit()
		elif message2.startswith("!error"):
				if "indexerror" in message2.lower():
					raise IndexError()
				elif "oserror" in message2.lower():
					raise OSError()
		elif message2.startswith("!print"):
			try:
				split = message2.split()
				printed = split[1]
				if printed == "file":
					try:
						file = split[2:len(split)]
						file = " ".join(file)
						result = fileRead(file).splitlines()
						result = ", ".join(result)
						#await printFile(message,client,file + ".txt")
						await sendMessage(message,client,platform,result)
					except FileNotFoundError:
						await sendMessage(message,client,platform,"The file does not exist.")
					except IndexError:
						await sendMessage(message,client,platform,"What file?")
				elif printed == "warnings":
					try:
						warnedList = split[2]
						warning = channel + "/CapsCheck/Warning"
						warning1 = fileRead(warning + "1.txt").split()
						warning2 = fileRead(warning + "2.txt").split()
						warning3 = fileRead(warning + "3.txt").split()
						warning4 = fileRead(warning + "4.txt").split()
						warning5 = fileRead(warning + "5.txt").split()
						peopleWarned = len(warning1) + len(warning2) + len(warning3) + len(warning4) + len(warning5)
						await sendMessage(message,client,platform,"The number of people in the warnings list are " + str(peopleWarned))
					except IndexError:
						await sendMessage(message,client,platform,"What warning should I print?")
			except IndexError:
				await sendMessage(message,client,platform,"Print what?")
		elif message2.startswith("!channel"):
			import Socket
			await sendMessage(message,client,platform,"The channel is " + channel + " (" + Socket.usedChannel + ")")
		elif message2.startswith("!testthing"):
			await sendMessage(message,client,platform,str(len(message2)) + " " + message2)
	

	if (user in mods):
		if "!addtrusted" in message.lower():
			foundUser = addUser(message)
			fileWrite(channel + "/Trusted.txt", foundUser)
			await sendMessage(message,client,platform, foundUser + " was added to Trusted list")
		if "!whitelist " in message.lower():
			whitelisted = addUser
			tempWhitelist.append(whitelisted)
			await sendMessage(message,client,platform, whitelisted + " May now post one link in chat")
		if "!removetrusted " in message.lower():
			removeUser = addUser(message)
			removeLine(channel + "/Trusted.txt", removeUser)
			await sendMessage(message,client,platform, removeUser + " was removed from the trusted list.")
		if message2.lower().startswith("!reset"):
			try:
				split = message2.split()
				resetting = split[1]
				if resetting == "warnings":
					try:
						resetUser = split[2]
						resetUser = resetUser.lower()
						try:
							toLevel = split[3]
						except IndexError:
							toLevel = "all"
						toLevel = toLevel.lower()
						count = 1
						warning = channel + "/CapsCheck/Warning"
						while count <= 5:
							removeLine(warning + str(count) + ".txt",resetUser)
							#print(count)
							count = count + 1
						if toLevel == "all":
							await sendMessage(message,client,platform,resetUser + " removed from warnings list")
						elif (toLevel == "1") or (toLevel == "one"):
							fileWrite(warning + "1.txt",resetUser)
							await sendMessage(message,client,platform,resetUser + " was moved to warning level 1")
						elif (toLevel == "2") or (toLevel == "two"):
							fileWrite(warning + "2.txt",resetUserv)
							await sendMessage(message,client,platform,resetUser + " was moved to warning level 2")
						elif (toLevel == "3") or (toLevel == "three"):
							fileWrite(warning + "3.txt",resetUser)
							await sendMessage(message,client,platform,resetUser + " was moved to warning level 3 (one second timeout)")
						elif (toLevel == "4") or (toLevel == "four"):
							fileWrite(warning + "4.txt",resetUser)
							await sendMessage(message,client,platform,resetUser + " was moved to warning level 4 (10 second timeout)")
						elif (toLevel == "5") or (toLevel == "five"):
							fileWrite(warning + "5.txt",resetUser)
							await sendMessage(message,client,platform,resetUser + " was moved to warning level 5 (1 minute time out)")
							
						
					except IndexError:
						await sendMessage(message,client,platform,"Who should I take off the warning list?")
				elif resetting == "greeted":
					varChange(channel + "/Greeted.txt","")
			except IndexError:
				await sendMessage(message,client,platform,"What am I resetting?")
		if channel == "John":
			if message2.lower().startswith("!stressfree"):
				await sendMessage(message,client,platform,"THIS IS THE STRESS FREE ZONE. That means, you come, and regardless of how terrible your day was, or how much crap life is throwing at you right now, you forget about it. put all your problems as far away as you possibly can, and have some fun with me. I'm here to make friends. are you ready?")
			if message2.lower().startswith("!rating"):
				try:
					split = message2.split()
					setting = split[1]
					setting = setting.lower()
					if (setting == "ff") or (setting == "family friendly"):
						rating = "Family Friendly"
						await sendMessage(message,client,platform,"The rating is now " + rating)
					elif (setting == "t") or (setting == "teen"):
						rating = "Teen"
						await sendMessage(message,client,platform,"The rating is now " + rating)
					elif (setting == "t+") or (setting == "teen+"):
						rating = "Teen"
						await sendMessage(message,client,platform,"The rating is now " + rating)
					elif (setting == "display"):
						await sendMessage(message,client,platform,"The Current rating of the stream is " + rating + " the chat is kept at a confortable Family Friendly rating")
					elif (setting == ""):
						await sendMessage(message,client,platform,"This channel employs a kind of rating system, FF being family friend, T which is Teen, and T+ which is basically mature. The Blacklist will remain in family friendly mode no matter the rating to keep a friendly chat. The current rating is " + rating)
				except IndexError:
					await sendMessage(message,client,platform,"This channel employs a kind of rating system, FF being family friend, T which is Teen, and T+ which is basically mature. The Blacklist will remain in family friendly mode no matter the rating to keep a friendly chat. The current rating is " + rating)
		
		
		
		
		
			
		
	'''elif message2.startswith("!add"):
			try:
				split = message2.split()
				added = split[1]
			except IndexError:
				await sendMessage(message,client,platform,"What am I to add?")
			if added == "command":
				try:
					split = message2.split()
					command = split[2]
					result = split[3:len(split)]
					result = " ".join(result)
					if (command == "") or (result == ""):
						await sendMessage(message,client,platform,"What am I adding? (One word command, result of command)")
					else:
						write1 = '\n	elif message2.startswith("!'
						write2 = '"):\n		await sendMessage(message,client,platform,"'
						write3 = '")'
						write = write1 + command + write2 + result + write3
						codeWrite("Simple_Commands.py",write)
						varChange("addSimple.txt","addSimple=1")
						await sendMessage(message,client,platform,"Command !" + command + " added " + user.format(message))
				except IndexError:
					await sendMessage(message,client,platform,"What am I adding? (One word command, result of command)")
			elif added == "blame":
				try:
					split = message2.split()
					blamed = split[2]
					broke = split[3:len(split)]
					broke = " ".join(broke)
					if (broke == "") or (blamed == ""):
						await sendMessage(message,client,platform,"Who is to blame and what did they do?")
					else:
						write1 = '\n	elif " '
						write2 = '" in message2.lower():\n		await sendMessage(message,client,platform,"'
						write3 = '")\n		return True'
						write = write1 + blamed + write2 + broke + write3
						codeWrite("Blame_Command.py",write)
						varChange("addSimple.txt","addSimple=1")
						await sendMessage(message,client,platform,"Blamed " + blamed + " has been added")
				except IndexError:
					await sendMessage(message,client,platform,"Who is to blame and what did they do?")'''
