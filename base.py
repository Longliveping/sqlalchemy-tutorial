from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql://localhost/sqlalchemy')
engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()