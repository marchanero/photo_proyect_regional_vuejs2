from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, LargeBinary
from config.db import meta, engine


users = Table(
    "users",
    meta,
    Column("id_participante", Integer, primary_key=True),
    Column("sexo", String(255)),
    Column("etnia", String(255)),
    Column("estadocivil", String(255)),
    Column("niveleducativo", String(255)),
    Column("profesion", String(255)),
    Column("situacionprofesional", String(255)),
    Column("poblacion", String(255)), 
    Column("lugarderesidencia", String(255))
)

photo = Table("photo", 
    meta, 
    Column("id", Integer, primary_key=True),
    Column("id_participant", String(255)),
    Column("title", String(255)), 
    Column("description", String(255)), 
    Column("img", LargeBinary ))

meta.create_all(engine)
