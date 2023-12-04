from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base



DB_URL = "Здесь ваша ссылка на базу POSTGRESQL"



engine = create_engine(DB_URL)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
