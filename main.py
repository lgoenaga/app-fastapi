from fastapi import FastAPI
from middleware.errores_handlers import ErrorHandler
from config.database import engine, db_td
from routers.movie import movie_router  # Adjust the import path as necessary

app = FastAPI()
app.title = "My API con FastAPI"
app.version = "1.0"
app.description = "Esta es una API de prueba con FastAPI"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)

db_td.metadata.create_all(engine)
