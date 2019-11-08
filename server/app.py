import sqlite3
from flask import Flask
app = Flask(__name__)

conn = sqlite3.connect('timecard.db')


@app.route('/')
def hello():
    c = conn.cursor()
    c.execute('''SELECT * from account''')

    rows = c.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    app.run()
