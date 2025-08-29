from sqlalchemy import select
from db_config import engine, users, addresses

select_all = select([users])
users_select = select([users]).where(users.c.name == 'Jane')
with engine.connect() as conn:
  for row in conn.execute(select_all): print(row)
  for row in conn.execute(users_select): print(row)
