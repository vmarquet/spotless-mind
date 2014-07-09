#!/usr/bin/python
# -*-coding:Utf-8 -*   # linux

from PyQt4 import QtGui, QtCore

class customQStandardItem(QtGui.QStandardItem):

	def __init__(self, father):
		QtGui.QStandardItem.__init__(self, father)
		self.setEditable(False)
		self.node = None   # link the the corresponding node

# class customQStandardItemForFile(customQStandardItem):

# 	def __init__(self, father):
# 		customQStandardItem.__init__(self, father)
# 		