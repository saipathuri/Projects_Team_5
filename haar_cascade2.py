import numpy as np
import cv2
import matplotlib as mp
import motor
import car_dir as turn
import time
import video_dir as camTurn
from threading import Thread

cap = cv2.VideoCapture(0)
cascPath = "closed_frontal_palm.xml"
handCascade = cv2.CascadeClassifier(cascPath)

motor.setup()
turn.setup()
turn.home()

def forward():
	turn.home()
	print("go forward")
	motor.forwardWithSpeed(spd=100)
	time.sleep(1)
	motor.stop()

def right_forward():
	turn.home()
	print("turn right")
	turn.turn_right()
	motor.forwardWithSpeed(spd=100)
	time.sleep(1)
	motor.stop()
	turn.home()

def left_forward():
	print("turn left")
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
	num_hands = len(hands)

   	if num_hands == 0:
		total += 1
	else:
		total = 0
    
    	if total > 15:
        	total = 0
        	camTurn.Current_x = 0
        	pwm.write(14,0,camTurn.Current_x)
        
        	while camTurn.Current_x < 640 or num_hands == 0:
            		Thread(target = move_increase_x).start()
            		hands
            		num_hands
    
	for (x, y, w, h) in hands:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		if x > 215 and x < 430
            if camTurn.Current_x < 295:
                Thread(target = left_forward).start()
			elif camTurn.Current_x > 345
                Thread(target = right_forward).start()
            else:
                Thread(target = forward).start()
		else:
			if x < 215:
				Thread(target = move_decrease_x).start()
			else:
				Thread(target = move_increase_x).start()

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
