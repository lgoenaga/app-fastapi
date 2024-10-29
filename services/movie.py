from fastapi import HTTPException, Query
from models.movie import ModelMovie
from typing import List

class MovieService:

    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def get_movies_service(self) -> List[ModelMovie]:
        movies_data = self.movie_repository.query(ModelMovie).all()
        if not movies_data:
            self.movie_repository.close()
            raise HTTPException(status_code=404, detail="Películas no encontradas")
        self.movie_repository.close()
        return movies_data

    def get_movie_by_id_service(self, id: int) -> ModelMovie:
        movie_data  = self.movie_repository.query(ModelMovie).filter(ModelMovie.id == id).first()
        if not movie_data:
            self.movie_repository.close()
            raise HTTPException(
              status_code=404, detail="Película no encontrada"
          )
        return movie_data

    def get_movies_by_categories_by_year_service(self, categories: str, year: int) -> List[ModelMovie]:
        movie_data  = self.movie_repository.query(ModelMovie).filter(ModelMovie.year == year, ModelMovie.category == categories).all()
        if not movie_data:
            self.movie_repository.close()
            raise HTTPException(
              status_code=404, detail="Películas con esa categoria y/o año no encontradas"
          )
        self.movie_repository.close()
        return movie_data

    def get_movies_by_categories_service(self, categories: str) -> List[ModelMovie]:
        movies_data = self.movie_repository.query(ModelMovie).filter(ModelMovie.categories == categories).all()       
        if not movies_data:
            self.movie_repository.close()
            raise HTTPException(
                status_code=404, detail="Películas con esa categoria no encontradas"
            )
        self.movie_repository.close()
        return movies_data

    def get_movies_by_year_service(self, year: int) -> List[ModelMovie]:
        movies_data  = self.movie_repository.query(ModelMovie).filter(ModelMovie.year == year).all()
        if not movies_data:
            self.movie_repository.close()
            raise HTTPException(
                status_code=404, detail="Películas con ese año no en contradas"
            )
        self.movie_repository.close()
        return movies_data

    def create_movie_service(self, movie_data: dict) -> ModelMovie:
        self.movie_repository.add(movie_data)
        self.movie_repository.commit()
        self.movie_repository.refresh(movie_data)
        self.movie_repository.close()
        return movie_data

    def update_movie_service(self, id: int, movie_data: dict) -> ModelMovie:
        movie_to_update = self.get_movie_by_id_service(id)   
        if not movie_to_update:
            self.movie_repository.close()
            raise HTTPException(
                status_code=404, detail="Película no encontrada"
            )           
        for key, value in movie_data.items():
            setattr(movie_to_update, key, value)     
        self.movie_repository.commit()
        self.movie_repository.refresh(movie_to_update)
        self.movie_repository.close()
        return movie_to_update

    def delete_movie_service(self, id: int) -> None:
        movie_data = self.get_movie_by_id_service(id)
        if not movie_data:
            self.movie_repository.close()
            raise HTTPException(
              status_code=404, detail="Película no encontrada"
            )
        self.movie_repository.delete(movie_data)
        self.movie_repository.commit()
        self.movie_repository.close()
        return None
