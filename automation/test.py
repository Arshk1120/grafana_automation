import pymysql

# Database connection details
host = "localhost"
user = "arshdeep"
password = "arsh123"
database = "grafanadb"

# Connect to the database
conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()

# Test connection
cur.execute("SELECT 1")
print(cur.fetchone())

# Close the connection
conn.close()

