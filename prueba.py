import psycopg2

# sudo service postgresql start

# Cadena de conexión
connection_string = "dbname='vscode' user='vscode' password='password' host='localhost' port='5432'"

# Conectar a la base de datos
try:
    conn = psycopg2.connect(connection_string)
    print("Conexión exitosa")
    conn.close()
except Exception as e:
    print(e)