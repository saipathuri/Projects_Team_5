# Import socket module
import socket 
import cv2
import numpy              
 
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define the port on which you want to connect
port = 11206 
 
# connect to the server on local computer
# receive data from the server
s.connect(('127.0.0.1', port))
filename = "sample1_l.jpg"


img = open(filename, "rb")
data = img.read()
img.close()

# capture = cv2.VideoCapture(0)
# ret, frame = capture.read()

# encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
# result, imgencode = cv2.imencode('.jpg', frame, encode_param)
# data = numpy.array(imgencode)
# stringData = data.tostring()

# sock.send( str(len(stringData)).ljust(16));
s.send(data);

print('client: ' + str(s.recv(1024))


# s.close()
# close the connection

