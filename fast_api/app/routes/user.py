from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User, UserCount
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)


@user.get(
    "/users",
    tags=["users"],
    response_model=List[User],
    description="Get a list of all users",
)
def get_users():
    return conn.execute(users.select()).fetchall()


@user.get("/users/count", tags=["users"], response_model=UserCount)
def get_users_count():
    result = conn.execute(select([func.count()]).select_from(users))
    return {"total": tuple(result)[0][0]}


@user.get(
    "/users/{id}",
    tags=["users"],
    response_model=User,
    description="Get a single user by Id",
)
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

#Creacion del usuario
@user.post("/users", tags=["users"], response_model=User, description="Create a new user from web")
def create_user(user: User):
    new_user = {
                "id_participante": user.id_participante,
                "sexo": user.sexo,
                "etnia": user.etnia,
                "estadocivil": user.estadocivil,
                "niveleducativo": user.niveleducativo,
                "profesion": user.profesion,
                "situacionprofesional": user.situacionprofesional,
                "poblacion": user.situacionprofesional,
                "lugarderesidencia": user.lugarderesidencia
                
                }
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id_participante == result.lastrowid)).first()


@user.put(
    "users/{id}", tags=["users"], response_model=User, description="Update a User by Id"
)
def update_user(user: User, id: int):
    conn.execute(
        users.update()
        .values(name=user.name, email=user.email, password=user.password)
        .where(users.c.id == id)
    )
    return conn.execute(users.select().where(users.c.id_participante == id)).first()


@user.delete("/{id}", tags=["users"], status_code=HTTP_204_NO_CONTENT)
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id_participante == id)).first()
