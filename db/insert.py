from sqlalchemy import insert
from db_config import engine, users, addresses

ins = users.insert().values([
  {'name': 'Jane', 'fullname': 'Jane Doe'},
  {'name': 'Alice', 'fullname': 'Alice Smith'},
  {'name': 'Bob', 'fullname': 'Bob Johnson'}
])

ins_add = addresses.insert().values([
  {'user_id': 1, 'email_address': 'john.doe@example.com'},
  {'user_id': 2, 'email_address': 'alice.smith@example.com'},
])
with engine.connect() as conn:
  conn.execute(ins)
  conn.execute(ins_add)