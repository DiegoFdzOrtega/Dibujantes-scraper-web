from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def consultar_db():
    conexion = sqlite3.connect('dibujantes.db')
    cursor = conexion.cursor()
    # Seleccionamos todos los videos
    cursor.execute("SELECT id, titulo, url FROM videos")
    datos = cursor.fetchall()
    conexion.close()
    return datos

@app.route('/')
def home():
    videos = consultar_db()
    # Le pasamos los datos al HTML
    return render_template('index.html', lista=videos)

if __name__ == '__main__':
    print("Servidor corriendo en http://127.0.0.1:5000")
    app.run(debug=True)