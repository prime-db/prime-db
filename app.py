from flask import Flask, render_template, request
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="prime_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        port=5432
    )
    return conn

@app.route("/")
def home():
    degree_filter = request.args.get('degree')
    conn = get_db_connection()
    cur = conn.cursor()
    if degree_filter:
        cur.execute("SELECT * FROM belyi WHERE LEFT(label, 1) = %s;", (degree_filter,))
    else:
        cur.execute("SELECT * FROM belyi;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', belyi=data, selected_degree=degree_filter)

@app.route('/<belyi_index>')
def profile(belyi_index):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM belyi WHERE index = %s', (belyi_index,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('profile.html', belyi=data)

if __name__ == "__main__":
    app.run(port=1972)

