# first of all import the socket library
import socket    
import cv2   
import numpy     
 
# next create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print ("Socket successfully created")

port = 11206            
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port)) 
print ("socket binded to %s" % port)

i = 0
s.listen(1)
print ("socket is listening")

c, addr = s.accept()
print(addr)

# while True:
data = c.recv(40906000)
rcv_img = open('rcv_img.jpg', 'wb')
rcv_img.write(data)
rcv_img.close()
c.send(b'received img')

c.close()
