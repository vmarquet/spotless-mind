#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

import os
import sys
import pickle
from xml.dom import minidom
from myXML import *
from src.model.node import node

def save_pickle(file_path, root_node_list):
	"""To save a list in a file with pickler"""
	with open(file_path, 'wb') as file:
		pickler = pickle.Pickler(file)
		pickler.dump("1.0")
		pickler.dump(root_node_list)
		file.close()

def save_XML(root):
	"""To save the tree (result of the scan) in a file"""
	file_dom = minidom.Document()  # create XML file with header

	# we run through the tree and convert it into DOM
	recursive_save_XML(file_dom, root, file_dom)

	# we save it to a XML file
	file = open("data" + root.name + ".xml", "w")
	file.write(file_dom.toxml())  # to have a well indented XML file, use toprettyxml, but the spaces will generate #text during loading
	file.close()

	# to see in console for debug
	# print file_dom.toprettyxml()


def recursive_save_XML(file_dom, node, father_dom):  # Warning: father is an XML element, not a node
	"""The recursive part of save function"""
	if node.isDir == True:
		file2xml = add_sub_dir(file_dom, node, father_dom)
	else:
		file2xml = add_file_to_dir(file_dom, node, father_dom)
	for child in node.children:
		recursive_save_XML(file_dom, child, file2xml)