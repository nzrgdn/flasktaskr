from views import db
from _config import DATABASE_PATH

import sqlite3
from datetime import datetime

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()
	c.execute("""alter table users rename to old_users""")
	db.create_all()
	c.execute("""select name, email, password 
		from old_users order by id asc""")

	data = [ (row[0], row[1], row[2], 'user') for row in c.fetchall() ]

	c.executemany("""insert into users (name, email, password, role) values (?, ?, ?, ?)""", data)

	c.execute("drop table old_users")