from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
  id: Optional[int] = None
  title: str = Field(min_length=5, max_length=50, example="Mi Pelicula", description="Nombre de la pelicula")
  description: str = Field(min_length=5, max_length=250, example="Descripcion de la pelicula", description="Descripcion de la pelicula")
  rating: float = Field(ge=0.0, le=10.0, example=8.1, description="Rating de la pelicula")
  year: int = Field(ge=1900, le=2024, example=2015, description="Año de la pelicula entre 1900 y 2024")
  categories: list = Field(min_length=4, max_length=50, example=["Action", "Adventure", "Sci-Fi"])