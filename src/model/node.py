#!/usr/bin/python3.2
# -*-coding:Utf-8 -*

import os
import sys

class node:
	"""To store an item of the filesystem (directory or file)"""
	
	def __init__(self, path, name, father):
		"""Attributes of the node class"""

		# attributes usefull to construct the node filesystem
		self.name = name  # name of the file WITHOUT PATH
		self.path = path  # path of the file WITHOUT FILENAME
		self.father = father  # link to the father node
		self.children = []  # link to every children node
		if father is None:
			self.depth = 0  # depth in the tree (usefull to optimize display)
		else:
			self.depth = father.depth + 1
		self.isDir = None  # boolean: is it a directory ?
		self.isVid = None  # boolean: is it a video ?

		# metadatas about the file
		self.filesize = None  # size in bytes
		self.mimetype = None  # MIME type
		self.creationDate = None  # file creation date
		self.lastAccessedDate = None  # last access to file date

		# movie info given by MediaInfo:
		self.generalMetadata = None  # only one object GeneralMetadata
		self.videoTracks = None  # list of tracks, there can be many in a single file (mkv...)
		self.audioTracks = None  # list of tracks
		self.subtitleTracks = None  # list of tracks
		self.haveYouSeenThisMovie = False




class GeneralMetadata:
	"""To store general metadatas about a video file"""

	def __init__(self):
		self.duration = None
		self.bitrate = None
		self.format = None

	def toString(self):
		print duration + "; " + bitrate + "; " + format


class VideoTrack:
	"""To store metadata about a video track"""

	def __init__(self):
		self.definition = None  # string: "width*height"
		self.framerate = None
		self.bitrate = None
		self.format = None
		self.codec = None


class AudioTrack:
	"""To store metadata about an audio track"""

	def __init__(self):
		self.language = None
		self.channels = None
		self.format = None
		self.codec = None
		self.default = None
		self.forced = None


class SubtitleTrack:
	"""To store metadata about a subtitle track"""

	def __init__(self):
		self.language = None
		self.format = None
		self.codec = None
		self.default = None
		self.forced = None

