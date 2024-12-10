import pymysql

# Database connection details
host = "localhost"
user = "arshdeep"
password = "arsh123"
database = "grafanadb"

# Connect to the database
conn = pymysql.connect(host=host, user=user, password=password, database=database)
cur = conn.cursor()

# Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS cpu_metrics (
    id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cpu_usage DECIMAL(5, 2) UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL
)
"""
cur.execute(create_table_query)

# Insert data into the table
insert_query = """
INSERT INTO cpu_metrics (cpu_usage, created_at) VALUES
(10.55, '2021-03-27 08:00:00'),
(15.10, '2021-03-27 08:01:00'),
(12.62, '2021-03-27 08:02:00'),
(17.80, '2021-03-27 08:03:00'),
(21.00, '2021-03-27 08:04:00')
"""
cur.execute(insert_query)
conn.commit()

# Close the connection
conn.close()

