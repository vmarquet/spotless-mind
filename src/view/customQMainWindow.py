#!/usr/bin/python3.2
# -*-coding:Utf-8 -*   # linux

import pickle
from PyQt4 import QtGui, QtCore
from src.view.customQPushButton import customQPushButton
from src.view.popupFileInfo import popupFileInfo
from src.model.load import *
from src.model.save import *
from src.model.scan import *
from src.view.display import *

class customQMainWindow(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.model_dir = None
		self.model_file = None
		self.view_tree = None   # to display directories
		self.view_list = None   # to display files
		self.root_item_list = list()
		self.init()

	def init(self):
		# settings of the main window
		self.setWindowTitle('Spotless Mind')
		icon = QtGui.QIcon("icons/icon.png")
		self.setWindowIcon(icon)
		self.resize(640, 480)
		self.move(300, 100)

		# we must use a widget for the main zone of the window (everywhere except toolbar)
		# WARNING: use window.setCentralLayout instead will not work, we must use a widget first
		# WARNING: for unknown reason, is the tollbar is added before centralWidget is set, the program freezes
		# mainWidget = QtGui.QWidget()
		mainWidget = QtGui.QSplitter()
		# QSplitter hérite de QWidget, pas de QLayout, mais se comporte comme un layout horizontal
		self.setCentralWidget(mainWidget)

		# we create the toolbar
		toolbar = QtGui.QToolBar("toolbar", self)  # dans un QWidget/QMainWindow: toolbar = QtGui.QToolBar("toolbar", Vlayout)
		toolbar.setMovable(False)
		toolbar.setMinimumSize(640,54)
		self.addToolBar(toolbar)

		# we create the buttons 
		buttonNewFile = customQPushButton("New file (clear current data)", "icons/buttonNewFile.png")
		buttonOpenFile = customQPushButton("Load a list from file (.mvl)", "icons/buttonLoadFile.png")
		buttonSaveFile = customQPushButton("Save a list to file (.mvl)", "icons/buttonSaveFile.png")
		buttonScan = customQPushButton("Scan an external harddrive", "icons/buttonScan.png")
		buttonSearch = customQPushButton("Search for a movie in the list", "icons/buttonSearch.png")
		buttonAbout = customQPushButton("About this software", "icons/buttonAbout.png")

		# on connecte tous les boutons à des fonctions
		self.connect(buttonNewFile,QtCore.SIGNAL("clicked()"),self.newFile)
		self.connect(buttonOpenFile,QtCore.SIGNAL("clicked()"),self.loadFile)
		self.connect(buttonSaveFile,QtCore.SIGNAL("clicked()"),self.saveFile)
		self.connect(buttonScan,QtCore.SIGNAL("clicked()"),self.scanDir)
		self.connect(buttonSearch,QtCore.SIGNAL("clicked()"),self.newSearch)

		# we add all the buttons to the toolbar
		toolbar.addWidget(buttonNewFile)
		toolbar.addWidget(buttonOpenFile)
		toolbar.addWidget(buttonSaveFile)
		toolbar.addWidget(buttonScan)
		toolbar.addWidget(buttonSearch)
		toolbar.addSeparator()
		toolbar.addWidget(buttonAbout)

		self.model_dir = QtGui.QStandardItemModel(0,1)  # rows will be append after
		self.model_dir.setHorizontalHeaderItem(0, QtGui.QStandardItem("Directories"))

		# we create the tree view to display directories
		self.view_tree = QtGui.QTreeView()
		mainWidget.addWidget(self.view_tree)
		self.view_tree.setModel(self.model_dir)
		# we connect the view to a function to update file display (right panel)
		self.view_tree.clicked.connect(self.updateFileDisplay)

		# we create the list view to display files
		self.view_list = QtGui.QListView()
		self.view_list.doubleClicked.connect(self.popupFileInfo)
		mainWidget.addWidget(self.view_list) 


	def loadFile(self):
		"""To open a file containing a filesystem data"""
		# "Fichier mvl (*.mvl)" -> pour filtrer sur l'extension
		file_path = QtGui.QFileDialog.getOpenFileName(self, "Load a list", QtCore.QString(), "Fichier mvl (*.mvl)")
		if file_path == "":
			print("User canceled")
			return
		result = load_pickle(file_path)
		if result == False:  # if problem
			return
		# we convert the trees of nodes to trees of items to display them
		for root in model.root_node_list:
			root_item = convertBinaryTreeToDisplayDirOnly(root)
			self.model_dir.appendRow(root_item)
			self.root_item_list.append(root_item)


	def saveFile(self):
		"""To save a filesystem data to a file"""
		#print("saveFile")
		if len(model.root_node_list) == 0:
			QtGui.QMessageBox.information(self, " ", "Nothing to save")
			return
		filter = QtCore.QString("Movie List .mvl (*.mvl)")
		file_path, filter = QtGui.QFileDialog.getSaveFileNameAndFilter(self, "Save a list", "", filter)
		# BUG: if user don't precise the extension (exemple: "file", the dialog window will check 
		# if "file" already exists, but not if "file.mvl" exists,
		# so "file.mvl" will be overwritten without any warning 
		if file_path == "":
			print("User canceled")
			return
		else:
			ext = file_path[-4:]  # we get the 4 last caracters
			if ext != ".mvl":
				file_path = file_path + ".mvl"
			# print "Choosen file: " + file_path
		save_pickle(file_path)


	def scanDir(self):
		"""To scan a filesystem to record data"""
		print("scanDir")
		dir = QtGui.QFileDialog.getExistingDirectory(self, "Choose a directory to scan")
		if dir == "":
			print("User canceled")
			return
		else:
			print("Choosen dir: ", unicode(dir))
			# we scan the directory 
			# root = node(os.path.basename(str(dir)), None)  # BUG: relative path
			root = node(os.path.dirname(unicode(dir)),os.path.basename(unicode(dir)), None)
			root.isDir = True
			recursive_scan(root)
			model.root_node_list.append(root)
			# we convert the tree of nodes to a tree of items to display it
			root_item = convertBinaryTreeToDisplayDirOnly(root)
			self.model_dir.appendRow(root_item)
			self.root_item_list.append(root_item)

	def updateFileDisplay(self, index):
		"""To update file display in the right panel of the window""" 
		# we create a new model
		self.model_file = QtGui.QStandardItemModel(0,1)
		self.model_file.setHorizontalHeaderItem(0, QtGui.QStandardItem("Files"))
		displayFilesInDirFromIndex(index, self.model_file, self.model_dir)
		self.view_list.setModel(self.model_file)

	def newFile(self):
		if len(model.root_node_list) > 0:
			reply = QtGui.QMessageBox.question(self,'Message',"Do you want to save current list ?",
			QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Yes |	QtGui.QMessageBox.No, QtGui.QMessageBox.No)
			if reply == QtGui.QMessageBox.Cancel:
				return
			if reply == QtGui.QMessageBox.Yes:
				self.saveFile()
		self.clear()

	def clear(self):
		"""To clear display"""
		for i in range(0,len(self.root_item_list)):
			del self.root_item_list[0]
		for i in range(0,len(model.root_node_list)):
			del model.root_node_list[0]

		# new dir model
		self.model_dir = QtGui.QStandardItemModel(0,1)  # rows will be append after
		self.model_dir.setHorizontalHeaderItem(0, QtGui.QStandardItem("Directories"))
		self.view_tree.setModel(self.model_dir)

		# new view model
		self.model_file = QtGui.QStandardItemModel(0,1)  # rows will be append after
		self.model_file.setHorizontalHeaderItem(0, QtGui.QStandardItem("Files"))
		self.view_list.setModel(self.model_file)

	def newSearch(self):
		"""To search for a film in the list"""
		QtGui.QMessageBox.information(self, "coming soon !", "Not implemented yet  :(")

	def popupFileInfo(self,index):
		item = self.model_file.itemFromIndex(index)
		popup = popupFileInfo(item.node)
		popup.exec_()


