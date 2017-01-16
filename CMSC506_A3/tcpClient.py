# Riley Hanson
# CMSC 506: Socket Programming Assignment 1
import sys
from socket import*

def main():
	server_host = ''
	server_port = 6789
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.connect((server_host, server_port))

	message = raw_input("-> ")
	while message != 'q':
		serverSocket.send(message)
		data = serverSocket.recv(1024)
		print "Received from server: " + str(data)
		message = raw_input("-> ")
	serverSocket.close()

if __name__ == '__main__':
	main()