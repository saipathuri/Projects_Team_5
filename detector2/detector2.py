###############################################################################
#
#	detection model class
#	
#	Member Variables:
#		* model.loadNet() # Loads the caffe model and the prototxt
#		* model()
#		* model.getInstances( objectType, image ) #	Returns a list of the objects
#													of type objectType
#		
#
################################################################################

import numpy as np
import cv2
import time

class Model:

	def __init__(self):
		self.net = None # The Caffe Model
		self.classes = ["background", "aeroplane", "bicycle", "bird", "boat",
						"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
						"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
						"sofa", "train", "tvmonitor"]

	def loadNet(self):
		print("[INFO] Loading Model")
		self.net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')

	def getInstances(self, objectType, image):
		blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
		self.net.setInput(blob)
		detections = self.net.forward()
		pass

a = Model()
a.loadNet()
img = cv2.imread('photo.jpg', 1)
a.getInstances('person', img)
