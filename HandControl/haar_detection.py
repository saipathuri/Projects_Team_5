import numpy as np
import cv2
import matplotlib as mp
import motor
import car_dir as turn
import time

cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

motor.setup()
turn.setup()
turn.home()

scanning_delay = 2

while True:
	time.sleep(scanning_delay)
	
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		if x < 215:
			print "turn left"
			turn.turn_left()
			motor.forwardWithSpeed()
			time.sleep(1)
			motor.stop()
			turn.home()
		elif x > 215 and x < 430:
			print "go forward"
			motor.forwardWithSpeed()
			time.sleep(1)
			motor.stop()
		else:
			print "turn right"
			turn.turn_right()
			motor.forwardWithSpeed()
			time.sleep(1)
			motor.stop()
			turn.home()

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
