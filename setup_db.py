import psycopg2

# Cadena de conexión
connection_string = "postgres://vscode:password@localhost:5432/vscode"

# Conectar a la base de datos
try:
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    
    # Crear tabla
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE NOT NULL
    );
    '''
    cur.execute(create_table_query)
    conn.commit()
    print("Tabla 'users' creada exitosamente")
    
    # Insertar datos de ejemplo
    insert_data_query = '''
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
    ON CONFLICT DO NOTHING;
    '''
    cur.execute(insert_data_query)
    conn.commit()
    print("Datos insertados exitosamente en la tabla 'users'")
    
    # Leer y mostrar los datos de la tabla
    select_query = "SELECT * FROM users;"
    cur.execute(select_query)
    rows = cur.fetchall()
    print("Datos en la tabla 'users':")
    for row in rows:
        print(row)
    
    # Cerrar la conexión
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error al conectar a la base de datos o ejecutar consultas: {e}")
