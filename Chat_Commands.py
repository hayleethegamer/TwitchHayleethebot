#from Quote_and_Dictionary_Discord import quote, dictionary
import Blame_Command
import Help_Command
from Functions import sendMessage, varChange, fileRead
import json
#import discord
import importlib
import random
from fractions import Fraction
import string
import statistics

async def chatCommands(message,message2,client,user,addBlame,helped,platform):
	me = ["hayleethebot", "hayleebot","<@180867799168712705>","<@180815771172077569>"]
	commandUser = ["myself", "me", "my"]
	old = ["thineself", "thyself"] 
	giversList = ["Aurey","Anne","Secret","itmeJP","Haylee","MasterChief","Tanaka","John","Fuster","Tee","Echelon"]
	languageList = ["binary","french","spanish","Japanese"]
	hayleeGamer = ["haylee","hayleethegamer","hayleegamer","<@167744970952933376>"]
	oddHayleeGamer = ["hayiee","hayle","hayl33"]
	oddCharacters = ["â","„","®","Ž","ℎ","℮","ÿ","ë"]
	puncutation = [",",".","?","!","'",'"',"*",":","`","~","_","@","#",";",":"]
	puncutation = "".join(puncutation)
	echoNoName = ["Hayleethegamer"]
	numEndList = [12,5,1,1,2,1,1,9,1,2,1]
	#Aurey, Anne, Secret, itmeJP, Haylee, Master Chief, Tanaka, John, Fuster, Tee, Echelon
	danceGifs = ["http://67.media.tumblr.com/7393afd6c1d384324ec6124c561ae5e3/tumblr_mwo4ewEx9T1rxinpyo1_500.gif","https://giphy.com/gifs/scooby-doo-cute-dancing-DKPlcyFLmqovK"]
	if message2.lower().startswith("!quote"):
		#await sendMessage(message,client,platform,"This is currently not working, sorry.")
		#quote(message,user,client)
		with open("Quotes.json") as data_files:
			data = json.load(data_files)
		with open("Quotes_words.json") as data_files:
			dataWord = json.load(data_files)
		
		givers = ", ".join(giversList)
		try:
			split = message2.lower().split()
			giver = split[1]
			quote = split[2:len(split)]
			try:
				quoteTest = "".join(quote)
				int(quoteTest)
				quote = quoteTest
				quoteNum = True
				#await sendMessage(message,client,platform,"Number Quote")
			except ValueError:
				quote = " ".join(quote)
				quoteNum = False
				#await sendMessage(message,client,platform,"Word Quote ValueError")
			except TypeError:
				quote = " ".join(quote)
				quoteNum = False
				#await sendMessage(message,client,platform,"Word Quote TypeError")
				
			await randomQuote(message,message2,client,user,platform,giversList,givers,numEndList,quote,data,giver,quoteNum)
		except IndexError:
			giver = "null"
			quote = "0"
			await randomQuote(message,message2,client,user,platform,giversList,givers,numEndList,quote,data,giver,quoteNum)
	#TroubleMaker command
	elif message2.lower().startswith("!troublemaker"):
		try:
			split = message2.split()
			trouble = split[1]
			
			if trouble != "":
				await sendMessage(message,client,platform,"Well well if it isn't the troublemaker " + trouble)
			elif trouble in me:
				await sendMessage(message,client,platform,"So " + user.format(message) + " you think I'm a trouble maker? Well your a trouble maker for thinking so.")
			elif trouble in commandUser:
				await sendMessage(message,client,platform,"Well well if it isn't the troublemaker " + user.format(message))
			elif trouble in old:
				await sendMessage(message,client,platform,"Wait, are you a trouble maker from the 1560s?")
			else:
				await sendMessage(message,client,platform,"Well well if it isn't the trouble maker...")
		except IndexError:
			trouble = "null"
			await sendMessage(message,client,platform,"Well well if it isn't the trouble maker...")
	#Thanks Command
	elif message2.lower().startswith("!thanks"):
		try:
			split = message2.split()
			thanked = split[1]
			await sendMessage(message,client,platform,"Thank you " + thanked)
		except IndexError:
			thanked = "null"
			await sendMessage(message,client,platform,"Thank you!")
	#Blame Command
	elif message2.lower().startswith("!blame"):
		if addBlame == 1:
			importlib.reload(Blame_Command)
			addBlame = 0
			print("reloaded Blame")
		if await Blame_Command.blameCommand(message,message2,client,user,platform) != True:
			await sendMessage(message,client,platform,"Who is to blame?")
	#Night Command
	elif message2.lower().startswith("!night"):
		try:
			split = message2.split()
			byed = split[1:len(split)]
			byed = " ".join(byed)
			await sendMessage(message,client,platform,"Good night " + byed)
		except IndexError:
			byed = "null"
			await sendMessage(message,client,platform,"Good night")

	#Ban Command
	elif message2.lower().startswith("!ban"):
		try:
			split = message2.split()
			banned = split[1]
			banned = banned.strip(puncutation)
			time = split[2:len(split)]
			time = " ".join(time)
			oddCharNum = 0
			oddCharFound = 0
			printedBan = 0
			#print(banned + " " + time)
			if (banned == "") or (time == ""):
				await sendMessage(message,client,platform,"Who am I banning and for how long?")
			elif ("*" in banned.lower()) or ("~" in banned.lower()):
				await sendMessage(message,client,platform,"Sorry, can't format it mid word, try again")
			elif banned.lower() in me:
				await sendMessage(message,client,platform,"Sorry, I'm not banning myself.")
			elif banned.lower() in commandUser:
				await sendMessage(message,client,platform,"Ok, banning " + user.format(message) + " for " + time)
			elif banned.lower() in old:
				await sendMessage(message,client,platform,"Wait, are we back in the 1560s?")
			elif banned.lower() in hayleeGamer:
				await sendMessage(message,client,platform,"Sorry, can't ban my creator, and I have half a mind to ban you for trying :stuck_out_tongue:")
			elif banned.lower() in oddHayleeGamer:
				await sendMessage(message,client,platform,"I think you mispelt, could be wrong but yeah... I don't think HAYLEE is spelt " + banned.upper() + " (" + banned.lower() + ")")
			else:
				while oddCharNum <= len(oddCharacters):
					#print(oddCharNum)
					#print (len(oddCharacters))
					oddCharNum = oddCharNum + 1
					try:
						if (oddCharacters[oddCharNum] in banned) and (oddCharFound == 0):
							await sendMessage(message,client,platform,"The heck even is that character?")
							oddCharFound = 1
							printedBan = 1
					except IndexError:	
						if printedBan == 0:
							await sendMessage(message,client,platform,"OK, banning " +banned + " for " + time)
							printedBan = 1
		except IndexError:
			banned = "null"
			time = "null"
			await sendMessage(message,client,platform,"Who am I banning and for how long?")
			#await sendMessage(message,client,platform,"Error")
			#print(split)
	#Buggy Command
	elif message2.lower().startswith("!buggy"):
		try:
			split = message2.split()
			buggy = split[1:len(split)]
			buggy = " ".join(buggy)
			if "hayleethebot" in buggy.lower():
				await sendMessage(message,client,platform,"Wait! I'm not buggy!")
			elif buggy == "":
				await sendMessage(message,client,platform,"What's Buggy?")
			else:
				await sendMessage(message,client,platform,"Yeah, " + buggy + " is very buggy")
		except IndexError:
			buggy = "null"
			await sendMessage(message,client,platform,"What's buggy?")
	#Stalker Command
	elif message2.lower().startswith("!stalker"):
		try:
			split = message2.split()
			stalked = split[1]
			stalker = split[2]
			await sendMessage(message,client,platform,"Why are you stalking " + stalked + " " + stalker)
		except IndexError:
			stalker = "null"
			stalked = "null"
			await sendMessage(message,client,platform,"Who's stalking who? (Stalked then Stalker)")
	#Lazy Command
	elif message2.lower().startswith("!lazy"):
		if "haylee" in message2.lower():
			await sendMessage(message,client,platform,"Yeah, Hayleethegamer is very lazy, why are you so lazy haylee?!")
		elif "alejo" in message2.lower():
			await sendMessage(message,client,platform,"Alejo! why are you lazier then Haylee?")
		elif "mittens" in message2.lower():
			await sendMessage(message,client,platform,"Mittens! Why are you such a lazy cat!?")
		elif "guy" in message2.lower():
			await sendMessage(message,client,platform,"Which guy is lazy? There are a lot of them around.")
		elif "japher" in message2.lower():
			await sendMessage(message,client,platform,"Japhers why are you being so lazy?")
		elif "para" in message2.lower():
			await sendMessage(message,client,platform,"Why you so forgetful para!?")
		elif "john" in message2.lower():
			await sendMessage(message,client,platform,"John! Give up your procrastination crown and do work!")
		elif "fuster" in message2.lower():
			await sendMessage(message,client,platform,"Fuster! Stop being lazy and do the thing! The crown of procrastination and laziness belongs to haylee!")
		elif "turtle" in message2.lower():
			await sendMessage(message,client,platform,"Turtlequeen quit being a turtle and do stuff!")

		else:
			await sendMessage(message,client,platform,"Sorry, but that was an invalid name, I do not know about this person in relation to laziness")

	#Echo Command
	elif message2.lower().startswith("!echo"):
		split = message2.split()
		echo = split[1:len(split)]
		echo = " ".join(echo)
		if echo == "":
			await sendMessage(message,client,platform,"What am I echoing?")
		else:
			#if user.format(message) in echoNoName:
			await sendMessage(message,client,platform,echo)
			#else:
				#await sendMessage(message,client,platform,user.format(message) + " echoed: " + echo)
	#Help Command
	elif (message2.lower().startswith("!help")) or (message2.lower().startswith("!halp")):
		if helped == 1:
			importlib.reload(Help_Command)
			helped = 0
			print("reloaded Help")
		await Help_Command.help(message,message2,client,user,giversList,platform,languageList)
	#Hello chance Command
	elif message2.lower().startswith("!hellochance"):
		hellos = fileRead("Greetings.txt").split()
		hellosNum = len(hellos)
		chanceFaction = "1/" + str(hellosNum)
		percent = (1 * 100)/hellosNum
		await sendMessage(message,client,platform,"The chance is " + chanceFaction + " as a fraction, as a percent "+ str(percent) + "%")
	elif message2.lower().startswith("!tp"):
		try:
			split = message2.split()
			person = split[1]
			place = split[2:len(split)]
			place = " ".join(place)
			await sendMessage(message,client,platform,"Teleporting " + person + " to " + place)
		except IndexError:
			person = "null"
			place = "null"
			await sendMessage(message,client,platform,"Who is teleporting where?")
	#Shotgun Command
	elif message2.lower().startswith("!shotgun"):
		try:
			oddCharNum = 0
			oddCharFound = 0
			printedShotgun = 0
			split = message2.split()
			person = split[1:len(split)]
			person = " ".join(person)
			person = person.strip(puncutation)
			if person == "":
				await sendMessage(message,client,platform,user.format(message) + " please don't tell me I gotta use my shotgun.")
			elif person == "pull":
				await sendMessage(message,client,platform,"oooo, I get to play with my shotgun")
			elif ("*" in person.lower()) or ("~" in person.lower()):
				await sendMessage(message,client,platform,"Sorry, can't format it mid word, try again")
			elif person.lower() in me:
				await sendMessage(message,client,platform,"Sorry, I'm not able to shotgun myself.")
			elif person.lower() in commandUser:
				await sendMessage(message,client,platform,"I don't know why but ok, I will shotgun you " + user.format(message))
			elif person.lower() in old:
				await sendMessage(message,client,platform,"Wait, are we back in the 1560s?")
			elif person.lower() in hayleeGamer:
				await sendMessage(message,client,platform,"Sorry, can't shotgun my creator, and I have half a mind to shotgun you for trying :stuck_out_tongue:")
			elif person.lower() in oddHayleeGamer:
				await sendMessage(message,client,platform,"I think you mispelt, could be wrong but yeah... I don't think HAYLEE is spelt " + person.upper() + " (" + person.lower() + ")")
			else:
				while oddCharNum <= len(oddCharacters):
					#print(oddCharNum)
					#print (len(oddCharacters))
					oddCharNum = oddCharNum + 1
					try:
						if (oddCharacters[oddCharNum] in person) and (oddCharFound == 0):
							await sendMessage(message,client,platform,"The heck even is that character?")
							oddCharFound = 1
							printedShotgun = 1
					except IndexError:	
						if printedShotgun == 0:
							await sendMessage(message,client,platform,"Sorry " + person + " but you better back off or you will get a shotgun to the face!")
							printedShotgun = 1
		except IndexError:
			person = "null"
			await sendMessage(message,client,platform,user.format(message) + " please don't tell me I gotta use my shotgun.")
	#Chance Command
	elif message2.lower().startswith("!chance"):
		try:
			split = message2.split()
			try:
				happened = split[1]
				pool = split[2]
				total = split [3]
			except IndexError:
				happened = split[1]
				total = split[2]
				pool = "null"
			if (happened == "") or (pool == "") or (total == ""):
				await sendMessage(message,client,platform,"What and I figureing? (What happened then total, you can also do a fraction for what happened)")
			elif pool == "null":
				chanceFaction = int(happened)/int(total)
				chanceFaction = Fraction(chanceFaction)
				percent = (int(happened) * 100)/int(total)
				await sendMessage(message,client,platform,"The chance is " + str(chanceFaction) + " as a fraction, as a percent "+ str(percent) + "%")
			else:
				chanceFaction = (int(happened)/int(pool))**int(total)
				chanceFaction = Fraction(chanceFaction)
				percent = ((int(happened)/int(pool)) * 100)/int(total)
				await sendMessage(message,client,platform,"The chance is " + str(chanceFaction) + " as a fraction, as a percent "+ str(percent) + "%")
		except IndexError:
			happened = "null"
			total = "null"
			await sendMessage(message,client,platform,"What and I figureing? (What happened then total, you can also do a fraction for what happened)")
	#English Command
	elif message2.startswith("!english"):
		try:
			split = message2.split()
			language = split[1]
			#"What is English?" Is the standard"
			with open("English.json") as data_files:
				data = json.load(data_files)
		
			if(language == ""):
				language = random.sample(languageList,1)
				language = language[0]
				language = language.lower()
				await sendMessage(message,client,platform,data["Languages"][0][language])
			else:
				await sendMessage(message,client,platform,data["Languages"][0][language])
		except IndexError:
			language = "null"
			#"What is English?" Is the standard"
			with open("English.json") as data_files:
				data = json.load(data_files)
			language = random.sample(languageList,1)
			language = language[0]
			language = language.lower()
			await sendMessage(message,client,platform,data["Languages"][0][language])
	#Random Command
	elif message2.startswith("!random"):
		randomLetters =[]
		times = random.randint(1,20)
		timesDone = 0
		while timesDone <= times:
			timesDone = timesDone + 1
			randomLetters.append(random.choice(string.ascii_letters))
		randomLetters = "".join(randomLetters)
		await sendMessage(message,client,platform,randomLetters)
	#Dice Command
	elif message2.startswith("!dice"):
		try:
			split = message2.split()
			sides = int(split[1])
			if sides > 100:
				await sendMessage(message,client,platform,"I am not rolling a dice with more then 100 sides")
				sides = 100
			try:
				times = int(split[2])
				if times > 100:
					await sendMessage(message,client,platform,"I am not rolling the dice more then 100 times")
					times = 100
			except IndexError:
				times = 1
			timesRolled = 1
			result = []
			numResult = []
			if sides == 1:
				await sendMessage(message,client,platform,"Why do you want me to roll a 1 sided dice?")
			else:
				while timesRolled <= times:
					timesRolled = timesRolled + 1
					result.append(str(random.randint(1,sides)))
					numResult.append(random.randint(1,sides))
				result = ", ".join(result)
				#mode = statistics.mode(numResult)
				await sendMessage(message,client,platform,"The Result(s) is/are " + result)#+ ", the mode is " + str(mode))
		except ValueError:
			await sendMessage(message,client,platform,"Whole numbers only please.")
		except IndexError:
			await sendMessage(message,client,platform,"How many sides the dice have? and how many times and I rolling?")
		except TypeError:
			await sendMessage(message,client,platform,"Last I checked, you need a number to tell how many sides there are")
	#Dance Command
	elif message2.lower().startswith("!dance"):
		await sendMessage(message,client,platform,random.choice(danceGifs))
		
		
		
		
