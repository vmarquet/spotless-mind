#!/usr/bin/python

from PyQt4 import QtGui, QtCore
from src.view.customQMainWindow import customQMainWindow
import sys


def main():
	app = QtGui.QApplication(sys.argv)

	# app.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 6px; }")
	app.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 9px; margin-top: 0.5em; }  QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }" )

	# we create the main window
	window = customQMainWindow()

	window.show()
	app.exec_()

if  __name__ == '__main__':
	main()
