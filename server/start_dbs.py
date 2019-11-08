import sqlite3
conn = sqlite3.connect('timecard.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE timesheet
            (id integer not null primary key, date text, employee_id text, \
            start_time text, end_time text, date_submitted text)''')
c.execute('''CREATE TABLE account(id integer not null primary key,\
           first_name text, last_name text, login_id text, email text, password text,\
           role_id integer)''')
# Insert a row of data
c.execute(
    "INSERT INTO account VALUES (1,'test','subject','tsubject','snehalvartak@iseinc.biz',\
   'test123', 1)")
# Save (commit) the changes
conn.commit()
# c.execute('''SELECT * from account''')
# print(c.fetchone())
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
