import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sqlite_db = "../database_movie.sqlite"
base_dir = os.path.dirname(os.path.relpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_db)}"

engine =  create_engine(database_url,  echo=True)

session =  sessionmaker(bind=engine)

db_td = declarative_base()