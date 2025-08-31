from sqlalchemy import create_engine # type: ignore

engine = create_engine('postgresql://postgres:1111@localhost:5432/mydb')