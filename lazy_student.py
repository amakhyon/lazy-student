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
spl_sec = Lecture("spl_sec", datetime.datetime(2021, 4, 18, 11, 30), "https://zoom.us/j/96135607670?pwd=VEJWSFNmZDJsVHpyWnUyQitPK3ZLdz09")



lecs = [spl_lec, spl_sec]

def open_lecture(link):
	driver = webdriver.Chrome()
	driver.get(link)
	time.sleep(3)
	pyautogui.click('launch_button.png')


def its_time(lec):
	now = datetime.datetime.now()
	if  now.strftime("%I") == lec.time.strftime("%I") and now.strftime("%M") == lec.time.strftime("%M"):
		return True
	else:
		return False





#scheduler that is not computationaly heavy 
# s = sched.scheduler(time.time, time.sleep)
# def check_lecs(sc): 
# 	now = datetime.datetime.now()
# 	for lec in lecs:
# 		if its_time(lec):
# 			open_lecture(lec.link)
# 	s.enter(40, 1, check_lecs, (sc,))

# s.enter(40, 1, check_lecs, (s,))
# s.run()

#Vbox ( lazy student label, Hbox( Vbox(label, time, add), Vbox(appointments, appoint1, appoint2,.., delete) ) )
class Window(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Lazy Student")
		self.setGeometry(100,100,400,200)
		main_layout = QVBoxLayout()
		lazyLabel = QLabel("Lazy Student")
		lazyLabel.setFont(QFont('Arial', 30))
		main_layout.addWidget( lazyLabel)


		containter = QHBoxLayout()
		left = QVBoxLayout()
		right = QVBoxLayout()
		containter.addLayout(left)
		containter.addLayout(right)




#====================left wing==================================
		leftLabel = QHBoxLayout()  #Label:....
		leftLabel.addWidget(QLabel("Label"))
		leftLabel.addWidget(QLineEdit())


		leftLink = QHBoxLayout() #link....
		leftLink.addWidget(QLabel("link"))
		leftLink.addWidget(QLineEdit())

		leftTime = QHBoxLayout() #Time:...
		leftTime.addWidget(QLabel("Time"))
		leftTime.addWidget(QDateTimeEdit())


		left.addLayout(leftLabel) #adding it all together
		left.addLayout(leftLink)
		left.addLayout(leftTime)
		left.addWidget(QPushButton("add"))


#=======================right wing==========================
		right.addWidget(QLabel("appointments"))
		for i in range(5):
			right.addWidget(QLabel(str(i)))
		right.addWidget(QPushButton("Delete"))



		main_layout.addLayout(containter)
		self.setLayout(main_layout)
		self.show()



def submit():
	print('aya')
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
#if you want to add more lecs 
#1-create a lec object using the following format
#spl_lec = Lecture(label, datetime.datetime(2021, 4, 18,10,30), link), were date format is (year, month, day, hour, minute)
#2- add it in the lecs array


#note for future me:
#	please add a storing mechanism in a txt or a sql, also a gui to interact with it...thank you!

#I added the gui, please add the functionality in the form of event handlers and txt storage
#warn the user of the american date format 
#thank you !
