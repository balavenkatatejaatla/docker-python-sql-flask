import pyodbc

# Establish connection to Azure SQL Database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=testpy.database.windows.net,1433;'
    'DATABASE=venkatdb;'
    'UID=mysqladmin@testpy;'
    'PWD=Password@123;'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=30;'
)

# Create a cursor object
cur = conn.cursor()

# Execute the SELECT query
cur.execute('SELECT * FROM FootballPlayers')

# Fetch all results from the executed query
rows = cur.fetchall()

# Iterate over the results and print each row
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

