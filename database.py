import sqlite3

# Turn service_requests.db into a constant for readability and editability purposes.
DATABASE_NAME = "service_requests.db"

def create_db():

"""Create the database and insert sample data if it doesn't already exist"""

# Open the database connection.
conn = sqlite3.connect(DATABASE_NAME)

# Initiate the cursor, which is your database assistant for executing commands.
cursor = conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS service_requests (
	id INTEGER PRIMARY KEY,
	description TEXT NOT NULL, 
	customer_name TEXT NOT NULL, 
	customer_email TEXT NOT NULL
	)
	""")

# Check the row count to avoid multiple insertions.
cursor.execute("SELECT COUNT(*) FROM service_requests")
count = cursor.fetschone()[0]

if count == 0:
	sample_requests = [
	(
		1,
		"Replace ATM receipt printer", 
		"Adam Johnson",
		"adam.johnson@gmail.com"
	),
	(

		2,
		"Install software update",
		"Stephan Balus",
		"Stephan.Balus@gmail.com"
	)
	(

		3,
		"Investigate cash dispenser fault",
		"John Doe"
		"john.doe@gmail.com"
	)

# Execute a range of INSERT commands with executemany.
# Making use of '?' as placeholders which is good practice against SQL injections.

cursor.executemany(
	"""
	INSERT INTO service_requests
	(id, description, customer_name, customer_email)
	VALUES (?,?,?,?)
	""",
	sample_requests
	)

# Commit and close the database.
conn.commit()
conn.close()

def get_service_request(request_id):

"""Return a service request as a dictionairy, so it can be passed into jsonify."""

conn = sqlite3.connect(DATABASE_NAME)

# row_factory allows you to return rows using the column names improving readability.

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute(

	"SELECT * FROM service_requests WHERE id = ?",
	(request_id,)
)

row = cursor.fetchone()

conn.close()

if row is None:
	return None

	return {
		"id": row[id],
		"description": row["description"],
		"customer_name": row["customer_name"],
		"customer_email": row["customer_email"]
		}
