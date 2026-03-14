import csv
import sqlite3

def insert_db(Query):
	conn = sqlite3.connect('master.db')
	cursor = conn.cursor()
	cursor.execute(Query)
	conn.commit()
	conn.close()

def main():
	create_db()
	print("Master table Created")
	origin = ""
	destination = ""
	size = ""
	str_type = ""
	mat_type = ""
	exp_type = ""
	Ap = ['ATL', 'DXB', 'DFW', 'HND', 'LHR', 'DEN', 'IST', 'ORT', 'DEL', 'PVG']
	with open('Shipping_timings.csv', mode='r') as file:
		csvFile = csv.reader(file)
		for lines in csvFile:
			id = lines[0]
			origin = Ap[int(lines[6])-1]
			destination = Ap[int(lines[7])-1]
			x = int(lines[1])
			if x == 1 :
				size = "small"
			elif x == 2 :
				size = "medium"
			elif x == 3 :
				size = "large"
			str_type = "short" if lines[2] == '1' else "long"
			mat_type = "Perishable" if lines[3] == '1' else "Non-Perishable"
			exp_type = "True" if lines[5] == '1' else "False"
			ETA = int(lines[4])
			#print(id, origin, destination, size, str_type, mat_type, exp_type, ETA)
			Query = f"""
				INSERT INTO master_orders(origin, destination, size, str_type, mat_type, exp_type, req_ETA) VALUES
				(\"{origin}\", 
			 	\"{destination}\", 
			 	\"{size}\", 
			 	\"{str_type}\",
			 	\"{mat_type}\", 
			 	\"{exp_type}\", 
			 	\"{ETA}\");
				"""
			insert_db(Query)
	#create_db()
def create_db():
	Query = f"""
		CREATE TABLE IF NOT EXISTS master_orders(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		origin TEXT,
		destination TEXT,
		size TEXT,
		str_type TEXT,
		mat_type TEXT,
		exp_type TEXT,
		req_ETA INTEGER
		);
		"""
	insert_db(Query)

if __name__ == '__main__' :
	main()
