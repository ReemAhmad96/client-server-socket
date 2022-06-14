import socket			     #line 1: Import socket module
ser= socket.socket()		     #line 2: create a socket object
host = socket.gethostname()	      #line 3: Get current machine name
port = 6666		            #line 4: Get port number for connection
ser.bind((host,port))		            #line 5: bind with the address
print("Waiting for connection...")
ser.listen(6)			            #line 6: listen for connections

while True:
	conn,addr = ser.accept()	    #line 7: connect and accept from client
	print('Got new Connection from', addr)
	message=conn.recv(1024).decode()
	print(message)
	conn.send('Server Saying Hi'.encode())
	conn.close()	          #line 15: Close the connection
