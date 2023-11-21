"""psql.py 
Postgresql database with create data
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:admin@localhost/sqlalchemy_db')  # lowercase database name
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = "student"  # corrected table name
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)

# Base.metadata.create_all(engine)

# Insert the data
# st = [
#     Student(name="Rajib Mahmud", address="Keraniganj, Dhaka", email="rajib.conf@gmail.com"),
#     Student(name="Rayhan", address="Barishal", email="rayhan@gmail.com")
# ]

# session.add_all(st)
# session.commit()


result = session.query(Student).all()

for obj in result:
    print(obj.name)
