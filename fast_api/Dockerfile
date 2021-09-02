FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install fastapi 
RUN pip install --upgrade pip
RUN pip install SQLAlchemy  cryptography typing openapi
RUN pip install starlette
RUN pip install jsonify
RUN pip install PyMySQL


COPY ./app /app

