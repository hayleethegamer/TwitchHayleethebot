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
import string
import time
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Chat_Commands import chatCommands, fileRead
from sys import argv

s = openSocket()
joinRoom(s)
readbuffer = ""

greeting = "hey, hi, hello, greetings"
person = "haylee, chat, friends, guys, all, everyone"
greeting = greeting.split(",")
person = person.split(",")
greeted = []
mods = []
trusted = []
wgreeted = open('Files/Greeted.txt', 'a')
tempWhitelist = []


while True:
	readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
	for line in temp:
		#print("Debug: " + line)
                if "PING" in line:
                	s.send(line.replace("PING", "PONG"))
                        print(line)
                        print(line.replace("PING", "PONG"))
			sendMessage(s, "Debug: Ping found and responded too")
                        break
		user = getUser(line)
        	message = getMessage(line)
		chatCommands(readbuffer,s,message,temp,line,user,greeting,person,wgreeted,greeted,trusted,mods,tempWhitelist)
