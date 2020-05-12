import sys
from PyQt4 import QtGui, QtCore
#from abcv import *
class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 1000, 1000)
		self.setWindowTitle("PyQT tuts!")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(100,100)
		btn.move(100,100)
	
		btn1 = QtGui.QPushButton("start", self)
		btn1.clicked.connect(QtCore.QCoreApplication.instance().abcv.py)
		btn1.resize(100,100)
		btn1.move(400,100)
		self.show()

	   
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
