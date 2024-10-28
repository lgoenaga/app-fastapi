from fastapi import Depends, FastAPI, HTTPException, Path, Query, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from model import Movie, UserModel
from jwt_manager import create_token, validar_token

from fastapi.security import HTTPBearer

from config.database import session, engine, db_td
from models.movie import ModelMovie


app = FastAPI()
app.title = "My API con FastAPI"
app.version = "1.0"
app.description = "Esta es una API de prueba con FastAPI"

db_td.metadata.create_all(engine)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validar_token(auth.credentials)
        if data["username"] != "admin" or data["password"] != "admin":
            raise HTTPException(status_code=403, detail="Credenciales Invalidas")


@app.get("/", tags=["Inicio"])
def content_home():
    return {"Hello": "World"}


@app.get(
    "/movies",
    tags=["Movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    db = session()
    movies = db.query(ModelMovie).all()
    db.close()
    if not movies:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@app.get("/movies/{id}", tags=["Movies"], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1)) -> Movie:
    db = session()
    movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    db.close()
    if not movie:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    return JSONResponse(status_code=200, content=jsonable_encoder(movie))


@app.get("/movies/", tags=["Movies"], response_model=List[Movie], status_code=200)
def get_movies_by_categories(
    categories: str = Query(min_length=5, max_length=10), year: int = None
) -> List[Movie]:
    db = session()
    query = db.query(ModelMovie).filter(ModelMovie.categories.contains(categories))
    if query.count() == 0:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    if year:
        query = query.filter(ModelMovie.year == year)
        if query.count() == 0:
            raise HTTPException(status_code=404, detail="Año no encontrado")
    movies = query.all()
    db.close()

    return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@app.post("/movies", tags=["Movies"], response_model=Movie, status_code=201)
def create_movie(movie: Movie) -> Movie:
    db = session()
    movie = ModelMovie(**movie.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    db.close()
    return JSONResponse(status_code=201, content=jsonable_encoder(movie))


@app.put("/movies/{id}", tags=["Movies"], response_model=Movie, status_code=200)
def update_movie(movie: Movie, id: int = Path(ge=1)) -> Movie:
    db = session()
    movie_to_update = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not movie_to_update:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    
    update_data = movie.model_dump(exclude={"id"})
    for key, value in update_data.items():
        setattr(movie_to_update, key, value)
    
    db.commit()
    db.refresh(movie_to_update)
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(movie_to_update))

@app.delete("/movies/{id}", tags=["Movies"], response_model=dict, status_code=200)
def delete_movie(id: int):
    db = session()
    movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")
    
    db.delete(movie)
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Pelicula eliminada"})


@app.post("/login", tags=["Auth"], response_model=dict, status_code=200)
def login(user: UserModel):
    token = create_token(user.model_dump())
    if token:
        return JSONResponse(status_code=200, content={"token": token})
    else:
        return JSONResponse(
            status_code=401, content={"message": "Credenciales incorrectas"}
        )
