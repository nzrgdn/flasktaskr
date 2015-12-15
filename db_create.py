# db_create.py


from datetime import date

from project import db
from project.models import Task, User

# create the database and the db table
db.create_all()


# commit the changes
db.session.commit()