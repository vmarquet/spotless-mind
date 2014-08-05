#!/usr/bin/python
# -*-coding:Utf-8 -*   # linux

from PyQt4 import QtGui, QtCore
from src.model.node import node, GeneralMetadata, VideoTrack, AudioTrack, SubtitleTrack

class popupFileInfo(QtGui.QDialog):

	def __init__(self,node):
		QtGui.QDialog.__init__(self)

		# if the file was not a video:
		if node.isVid == False:
			label = QtGui.QLabel("Not a video file")
			layout = QtGui.QGridLayout()
			self.setLayout(layout)
			layout.addWidget(label)
			return

		self.setWindowTitle(node.name)
		# self.resize(350, 200)
		# self.setFixedSize(self.size())

		layout = QtGui.QGridLayout()
		self.setLayout(layout)

		gb_general = QtGui.QGroupBox("General")
		layout.addWidget(gb_general,0,0)
		layout_general = QtGui.QGridLayout()
		gb_general.setLayout(layout_general)

		label = QtGui.QLabel("Size: ")
		layout_general.addWidget(label,0,0)
		label = QtGui.QLabel(node.filesize)
		layout_general.addWidget(label,0,1)

		label = QtGui.QLabel("Duration: ")
		layout_general.addWidget(label,1,0)
		label = QtGui.QLabel(node.generalMetadata.duration)
		layout_general.addWidget(label,1,1)

		label = QtGui.QLabel("Format: ")
		layout_general.addWidget(label,2,0)
		label = QtGui.QLabel(node.generalMetadata.format)
		layout_general.addWidget(label,2,1)

		# for each video track
		for i in range(0,len(node.videoTracks)):
			videoTrack = node.videoTracks[i]

			gb_video = QtGui.QGroupBox("Video")
			layout.addWidget(gb_video,1,0)
			layout_video = QtGui.QGridLayout()
			gb_video.setLayout(layout_video)

			label = QtGui.QLabel("Definition: ")
			layout_video.addWidget(label,0,0)
			label = QtGui.QLabel(str(videoTrack.definition))
			layout_video.addWidget(label,0,1)

			label = QtGui.QLabel("Frame-rate: ")
			layout_video.addWidget(label,1,0)
			label = QtGui.QLabel(str(videoTrack.framerate))
			layout_video.addWidget(label,1,1)

			label = QtGui.QLabel("Codec: ")
			layout_video.addWidget(label,2,0)
			label = QtGui.QLabel(str(videoTrack.codec))
			layout_video.addWidget(label,2,1)

		# for each audio track
		for i in range(0,len(node.audioTracks)):
			audioTrack = node.audioTracks[i]

			gb_audio = QtGui.QGroupBox("Audio " + str(i))
			layout.addWidget(gb_audio,i,1)
			layout_audio = QtGui.QGridLayout()
			gb_audio.setLayout(layout_audio)

			label = QtGui.QLabel("Language: ")
			layout_audio.addWidget(label,0,0)
			label = QtGui.QLabel(str(audioTrack.language))
			layout_audio.addWidget(label,0,1)

			label = QtGui.QLabel("Format: ")
			layout_audio.addWidget(label,1,0)
			label = QtGui.QLabel(str(audioTrack.format))
			layout_audio.addWidget(label,1,1)

			label = QtGui.QLabel("Default: ")
			layout_audio.addWidget(label,2,0)
			label = QtGui.QLabel(str(audioTrack.default))
			layout_audio.addWidget(label,2,1)

			label = QtGui.QLabel("Forced: ")
			layout_audio.addWidget(label,3,0)
			label = QtGui.QLabel(str(audioTrack.forced))
			layout_audio.addWidget(label,3,1)

		# for each subtitle track
		for i in range(0,len(node.subtitleTracks)):
			subtitleTrack = node.subtitleTracks[i]

			gb_subtitles = QtGui.QGroupBox("Subtitle " + str(i))
			layout.addWidget(gb_subtitles,i,2)
			layout_subtitles = QtGui.QGridLayout()
			gb_subtitles.setLayout(layout_subtitles)

			label = QtGui.QLabel("Language: ")
			layout_subtitles.addWidget(label,0,0)
			label = QtGui.QLabel(str(subtitleTrack.language))
			layout_subtitles.addWidget(label,0,1)

			label = QtGui.QLabel("Format: ")
			layout_subtitles.addWidget(label,1,0)
			label = QtGui.QLabel(str(subtitleTrack.format))
			layout_subtitles.addWidget(label,1,1)

			label = QtGui.QLabel("Default: ")
			layout_subtitles.addWidget(label,2,0)
			label = QtGui.QLabel(str(subtitleTrack.default))
			layout_subtitles.addWidget(label,2,1)

			label = QtGui.QLabel("Forced: ")
			layout_subtitles.addWidget(label,3,0)
			label = QtGui.QLabel(str(subtitleTrack.forced))
			layout_subtitles.addWidget(label,3,1)

