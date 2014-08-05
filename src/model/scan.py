#!/usr/bin/python3.2
# -*-coding:Utf-8 -*   # linux

import os
from pymediainfo import MediaInfo
from src.model.node import node, GeneralMetadata, VideoTrack, AudioTrack, SubtitleTrack

def recursive_scan(father):
	"""To add recursively every file to the tree from the root of the scan"""

	# for performance reasons, we will scan files with mediainfo only if they have a videofile extension
	ext_video = ['.divx','.avi','.mp4','.mkv','.wmv','.flv','.mov','.mpg','.mpeg','.rmvb','.m4v','.ts','.vlc']

	curdir = os.path.join(father.path, father.name)
	# print "recursive-scan: i visited " + curdir
	for file in os.listdir(curdir):  # for every file
		new_node = node(curdir, file, father)
		file_name, file_extension = os.path.splitext(file)

		# TODO: we get filesize (in bytes)
		# we could also get creation date or last modification date
		
		# in order to deal with case matching, we convert extension to lowercase, and then we compare
		if file_extension.lower() in ext_video:
			# we use MediaInfo to get video informations if it's a video file
			mediainfo(new_node)
		else:
			new_node.isVid = False

		father.children.append(new_node)
		if os.path.isdir(os.path.join(curdir, file)):  # if the file is a directory
			new_node.isDir = True
			recursive_scan(new_node)
		else:  # if the file is not a directory
			new_node.isDir = False


def mediainfo(node):
	"""To collect video informations about the file and store it in the node structure"""

	file_path = os.path.join(node.path, node.name)
	print "MediaInfo: analysing file " + file_path

	# we scan the file with pymediainfo
	media_info = MediaInfo.parse(file_path)

	# if it's not a valid videofile, an exception will be raised when we will try to read the tracks
	try:
		test = media_info.tracks
		node.isVid = True
	except AttributeError:
		node.isVid = False
		return

	# we create lists to record video, audio and subtitles tracks
	node.videoTracks = list()
	node.audioTracks = list()
	node.subtitleTracks = list()

	# we record matadatas given by MediaInfo
	for track in media_info.tracks:

		# general information: duration, filesize
		if track.track_type == 'General':
			metadata = GeneralMetadata()

			# we get duration (given in milliseconds)
			if track.duration == None:
				metadata.duration = "?"
			else:
				duration_sec_total = int(float(track.duration))/1000
				duration_hour = int(duration_sec_total/3600)
				duration_min = (duration_sec_total/60)%60
				metadata.duration = str(duration_hour) + "h" + str(duration_min)

			# we get format
			metadata.format = toStr(track.format)

			node.generalMetadata = metadata

		# video track: dimension of pictures, framerate, codec
		if track.track_type == 'Video':
			video_track = VideoTrack()
			video_track.definition = toStr(track.width) + "*" + toStr(track.height)
			video_track.framerate = toStr(track.frame_rate)
			video_track.format = toStr(track.format)
			video_track.codec = toStr(track.codec)
			node.videoTracks.append(video_track)

		# audio track: language, format, tags (default, forced)
		if track.track_type == 'Audio':
			audio_track = AudioTrack()
			audio_track.language = toStr(track.language)
			audio_track.channels = toStr(track.channels)
			audio_track.format = toStr(track.format)
			audio_track.codec = toStr(track.codec)
			audio_track.default = toStr(track.default)
			audio_track.forced = toStr(track.forced)
			node.audioTracks.append(audio_track)

		# subtitle track: language, format, tags (default, forced)
		if track.track_type == 'Text':
			subtitle_track = SubtitleTrack()
			subtitle_track.language = toStr(track.language)
			subtitle_track.format = toStr(track.format)
			subtitle_track.codec = toStr(track.codec)
			subtitle_track.default = toStr(track.default)
			subtitle_track.forced = toStr(track.forced)
			node.subtitleTracks.append(subtitle_track)


def toStr(parameter):
	if parameter == None:
		return "?"
	else:
		return str(parameter)