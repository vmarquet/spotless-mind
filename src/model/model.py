#!/usr/bin/python2.7
# -*-coding:Utf-8 -*


class model:
	"""Model class as in MVC pattern: to store parameters and data. Singleton pattern."""

	# static attributes:
	version = "0.5"
	root_node_list = list()
	model_dir = None
	scan_thread = None  # we must keep a reference to the thread,
		                        # else it's garbage collected before it's end
	root_item_list = list()
	# parameters:
	recordHiddenFiles = False  # to record hidden or temporary files such as .* or *~ 
	recordVideoMetadatas = True  # to record video metadatas with pyMediaInfo