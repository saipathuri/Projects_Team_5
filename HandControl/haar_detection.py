import numpy as np
import cv2
import matplotlib as mp
import motor
import car_dir as turn
import time
from threading import Thread

cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

motor.setup()
turn.setup()
turn.home()

scanning_delay = .5

while True:


	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		if x < 215:
			Thread(target = left_forward).start()
		elif x > 215 and x < 430:
			Thread(target = forward).start()
		else:
			Thread(target = right_forward).start()

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	print "waiting for scanning_delay"
	time.sleep(scanning_delay)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

def forward():
	print "go forward"
	motor.forwardWithSpeed()
	time.sleep(1)
	motor.stop()

def right_forward():
	print "turn right"
	turn.turn_right()
	motor.forwardWithSpeed()
	time.sleep(1)
	motor.stop()
	turn.home()

def left_forward():
	print "turn left"
	turn.turn_left()
	motor.forwardWithSpeed()
	time.sleep(1)
	motor.stop()
	turn.home()
