from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

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

@app.route('/')
def index():
    # Create a cursor object
    cur = conn.cursor()
    
    # Execute the SELECT query
    cur.execute('SELECT * FROM FootballPlayers')
    
    # Fetch all results from the executed query
    rows = cur.fetchall()
    
    # Close the cursor
    cur.close()
    
    # Convert rows to a list of dictionaries
    results = [{'ID': row[0], 'Name': row[1], 'Age': row[2], 'Job': row[3], 'Country': row[4], 'Married': row[5], 'YearsEmployed': row[6]} for row in rows]
    
    return jsonify(results)

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

