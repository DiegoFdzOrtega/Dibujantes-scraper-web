import yt_dlp
import sqlite3

# Configuración básica para no descargar el video, solo leer info
opciones = {
    'quiet': True,
    'extract_flat': True,
    'force_generic_extractor': True,
}

# Puedes cambiar esta URL por tu dibujante favorito
url_canal = "https://www.youtube.com/@Jazza/videos" 

print("Copiando datos de YouTube... espera un poco...")

with yt_dlp.YoutubeDL(opciones) as ydl:
    info = ydl.extract_info(url_canal, download=False)
    # Cogemos los primeros 5 videos para probar
    videos = info['entries'][:5]

# Guardamos en la base de datos
conexion = sqlite3.connect('dibujantes.db')
cursor = conexion.cursor()

for v in videos:
    cursor.execute("INSERT INTO videos (titulo, url) VALUES (?, ?)", (v['title'], v['url']))

conexion.commit()
conexion.close()
print("✅ ¡Vídeos guardados en la base de datos!")