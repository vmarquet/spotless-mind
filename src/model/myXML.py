#!/usr/bin/python3.2

def add_sub_dir(file_dom, node, father):
	new_node = file_dom.createElement(node.name)
	father.appendChild(new_node)
	return new_node

def add_file_to_dir(file_dom, node, father):
	new_node = file_dom.createElement(node.name)
	father.appendChild(new_node)
	return new_node