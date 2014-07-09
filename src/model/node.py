#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

import os
import sys

class node:
	"""To store an item of the filesystem (directory or file)"""
	
	def __init__(self, path, name, father):
		"""Variables of the node class"""
		self.name = name  # name of the file WITHOUT PATH
		self.path = path  # path of the file WITHOUT FILENAME
		self.isDir = True  # is it a directory ?
		self.isVid = False  # is it a video ?
		self.father = father  # link to the father node
		self.children = []  # link to every children node
		# reminder about the lists:
		# add an element: children.append(element)
		# loop: for element in children: 
		self.seen = False  # have you seen this movie ?
		if father is None:
			self.depth = 0  # depth in the tree (usefull to optimize display)
		else:
			self.depth = father.depth + 1

		# 
		self.haveYouSeenThisMovie = False

		# info given by MediaInfo:
		self.duration = None
		self.size = None
		self.definition = None
		self.frame_rate = None
		self.codec = None
		self.tracks_audio = None  # list containing audio tracks
		self.tracks_subtitles = None  # list containing subtitles tracks