async def randomQuote(message,message2,client,user,platform,giversList,givers,numEndList,quote,data,giver,quoteNum):
	if " list" in message2.lower():
		if quote == "":
			await sendMessage(message,client,platform,"There are " + str(len(giversList)) + " givers, " + givers + " and there are varying number of quotes to each(!quote list [giver]")
		if quote == "aurey":
			await sendMessage(message,client,platform,"Aurey has " +str(numEndList[0]) + " quotes.")
		elif quote == "anne":
			await sendMessage(message,client,platform,"Anne has " +str(numEndList[1]) + " quotes.")
		elif quote == "secret":
			await sendMessage(message,client,platform,"Secret has " +str(numEndList[2]) + " quotes.")
		elif quote == "itmejp":
			await sendMessage(message,client,platform,"itmeJP has " +str(numEndList[3]) + " quotes.")
		elif quote == "haylee":
			await sendMessage(message,client,platform,"Haylee has " +str(numEndList[4]) + " quotes.")
		elif quote == "masterchief":
			await sendMessage(message,client,platform,"Master Chief has " +str(numEndList[5]) + " quotes.")
		elif quote == "tanaka":
			await sendMessage(message,client,platform,"Tanaka has " +str(numEndList[6]) + " quotes.")
		elif quote == "john":
			await sendMessage(message,client,platform,"IbanezFanJohn has " +str(numEndList[7]) + " quotes.")
		elif quote == "fuster":
			await sendMessage(message,client,platform,"FusterClunk has " +str(numEndList[8]) + " quotes.")
		elif quote == "tee":
			await sendMessage(message,client,platform,"Tee has " +str(numEndList[9]) + " quotes.")
		elif quote == "echelon":
			await sendMessage(message,client,platform,"Echelon has " +str(numEndList[9]) + " quotes.")
	
	elif (giver == "random") or (quote == "r a n d o m") or (quote == "random"):	
		if giver == "random":
			giver = random.sample(giversList,1)
			giver = giver[0]
			giver = giver.lower()
		if giver == "aurey":
			numEnd = numEndList[0]
			quote = random.randint(1,numEnd)
		elif giver == "anne":
			numEnd = numEndList[1]
			quote = random.randint(1,numEnd)
		elif giver == "secret":
			numEnd = numEndList[2]
			quote = random.randint(1,numEnd)
		elif giver == "itmejp":
			numEnd = numEndList[3]
			quote = random.randint(1,numEnd)
		elif giver == "haylee":
			numEnd = numEndList[4]
			quote = random.randint(1,numEnd)
		elif giver == "masterchief":
			numEnd = numEndList[5]
			quote = random.randint(1,numEnd)
		elif giver == "tanaka":
			numEnd = numEndList[6]
			quote = random.randint(1,numEnd)
		elif giver == "john":
			numEnd = numEndList[7]
			quote = random.randint(1,numEnd)
		elif giver == "fuster":
			numEnd = numEndList[8]
			quote = random.randint(1,numEnd)
		elif giver == "tee":
			numEnd = numEndList[9]
			quote = random.randint(1,numEnd)
		elif giver == "echelon":
			numEnd = numEndList[10]
			quote = random.randint(1,numEnd)
		#print(giver)
		quote = str(quote)#[0]
		list = int(quote) - 1
		#await sendMessage(message,client,platform,"Giver: " + giver)
		#await sendMessage(message,client,platform,"Quote: " + str(quote))
		#await sendMessage(message,client,platform,"List: " + str(list))
		#await sendMessage(message,client,platform,"Hello! :D")
		await sendMessage(message,client,platform,data[giver][list][quote])
	elif(giver == "") or (quote == ""):
		await sendMessage(message,client,platform,"Who gave the quote and which quote?")
	else:
		try:
			if quoteNum == True:
				list = int(quote) - 1
				await sendMessage(message,client,platform,data[giver][list][quote])
			else:
				await sendMessage(message,client,platform,dataWord[giver][0][quote])
		except KeyError:
			#await sendMessage(message,client,platform,"Giver: " + giver)
			#await sendMessage(message,client,platform,"Quote: " + quote)
			#await sendMessage(message,client,platform,"List: " + str(list))
			await sendMessage(message,client,platform,"Sorry, Invalid Giver/quote")