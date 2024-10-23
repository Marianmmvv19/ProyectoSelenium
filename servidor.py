from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('votaciones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM votaciones")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
