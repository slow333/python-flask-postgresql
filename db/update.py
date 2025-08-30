from sqlalchemy import update
from db_config import engine, users

stmt = users.update().where(users.c.name == 'Jane').values(fullname='Jane Doe Updated')
with engine.connect() as conn:
  conn.execute(stmt)