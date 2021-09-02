from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user


app = FastAPI(title="Users API",
              description="a REST API using python and mysql",
              version="0.0.1",)
origins = [
    "api-test.emosys.site:5001",
    "http://api.emosys.site"
    "https://api.emosys.site",
    "http://emosys.site",
    "https://emosys.site",
    "proyectofotos.emosys.site"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # max_age=3600,
)

app.include_router(user)


@app.get("/", tags=["test"], description="Test base directory")
def read_root():
    return {"Hello": "World FASTAPI RULES!!!!"}


@app.get("/test", tags=["test"], description="Test base directory")
def read_test():
    return {'Test': 'Funcionando la puñetera aplicacion'}


@app.get("/items/{item_id}", tags=["test"], description="Test base directory")
async def read_item(item_id: int):
    return {"item_id": item_id}
