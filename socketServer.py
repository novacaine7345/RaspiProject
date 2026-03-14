import socket
import sqlite3

def getfromdb(Query):
	conn = sqlite3.connect("master.db")
	cursor = conn.cursor()
	cursor.execute(Query)
	rows = cursor.fetchall()
	return rows
	conn.close()
def socketServerPi():
	host = '0.0.0.0'
	port = 6000

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((host, port))
	server.listen()

	print("Server listening on port: ", port)

	conn, addr = server.accept()

	while True:
		data = conn.recv(1024)
		if not data:
			break
		message = data.decode()
		print("Message received : ", message)
		Query = f"select * from master_orders where id = \"{message}\" ;"
		rows = getfromdb(Query)
		reply = str(rows)
		conn.sendall(reply.encode())
	conn.close()
	server.close()
