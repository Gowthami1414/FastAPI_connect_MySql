from sqlalchemy import create_engine #sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE ="mysql+pymysql://root:<give password>@localhost:<give port>/myfastapi_db" #if your password contains '@'in between the replace that with" %40 " instead of '@'

engine=create_engine(URL_DATABASE)

sessionlocal=sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base=declarative_base()
