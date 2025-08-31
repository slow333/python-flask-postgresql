import sys
sys.path.append('B:\\python\\window-flask')

from sqlalchemy import select
from db.users.connect_db import engine
from db.users.create_users_table import users

sel_users = select([users])
sel_with_id = select([users.c.lname, users.c.fname]).where(users.c.id == 4)

all_users =[]

with engine.connect() as conn:
  for user in conn.execute(sel_users):
    all_users.append(user)
  for user in conn.execute(sel_with_id):
    print(user)