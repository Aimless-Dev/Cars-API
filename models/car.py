from sqlalchemy import Column, Table
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import String, Integer

cars = Table(
    'cars',
    meta,
    Column('id', String(225), primary_key=True),
    Column('marca', String(255)),
    Column('modelo', String(255)),
    Column('precio', Integer, nullable=False)
)

meta.create_all(engine)