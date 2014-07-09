#!/usr/bin/python
# -*-coding:Utf-8 -*   # linux

from PyQt4 import QtGui, QtCore

class customQPushButton(QtGui.QPushButton):  # special class for the toolbar buttons: same size

	def __init__(self, tooltip, icon_path):
		QtGui.QPushButton.__init__(self,"")  # empty string because we don't want text next to the button
		self.size = 50
		self.icon_size = 48
		self.setFlat(True)  # to remove the square around the icon
		self.init(tooltip, icon_path)

	def init(self, tooltip, icon_path):
		self.setFixedSize(self.size + 10,self.size)
		self.setToolTip(tooltip)
		self.setIconSize(QtCore.QSize(self.icon_size, self.icon_size))
		icon = QtGui.QIcon(icon_path)
		self.setIcon(icon)