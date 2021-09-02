from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import relationship
class User(BaseModel):
    
    id: Optional[int]
    id_participante: int
    sexo: str
    etnia: str
    estadocivil: str
    niveleducativo: str 
    profesion: str
    situacionprofesional: str
    poblacion: str
    lugarderesidencia:str

class UserCount(BaseModel):
    total: int

class Photo (BaseModel):
    id: Optional[int]
    id_participant: str
    title: str
    description: str 
    img: str