"""main.py"""
"""Data Types:
    String, Text, Integer, SmallInteger, BigInteger, Numeric, Float, Boolean, DateTime, Date, Time
"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import text

engine = create_engine("sqlite:///college.db", echo=True)
meta = MetaData()
conn = engine.connect()

# students = Table(
#     'students', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String)
# )
# meta.create_all(engine)

# Reflect the "students" table from the database
students = Table('students', meta, autoload_with=engine)


with engine.connect() as conn:
    conn.execute(students.insert(), [
        {'name': 'Alice'},
        {'name': 'Bob'},
        {'name': 'Charlie'},
        {'name': 'David'},
        {'name': 'Eva'},
        {'name': 'Frank'},
        {'name': 'Grace'},
        {'name': 'Hank'},
        {'name': 'Ivy'},
        {'name': 'Jack'},
        {'name': 'Katie'},
        {'name': 'Liam'},
        {'name': 'Mia'},
        {'name': 'Nathan'},
        {'name': 'Olivia'},
        {'name': 'Paul'},
        {'name': 'Quinn'},
        {'name': 'Ryan'},
        {'name': 'Sophia'},
        {'name': 'Tyler'},
        # Add more names as needed
    ])
    # Commit the transaction
    conn.commit()

# select the the data
s = students.select()
# s = text("select * from students where id > 10")
result = conn.execute(s).fetchall()

for obj in result:
    print(obj)