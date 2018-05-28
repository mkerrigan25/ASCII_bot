import socket
import time
import urllib
import urllib2
import sys
import string
import random
import os
from time import gmtime, strftime

server = "irc.server.com"
channel = "#channel"
botnick = "username"
folder_dir = os.path.join("location of ascii dir") 

def ping():
	ircsock.send("PONG :Pong\n")

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+chan+" :"+msg+"\n")

def joinchan(chan):
	ircsock.send("JOIN "+chan+"\n")

def hello():
	ircsock.send("PRIVMSG "+channel+" :Hello\n")

def randFile():
	return random.choice(os.listdir(folder_dir))


ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+botnick+" "+botnick +" "+botnick+"\n")
ircsock.send("NICK "+botnick+"\n")
joinchan(channel)

while 1:
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)

	if ircmsg.find(":Hello " + botnick) != -1:
		hello()

	if ircmsg.find(":!ascii") != -1:
		img = open(os.path.join(folder_dir, randFile()), 'r')
		for var in img:
			sendmsg(channel, var)
			time.sleep(1)
		img.close()

	if ircmsg.find(":Time") != -1:
		sendmsg(channel, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
