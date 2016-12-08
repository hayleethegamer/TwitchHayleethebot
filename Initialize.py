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
from Chat_Commands import fileRead, varChange
from Socket import sendMessage
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	if "reload = 0" in fileRead("Vars/Reload.txt"):
		sendMessage(s, "Hello! I'm Hayleethebot, a bot made my Hayleethegamer!")
		varChange("Reload.txt", "reload = 0")
	else:
		sendMessage(s, "Bot Reloaded")
		varChange("Reload.txt", "reload = 0")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
