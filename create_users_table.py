import sys
sys.path.append('B:\\python\\window-flask')

from sqlalchemy import MetaData # type: ignore
from sqlalchemy import Table, Column, String, Integer # type: ignore
from db.users.connect_db import engine

metadata = MetaData()

# create table
users = Table('users', metadata,
  Column('id', Integer, primary_key=True),
  Column('fname', String(40)),
  Column('lname', String(30))
)

metadata.create_all(engine)