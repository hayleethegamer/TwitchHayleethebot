from Functions import sendMessage, varChange, fileRead
async def blameCommand(message,message2,client,user,platform):
	if " hayleethebot" in message2.lower():
		await sendMessage(message,client,platform,"Hey, why you blaming me?")
		return True
	elif (" hayleethegamer" in message2.lower()) or (" haylee" in message2.lower()):
		await sendMessage(message,client,platform,"HAYLEE! Why did you do this? Well I guess I can't be to mad at you... You are my creator.")
		return True
	elif " echo" in message2.lower():
		await sendMessage(message,client,platform,"Yeah Echo! Why you do this? And don't you dare try and echo the blame to someone else!")
		return True
	elif " blue" in message2.lower():
		await sendMessage(message,client,platform,"Yeah Blue! Stop making everything blue and screwing everything up!")
		return True
	elif " kjay" in message2.lower():
		await sendMessage(message,client,platform,"Yeah Kjay! Stop throwing and flipping things! Your screwing everything up!")
		return True
	elif (" isp" in message2.lower()) or (" internet service provider" in message2.lower()):
		await sendMessage(message,client,platform,"ISP! WHY ARE YOU BEING TO BAD! WORK! NOW!")
		return True
	elif " sandy" in message2.lower():
		await sendMessage(message,client,platform,"SANDY! Why are you being so sandy and screwing things up?")
		return True
	elif " bananas" in message2.lower():
		await sendMessage(message,client,platform,"Dang it bananas, why'd you have to go and split")
		return True
	#Command Added

	elif " ace" in message2.lower():
		await sendMessage(message,client,platform,"Ace! Why are you screwing things up so much")
		return True

	elif " para" in message2.lower():
		await sendMessage(message,client,platform,"Para, why you gotta go mess everything up?")
		return True

	elif " autocorrect" in message2.lower():
		await sendMessage(message,client,platform,"AUTO CORRECT! STOP AUTO INCORRECTING!")
		return True

	elif " john" in message2.lower():
		await sendMessage(message,client,platform,"JOHN! Why you gotta john everything?")
		return True
