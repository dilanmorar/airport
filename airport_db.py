import pyodbc

# these are our variables to connect
server = 'localhost,1433'
database = 'airport'
username = 'SA'
password = 'Passw0rd2018'

# making the connection
docker_airport = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# making a cursor
cursor = docker_airport.cursor()

# execute some sql commands
cursor.execute("Select * from passenger")

row = cursor.fetchone()
print(row)