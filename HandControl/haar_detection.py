import numpy as np
import cv2
import matplotlib as mp
import motor
import car_dir as turn
import time
from threading import Thread

cap = cv2.VideoCapture(0)
cascPath = "closed_frontal_palm.xml"
handCascade = cv2.CascadeClassifier(cascPath)

motor.setup()
turn.setup()
turn.home()

def forward():
	turn.home()
	print "go forward"
	motor.forwardWithSpeed(spd=100)
	time.sleep(1)
	motor.stop()

def right_forward():
	turn.home()
	print "turn right"
	turn.turn_right()
	motor.forwardWithSpeed(spd=100)
	time.sleep(1)
	motor.stop()
	turn.home()

def left_forward():
	print "turn left"
	turn.home()
	turn.turn_left()
	motor.forwardWithSpeed(spd=100)
	time.sleep(1)
	motor.stop()
	turn.home()

while True:
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	hands = handCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

	for (x, y, w, h) in hands:
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

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
