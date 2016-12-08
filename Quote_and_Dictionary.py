'''Copyright (C) 2016 Hayleethegamer 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
from Socket import sendMessage
import random

def quote(message,user,s):
	if " random" in message.lower():
		sendMessage(s, "This is a work in progress")
		givers = [" aurey ", " anne ", " secret "]
		giver = random.sample(givers,1)
		numChoose = 0
		print(giver[0])
		if giver[0] == " aurey ":
			print ("ok")
			num = [" 1"," 2"," 3"," 4"]
			print (num)
			numChoose = random.sample(num,1)
			quote(giver + numChoose, user, s)
			print(numChoose)
		elif giver[0] == " anne ":
			num = [" 1"," 2"," 3"," 4"," 5"]
			print (num)
			numChoose = random.sample(num,1)
			quote(giver + numChoose, user, s)
			print(numChoose)
		elif giver[0] == " secret ":
			num = [" 1"]
			print (num)
			numChoose = random.sample(num,1)
			quote(giver + numChoose, user, s)
			print(numChoose)

	elif " help" in message.lower():
		sendMessage(s, user + ", to use this command you need to enter a source and a number or description of a quote in my records. Example: '!quote haylee 1' You may also do a random quote with '!quote random'")

	elif (" aurey " in message.lower()) or (" aureylian " in message.lower()):
		if (" 1" in message) or (" aurey anne tap" in message.lower()):
			sendMessage(s, '"Anne I needed to tap that Sorry"- Aurey 2016')
		elif (" 2" in message) or (" me too player" in message.lower()):
			sendMessage(s, '"They have a me too on there player" ~Aurey 2016')
		elif (" 3" in message) or (" 3 2 1ed" in message.lower()):
			sendMessage(s, '"It wasnt 3 2 1ed yet." - Aureylian 2016')
		elif (" 4" in message) or (" aurey anne soulmates" in message.lower()):
			sendMessage(s, '"Because Anne and I are soulmates"- Aureylian 2016')
		else:
			sendMessage(s, "Sorry " + user + " That ws an invalid quote number or description for one of Aurey's quotes.")

	elif (" anne " in message.lower()) or (" annemunition " in message.lower()):
		if (" 1" in message) or (" I die" in message.lower()):
			sendMessage(s, '"I die" and "Im died" ~Anne 2015')
		elif (" 2" in message) or (" I'm streamer" in message.lower()):
			sendMessage(s, '"Hang on, Im a streamer!"~Anne 2016"')
		elif (" 3" in message) or (" pixel judge" in message.lower()):
			sendMessage(s, '"Little pixel man judges you!" ~Anne 2016')
		elif (" 4" in message) or (" forgot to remember" in message.lower()):
			sendMessage(s, '"sorry, forgot to remember" ~Anne 2016')
		elif (" 5" in message) or (" minute resub" in message.lower()):
			sendMessage(s, '"Thanks for the 4 minute resub" ~Anne 2016')
		else:
			sendMessage(s, "Sorry " + user + " you entered an invalid quote number or description for one of Anne's Quotes.")

	elif (" secret " in message.lower()):
		if (" 1" in message) or ("guys have them too" in message.lower()):
			sendMessage(s, "Guys have them too, they're just not as cool. ~[Name omitted for privacy] April 1, 2015")
		else:
			sendMessage(s, "Sorry " + user + " You entered an invalid quote number or descirption for one the secret giver's quotes.")
	else:
		sendMessage(s, "Sorry " + user + " you entered a quote giver I do not have on record, please try again.")


def dictionary(message,user,s):
	if " random" in message.lower():
		sendMessage(s, "This is a work in progress")
		#recall with mess of randomly choicen option and number, user of user

	elif " help" in message.lower():
		sendMessage(s, user + ", to use this command you need to enter a source and a number or the word you wish to see that is in my records. Example: '!dictionary haylee 1' You may also get a random word using '!dictionary random'")

	elif (" aurey " in message.lower()) or (" aureylian " in message.lower()):
		if (" 1" in message) or (" percentageally" in message.lower()):
			sendMessage(s, 'Word: "Percentageally" Definition: "" Time: "Aureylian, 2016"')
		else:
			sendMessage(s, "Sorry " + user + " that is an invalid word or number, please try again.")
	elif (" anne " in message.lower()) or (" annemunition " in message.lower()):
		if (" 1" in message) or (" exspoiled" in message.lower()):
			sendMessage(s, 'Word: "exspoiled" Definition: "Spoiled" Time: "Annemunition 2016"')
	else:
		sendMessage(s, "Sorry " + user + " that is an invalid source, please try again")
			
