from flask import Flask, render_template_string, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    db_config = {
        'host': os.environ.get('DB_HOST', 'localhost'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', ''),
        'database': os.environ.get('DB_DATABASE', 'score'),
        'port': int(os.environ.get('DB_PORT', 3306))
    }
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Run hello world query
        cursor.execute('SELECT "This is an example application deployed with Score!" as message')
        rows = cursor.fetchall()
        message = rows[0][0]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify(error=str(err)), 500
    finally:
        cursor.close()
        connection.close()

    html = """
    <html>
      <body>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
        <div class="container text-center mt-5 pt-5">
          <h1>Hello World!</h1>
          <p>{}</p>
        </div>
      </body>
    </html>
    """.format(message)

    return render_template_string(html)

@app.route('/health')
def health():
    return jsonify(status="healthy"), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    try:
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Something bad happened: {e}")
