from database import engine
from models import User
from database import Base

Base.metadata.create_all(bind=engine)

print("Tables created successfully")