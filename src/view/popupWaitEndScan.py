#!/usr/bin/python
# -*-coding:Utf-8 -*


from PyQt4 import QtGui, QtCore

class popupWaitEndScan(QtGui.QDialog):

	def __init__(self):
		QtGui.QDialog.__init__(self)

		self.closeThisPopup = False
		self.setWindowTitle("Scanning...")

		label = QtGui.QLabel("\
Please wait for the scan to complete. \n \
This can be long if there is a lot of files (several thousands) \n \
or if the metadata analysis with MediaInfo is activated.")

		layout = QtGui.QGridLayout()
		self.setLayout(layout)
		layout.addWidget(label)


	# we redefine the event handler because this popup musn't be closed
	# until the scan is finished
	def closeEvent(self, event):
		if self.closeThisPopup == False:
			event.ignore()
		if self.closeThisPopup == True:
			# event.accept()  # doesn't work !?
			super(popupWaitEndScan, self).accept()

	def closePopup(self):
		self.closeThisPopup = True
		self.closeEvent(QtCore.QEvent(QtCore.QEvent.Close))
