from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from middleware.jwt_bearer import JWTBearer
from models.movie import ModelMovie
from config.database import session
from schema.movie import Movie
from services.movie import MovieService

movie_router =  APIRouter()


@movie_router.get(
    "/movies",
    tags=["Movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())]
)
def get_movies() -> List[Movie]:
    with session() as db:
        movies = MovieService(db).get_movies_service()
        return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@movie_router.get(
    "/movies/{id}",
    tags=["Movies"],
    response_model=Movie,
    status_code=200,
    dependencies=[Depends(JWTBearer())]
)
def get_movie(id: int = Path(ge=1)) -> Movie:
    with session() as db:
        movie = MovieService(db).get_movie_by_id_service(id)
        return JSONResponse(status_code=200, content=jsonable_encoder(movie))


@movie_router.get(
    "/movies/",
    tags=["Movies"],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())]
)
def get_movies_by_categorys_and_year(
    categories: str = Query(min_length=5, max_length=15), year: int = None
) -> List[Movie]:
    with session() as db:
        movies = MovieService(db).get_movies_by_categories_service(categories)
        if year and movies:
            movies = MovieService(db).get_movies_by_year_service(year)
        return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@movie_router.post(
    "/movies",
    tags=["Movies"],
    response_model=Movie,
    status_code=201,
    dependencies=[Depends(JWTBearer())]
)
def create_movie(movie: Movie) -> Movie:
    with session() as db:
        new_movie = MovieService(db).create_movie_service(
            ModelMovie(**movie.model_dump(exclude={"id"}))
        )
        return JSONResponse(status_code=201, content=jsonable_encoder(new_movie))


@movie_router.put(
    "/movies/{id}", 
    tags=["Movies"], 
    response_model=Movie, 
    status_code=200,
    dependencies=[Depends(JWTBearer())]
)
def update_movie(id: int, movie: Movie) -> Movie:
    with session() as db:
        updated_movie = MovieService(db).update_movie_service(id, movie.model_dump(exclude={"id"}))
        return JSONResponse(status_code=200, content=jsonable_encoder(updated_movie))


@movie_router.delete(
    "/movies/{id}",
    tags=["Movies"],
    response_model=dict,
    status_code=200,
    dependencies=[Depends(JWTBearer())],
)
def delete_movie(id: int) -> dict:
    with session() as db:
        MovieService(db).delete_movie_service(id)
        return JSONResponse(status_code=200, content={"message": "Película eliminada"})
