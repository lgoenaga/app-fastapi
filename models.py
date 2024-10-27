from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(
        min_length=5,
        max_length=50,
        description="Nombre de la pelicula",
    )
    description: str = Field(
        min_length=5,
        max_length=250,
        description="Descripcion de la pelicula",
    )
    rating: float = Field(
        description="Rating de la pelicula entre 0.0 y 10.0",
    )
    year: int = Field(
        ge=1900,
        le=2024,
        description="Año de la pelicula entre 1900 y 2024",
    )
    categories: list = Field(
        min_length=4, max_length=50, 
        description="Categorias de la pelicula",
    )
  
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi pelicula",
                    "description": "Descripcion de mi pelicula",
                    "rating": 8.0,
                    "year": 2020,
                    "categories": ["Action", "Thriller"]
                }
            ]
        }
    }
    

    """
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "description": "Descripcion de mi pelicula",
                "rating": 8.0,
                "year": 2020,
                "categories": ["Action", "Thriller"],
            }
        }
    """
