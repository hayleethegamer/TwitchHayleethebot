from Functions import sendMessage
async def help(message,message2,client,user,giversList,platform,languageList):
		try:
			split = message2.split()
			command = split[1:len(split)]
			command = " ".join(command)
			command = command.lower()
			blamePeople = ["hayleethebot", "echo", "blue","kjay","ISP","sandy","bananas","hayleethegamer"]
			blamePeople = ", ".join(blamePeople)
			simpleCommands = ["hayleethebot", "bed", "get well", "abuser", "rude", "hayleediscord", "lawyer", "cut", "realhaylee", "hayleebelief", "party", "gg", "break", "hold", "dance", "questionit", "order66"]
			simpleCommands2 = "`, `".join(simpleCommands)
			complexCommands = ["quote", "troublemaker", "thanks", "blame", "night", "ban", "buggy", "stalker", "lazy","hellochance","Shotgun", "english", "random", "dice"]
			complexCommands = "`, `".join(complexCommands)
			givers = ", ".join(giversList)
			language = ", ".join(languageList)
			if command == "":
				await sendMessage(message,client,platform,"The current Commands are `" + simpleCommands2 + "`, `" + complexCommands + "`. Some commands need extra to run properly, type '!help [command]' for more information on how to use that command")
			elif command in simpleCommands:
				await sendMessage(message,client,platform,command.capitalize() + " is a 'simple command' so there is nothing to it, just type it in and go")
			elif command == "quote":
				await sendMessage(message,client,platform,"Quote takes a 'giver' and a number, the current givers are " + givers + ". The numbers vary by who the giver is. You can also have it randomly pick quotes with '!quote random' and '!quote [giver] random' You can also do '!quote list' to list the givers and how many quotes they have ('!quote list [giver]')")
			elif command == "troublemaker":
				await sendMessage(message,client,platform,"Troublemaker requires a name. Example: '!troublemaker haylee'")
			elif command == "thanks":
				await sendMessage(message,client,platform,"Thanks can be used with or without a name. Example with name: '!thanks haylee'")
			elif command == "blame":
				await sendMessage(message,client,platform,"Blame requires a specific name to work right. these names are " + blamePeople + ". Example: '!blame hayleethebot'")
			elif command == "night":
				await sendMessage(message,client,platform,"Night can be used with or without a name much like thanks. Example with name: '!night haylee'")
			elif command == "ban":
				await sendMessage(message,client,platform,"First up, ban will **NOT** actually ban a user. Ban requires both a user to ban and a time for which to ban them in that order. Example: '!ban haylee life'")
			elif command == "buggy":
				await sendMessage(message,client,platform,"Buggy requires an object that you think is buggy. Example: '!buggy hayleethebot'")
			elif command == "stalker":
				await sendMessage(message,client,platform,"Stalker is a bit weird in it's order, but requires the one being stalked and the one doing the stalking in that order, which may seem weird. Example: '!stalker haylee hayleethebot'")
			elif command == "lazy":
				await sendMessage(message,client,platform,"Lazy requires a name which I know. These names are haylee, alejo, mittens, guy, and japher. Example: '!lazy haylee'")
			elif command == "hellochance":
				await sendMessage(message,client,platform,"Hellochance is kinda of a simple command, but it gets it's own help and it's considered complex. All this command does is figure the chance of a partical hello will be used in a fraction and a percent.")
			elif command == "shotgun":
				await sendMessage(message,client,platform,"Shotgun is an agressive command, a spin off of cut, except you can direct it at someone.")
			elif command == "english":
				await sendMessage(message,client,platform,"Simply says 'What is engilsh?' in " + language)
			elif command == "random":
				await sendMessage(message,client,platform,"Random is simple enough, it just randomly prints characters")
			elif command == "dice":
				await sendMessage(message,client,platform,"Dice is simple, it roles a dice with how ever many sides you tell it how ever many times you tell it, however the time is optional, if left blank it roles once.")
			else:
				await sendMessage(message,client,platform,"Sorry, that is not a command I have.")

		except IndexError:
			await sendMessage(message,client,platform,"The current Commands are hayleethebot, bed, get well, abuser, rude, hayleediscord, lawyer, realhaylee, troublemaker, thanks, blame, night, ban, buggy, stalker, and lazy. Some commands need extra to run properly, type '!help [command]' for more information on how to use that command")