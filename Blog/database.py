from sqlalchemy import create_engine #sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE ="mysql+pymysql://root:Gowthu%40149@localhost:3306/myfastapi_db"

engine=create_engine(URL_DATABASE)

sessionlocal=sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base=declarative_base()