#!/usr/bin/python3.2
# -*-coding:Utf-8 -*


class model:
	"""Model class as in MVC pattern: to store parameters and data. Singleton pattern."""

	# static attributes:
	version = "0.5"
	root_node_list = list()
	# parameters:
	recordHiddenFiles = False  # to record hidden or temporary files such as .* or *~ 
	recordVideoMetadatas = True  # to record video metadatas with pyMediaInfo