#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

import os
import sys
import pickle
from xml.dom import minidom
from myXML import *

def load_pickle(file_path):
	"""To load a list with Pickler"""
	with open(file_path, 'rb') as file:
		pickler = pickle.Unpickler(file)
		version = pickler.load()
		if version != "1.0":
			print("VERSION ERROR: NEED 1.0")
			file.close()
			popup = QtGui.QMessageBox()
			popup.setText("VERSION ERROR: NOT 1.0")
			popup.setWindowTitle("ERROR")
			popup.setFixedSize(500,200)
			popup.exec_()
			return False, list()
		root_node_list = pickler.load()
		file.close()
		return True, root_node_list

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