import string

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(":", 2)
	#print(separate)
	message = separate[2]
	#print(message)
	return message
