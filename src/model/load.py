#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

import os
import sys
import pickle
from PyQt4 import QtGui
from src.model.model import model
from xml.dom import minidom
from myXML import *

def load_pickle(file_path):
	"""To load a list with Pickler"""
	with open(file_path, 'rb') as file:
		pickler = pickle.Unpickler(file)
		file_version = pickler.load()
		software_version = model.version
		if file_version != software_version:
			reply = QtGui.QMessageBox.warning(None, "WARNING", "This .mvl file was created "
				+ "with a different version of this software."
				+ " Loading it can lead to severe malfunctionning. Load it anyway ? \n"
				+ "File version: " + file_version + "\nSoftware version: " + software_version, 
				 QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
			if reply == QtGui.QMessageBox.No:
				file.close()
				return False
		model.root_node_list = pickler.load()
		file.close()
		return True

def load_XML(file):
	"""To load the content of a tree saved in an XML file"""
	file_dom = minidom.parse(file + '.xml')  # convert from XML to DOM
	root_dom = file_dom.documentElement  # to get root element of a DOM
	root_node = node(root_dom.nodeName, None)
	root_node.path = ""  # this line is useless now
	child = file_dom.childNodes

	# we create the node tree
	recursive_load_XML(child[0], root_node)
	return root_node

def recursive_load_XML(file_dom, father_node):
	"""The recursive part of load_XML function"""
	if file_dom.hasChildNodes() == True:
		father_node.isDir = True
		for child in file_dom.childNodes:
			tmp = node(child.nodeName, father_node)
			father_node.children.append(tmp)
			recursive_load_XML(child, tmp)
	else:
		father_node.isDir = False  # BUG: if the directory if empty, it will be false instead of true