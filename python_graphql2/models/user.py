from conn.db import meta
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String


users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("email", String(50)),
    Column("password", String(50)),
)
