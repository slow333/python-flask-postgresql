from sqlalchemy import delete
from db_config import engine, users

stmt = users.delete().where(users.c.name == 'Jane')
with engine.connect() as conn:
  conn.execute(stmt)