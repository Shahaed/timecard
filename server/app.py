import sqlite3
import json
from flask import Flask
app = Flask(__name__)

conn = sqlite3.connect('timecard.db')


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def hello():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute('''SELECT * from account''')

    rows = c.fetchall()
    conn.close()
    return json.dumps(rows)


@app.route("/task", methods=["POST"])
def handle_add_task():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    deliverable = request.form['deliverable']
    date = request.form['date']

    # Select from table here:
    pass


if __name__ == '__main__':
    app.run()
