from sqlalchemy import select, join
from db_config import engine, users, addresses
import sqlalchemy

print(sqlalchemy.__version__)
j = join(users, addresses, users.c.id == addresses.c.user_id)
inner_join = select([users.c.name, addresses.c.email_address]).select_from(j)
print(str(inner_join))

oj = join(users, addresses, users.c.id == addresses.c.user_id, isouter=True)
left_outer_join = (
  select([users, addresses])
  .select_from(oj)
  )
print(str(left_outer_join))

with engine.connect() as conn:
  result = conn.execute(inner_join)
  for row in result:
    print(row)
  for row in conn.execute(left_outer_join):
    print(row)