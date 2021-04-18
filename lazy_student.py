import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from selenium import webdriver
import urllib.request
import sched, time
import pyautogui
import datetime




# x = datetime.datetime(2021, 4, 18,5,17) # year, month, day, hour, minute
# y = datetime.datetime(2021, 5, 23,5,17) #2021-04-18 07:01:27.243946
# if x.strftime("%a") == y.strftime("%a"):
# 	print(x.strftime("%a")) # weekday in short format (wed)
# 	print(y.strftime("%I")) #time in 0 -12 format
# 	print(x.strftime("%M")) #time in minutes 0-59
# 	print("now!!!")



class Lecture():
	def __init__(self,label,time,link):
		self.label = label;  self.time = time; self.link = link;



spl_lec = Lecture("spl_lec", datetime.datetime(2021, 4, 18,10,30), "https://zoom.us/j/7830655944")
spl_sec = Lecture("spl_sec", datetime.datetime(2021, 4, 18, 7, 44), "https://zoom.us/j/96135607670?pwd=VEJWSFNmZDJsVHpyWnUyQitPK3ZLdz09")



lecs = [spl_lec, spl_sec]

def open_lecture(link):
	driver = webdriver.Chrome()
	driver.get(link)
	time.sleep(3)
	pyautogui.click('launch_button.png')


def is_it_time(lec):
	now = datetime.datetime.now()
	if  now.strftime("%I") == lec.time.strftime("%I") and now.strftime("%M") == lec.time.strftime("%M"):
		return True
	else:
		return False





#scheduler that is not computationaly heavy 
s = sched.scheduler(time.time, time.sleep)
def check_lecs(sc): 
	now = datetime.datetime.now()
	for lec in lecs:
		if is_it_time(lec):
			open_lecture(lec.link)
	s.enter(55, 1, check_lecs, (sc,))

s.enter(55, 1, check_lecs, (s,))
s.run()



#if you want to add more lecs 
#1-create a lec object using the following format
#spl_lec = Lecture(label, datetime.datetime(2021, 4, 18,10,30), link), were date format is (year, month, day, hour, minute)
#2- add it in the lecs array


#note for future me:
#	please add a storing mechanism in a txt or a sql, also a gui to interact with it...thank you!