import sys
sys.path.append('B:\\python\\window-flask')

from sqlalchemy import insert
from db.users.connect_db import engine
from db.users.create_users_table import users

ins_user = users.insert().values([
  {'fname': 'Jane', 'lname': 'Doe'},
  {'fname': 'Alice', 'lname': 'Smith'},
  {'fname': 'Bob', 'lname': 'Johnson'},
  {'fname' : 'Jasica', 'lname': 'Masion'},
  {'fname': '관용', 'lname': '김'}
])


with engine.connect() as conn:
  conn.execute(ins_user)