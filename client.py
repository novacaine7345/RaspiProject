import socket
import sqlite3

def getfromdb(Query):
	conn = sqlite3.connect("master.db")
	cursor = conn.cursor()
	cursor.execute(Query)
	rows = cursor.fetchall()
	
	return rows

HOST = "172.16.16.138"   # server IP
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
print("Connected to server")

while True:
    msg = input("Request unique ID : ")
    client.sendall(msg.encode())

    data = client.recv(1024)
    print("Server:", data.decode())

client.close()
