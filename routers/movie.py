from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from middleware.jwt_bearer import JWTBearer
from model import Movie, UserModel
from models.movie import ModelMovie
from jwt_manager import create_token
from config.database import session

movie_router =  APIRouter()


@movie_router.get(
    "/movies",
    tags=["Movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    with session() as db:
        movies = db.query(ModelMovie).all()
        if not movies:
            raise HTTPException(status_code=404, detail="Películas no encontradas")
        return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@movie_router.get("/movies/{id}", tags=["Movies"], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1)) -> Movie:
    with session() as db:
        movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
        if not movie:
            raise HTTPException(status_code=404, detail="Película no encontrada")
        return JSONResponse(status_code=200, content=jsonable_encoder(movie))


@movie_router.get("/movies/", tags=["Movies"], response_model=List[Movie], status_code=200)
def get_movies_by_categories(
    categories: str = Query(min_length=5, max_length=10), year: int = None
) -> List[Movie]:
    with session() as db:
        query = db.query(ModelMovie).filter(ModelMovie.categories.contains(categories))
        if query.count() == 0:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        if year:
            query = query.filter(ModelMovie.year == year)
            if query.count() == 0:
                raise HTTPException(status_code=404, detail="Año no encontrado")
        movies = query.all()
        return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@movie_router.post("/movies", tags=["Movies"], response_model=Movie, status_code=201)
def create_movie(movie: Movie) -> Movie:
    with session() as db:
        movie = ModelMovie(**movie.model_dump())
        db.add(movie)
        db.commit()
        db.refresh(movie)
        return JSONResponse(status_code=201, content=jsonable_encoder(movie))


@movie_router.put("/movies/{id}", tags=["Movies"], response_model=Movie, status_code=200)
def update_movie(movie: Movie, id: int = Path(ge=1)) -> Movie:
    with session() as db:
        movie_to_update = db.query(ModelMovie).filter(ModelMovie.id == id).first()
        if not movie_to_update:
            raise HTTPException(status_code=404, detail="Película no encontrada")

        update_data = movie.model_dump(exclude={"id"})
        for key, value in update_data.items():
            setattr(movie_to_update, key, value)

        db.commit()
        db.refresh(movie_to_update)
        return JSONResponse(status_code=200, content=jsonable_encoder(movie_to_update))


@movie_router.delete("/movies/{id}", tags=["Movies"], response_model=dict, status_code=200)
def delete_movie(id: int):
    with session() as db:
        movie = db.query(ModelMovie).filter(ModelMovie.id == id).first()
        if not movie:
            raise HTTPException(status_code=404, detail="Película no encontrada")

        db.delete(movie)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Película eliminada"})


@movie_router.post("/login", tags=["Auth"], response_model=dict, status_code=200)
def login(user: UserModel):
    token = create_token(user.model_dump())
    if token:
        return JSONResponse(status_code=200, content={"token": token})
    else:
        return JSONResponse(
            status_code=401, content={"message": "Credenciales incorrectas"}
        )
