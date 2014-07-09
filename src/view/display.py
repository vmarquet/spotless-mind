#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

import os
import sys
from PyQt4 import QtGui, QtCore
from src.model.node import node
from src.view.customQStandardItem import customQStandardItem
		

def convertBinaryTreeToDisplay(root_node):
	"""Convert a tree of nodes to a tree of QStandardItems to display it""" 
	root_item = customQStandardItem(root_node.name)
	for n in root_node.children:
		convertBinaryTreeToDisplay_recursive(n, root_item)
	return root_item


def convertBinaryTreeToDisplay_recursive(node, father_QSItem):
	"""the recursive part of convertBinaryTreeToDisplay""" 
	item = customQStandardItem(node.name)
	father_QSItem.appendRow(item)
	if node.isDir == True:
		for n in node.children:
			convertBinaryTreeToDisplayRecursive(n, item)

def convertBinaryTreeToDisplayDirOnly(root_node):
	"""Convert a tree of nodes to a tree of QStandardItems to display it""" 
	root_item = customQStandardItem(root_node.name)
	root_item.node = root_node
	for n in root_node.children:
		convertBinaryTreeToDisplayDirOnly_recursive(n, root_item)
	return root_item


def convertBinaryTreeToDisplayDirOnly_recursive(node, father_QSItem):
	"""the recursive part of convertBinaryTreeToDisplayDirOnly""" 
	if node.isDir == False:
		return
	item = customQStandardItem(node.name)
	item.node = node
	father_QSItem.appendRow(item)
	if node.isDir == True:
		for n in node.children:
			convertBinaryTreeToDisplayDirOnly_recursive(n, item)

def displayFilesInDirFromNode(father_node, item_model):
	"""To get all the files in a directory""" 
	for n in father_node.children:
		item = customQStandardItem(n.name)
		item_model.appendRow(item)

def displayFilesInDirFromIndex(father_index, model_file, model_dir):
	"""To get all the files in a directory""" 
	father_item = model_dir.itemFromIndex(father_index)
	father_node = father_item.node
	for n in father_node.children:
		if n.isDir == False:  # we want to display only files, not directories
			item = customQStandardItem(n.name)
			item.node = n
			model_file.appendRow(item)
	

def display(root):  # to display in console
	"""To run through a tree and display it with indentation"""
	# Python 
	print "   " * root.depth + root.name
	display_recursive(root)

def display_recursive(father):
	"""Recursive part of display function"""
	for file in father.children:
		if file.isDir == True:
			# Python 2.7
			# print "   " * file.depth + file.name + 'X'*file.depth
			# Python 3
			print("   " * file.depth, file.name, 'X'*file.depth)
			display_recursive(file)
		else:
			# Python 2.7
			# print "   " * file.depth + file.name
			# Python 3
			print("   " * file.depth, file.name)