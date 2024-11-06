from flask import Flask, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# Ruta para servir imágenes
@app.route('/imagenes/<path:filename>')
def serve_image(filename):
    return send_from_directory('imagenes', filename)

def get_data():
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM votaciones WHERE ruta_imagen IS NOT NULL AND ruta_imagen != ''")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
