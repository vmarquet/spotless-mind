#!/usr/bin/python3.2
# -*-coding:Utf-8 -*   # linux

import os
from pymediainfo import MediaInfo
from src.model.node import node

def recursive_scan(father):
	"""To add recursively every file to the tree from the root of the scan"""
	ext_video = ['.divx','.avi','.mp4','.mkv','.wmv','.flv','.mov','.mpg','.mpeg','.rmvb','.m4v','.ts','.vlc']
	# PENSER A GERER LE CAS OU LES EXT SONT EN MAJUSCULE
	curdir = os.path.join(father.path, father.name)
	# print "recursive-scan: i visited " + curdir
	for file in os.listdir(curdir):  # for every file
		new_node = node(curdir, file, father)
		file_name, file_extension = os.path.splitext(file)

		# TODO: we get filesize (in bytes)

		# we use MediaInfo to get video informations if it's a video file
		if file_extension in ext_video:
			mediainfo(new_node)
			new_node.isVid = True

		father.children.append(new_node)
		if os.path.isdir(os.path.join(curdir, file)):  # if the file is a directory
			new_node.isDir = True
			recursive_scan(new_node)
		else:  # if the file is not a directory
			new_node.isDir = False

def mediainfo(node):
	"""To update video informations in the node"""
	file_path = os.path.join(node.path, node.name)
	print(file_path)
	media_info = MediaInfo.parse(file_path)
	if media_info == None:  # not sure if usefull
		return
	node.tracks_audio = list()
	node.tracks_subtitles = list()

	for track in media_info.tracks:
		if track.track_type == 'General':
			# NB: track.duration is given in milliseconds
			duration_sec_total = int(float(track.duration))/1000
			duration_hour = int(duration_sec_total/3600)
			duration_min = (duration_sec_total/60)%60
			node.duration = str(duration_hour) + "h" + str(duration_min)
			if track.file_size < 1000000:
				node.size =  str(track.file_size/1000000) + " mb"
			else:
				node.size =  str(track.file_size/1000000000) + "." + str((track.file_size/1000000)%1000) + " gb"
		if track.track_type == 'Video':
			node.definition = str(track.width) + "*" + str(track.height)
			node.frame_rate = str(track.frame_rate)
			node.codec = str(track.codec)
		if track.track_type == 'Audio':
			l = list()
			l.append(str(track.language))
			l.append(str(track.format))
			l.append(str(track.default))
			l.append(str(track.forced))
			node.tracks_audio.append(l)
		if track.track_type == 'Text':
			l = list()
			l.append(str(track.language))
			l.append(str(track.format))
			l.append(str(track.default))
			l.append(str(track.forced))
			node.tracks_subtitles.append(l)


