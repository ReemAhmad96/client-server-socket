#This is tcp_client.py script
import socket
cli = socket.socket()
host = socket.gethostname()	        # Get current machine name
port = 6666		                # Client wants to connect to server's
				                    # port number 6666
cli.connect((host,port))
message=input("enter message")
cli.send(message.encode())
print(cli.recv(1024).decode())	            # 1024 is bufsize or max amount
				                    # of data to be received at once
cli.close()
