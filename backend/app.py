from flask import Flask, jsonify
from flask_cors import CORS
import pymysql
import os
import time

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'database'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'devops_pass_2026'),
        database=os.environ.get('DB_NAME', 'pacific_fest'),
        autocommit=True
    )

# SECCIÓN DE ESPERA ACTIVA: Espera a que MySQL configure e inicie la DB por completo
print("Esperando a que la base de datos MySQL esté lista...")
tabla_creada = False

for intento in range(15): # Va a intentar 15 veces (esperando 3 segundos entre cada intento)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Si logra conectarse, crea la tabla de inmediato
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS artistas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
            )
        """)
        
        # Inserta los artistas si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM artistas")
        if cursor.fetchone()[0] == 0:
            artistas = [('Docker Band'), ('The Kubernetes'), ('Microservices Crew'), ('Continuous Integration')]
            cursor.executemany("INSERT INTO artistas (nombre) VALUES (%s)", artistas)
            
        cursor.close()
        conn.close()
        print("¡Base de datos y tabla configuradas con éxito!")
        tabla_creada = True
        break
    except pymysql.MySQLError as e:
        print(f"MySQL no está listo aún (Intento {intento+1}/15)... Esperando 3 segundos.")
        time.sleep(3)

if not tabla_creada:
    print("ERROR CRÍTICO: No se pudo inicializar la tabla después de varios intentos.")

@app.route('/api/concierto', methods=['GET'])
def get_concierto():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM artistas")
        rows = cursor.fetchall()
        artistas = [r[0] for r in rows]
        cursor.close()
        conn.close()
        return jsonify({
            "festival": "Pacific DevOps Music Fest",
            "fecha": "15 de Julio de 2026",
            "artistas": artistas
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)