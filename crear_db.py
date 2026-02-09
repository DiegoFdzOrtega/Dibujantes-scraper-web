import sqlite3

def preparar_proyecto():
    conexion = sqlite3.connect('dibujantes.db')
    cursor = conexion.cursor()
    
    # Creamos una tabla sencilla para empezar
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            url TEXT
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("✅ Base de datos 'dibujantes.db' creada correctamente.")

preparar_proyecto()