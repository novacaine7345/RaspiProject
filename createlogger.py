import sqlite3

def idb(Query):
	conn = sqlite3.connect("master.db")
	cursor = conn.cursor()
	cursor.execute(Query)
	conn.commit()
	conn.close()

def main():
	Query = """
		CREATE TABLE master_logger(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		log_time TEXT,
		product_id INTEGER,
		origin TEXT,
		destination TEXT,
		size TEXT,
		str_type TEXT,
		mat_type TEXT,
		exp_type TEXT,
		req_ETA INTEGER,
		actual_time INTEGER,
		status TEXT
		);
		"""
	idb(Query)
if __name__ == "__main__":
	main()
