from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can use os.environ to access your variables

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
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM belyi;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', belyi=data)

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
    app.run()

