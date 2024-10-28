from pydantic import BaseModel, Field
from typing import Optional


class UserModel(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50,
        description="Nombre de usuario",
    )
    email: str = Field(
        description="Correo electrónico del usuario",
    )
    password: str = Field(
        min_length=4,
        max_length=50,
        description="Contraseña del usuario",
    )
    is_active: bool = Field(
        default=True,
        description="Indica si el usuario está activo",
    )
    
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(
        min_length=5,
        max_length=50,
        description="Nombre de la película",
    )
    description: str = Field(
        min_length=5,
        max_length=250,
        description="Descripción de la película",
    )
    rating: float = Field(
        ge=0.0,
        le=10.0,
        description="Rating de la película entre 0.0 y 10.0",
    )
    year: int = Field(
        ge=1900,
        le=2024,
        description="Año de la película entre 1900 y 2024",
    )
    categories: list = Field(
        min_length=1, 
        max_length=5, 
        description="Categorías de la película",
    )
  
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi película",
                    "description": "Descripción de mi película",
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
                "title": "Mi película",
                "description": "Descripción de mi película",
                "rating": 8.0,
                "year": 2020,
                "categories": ["Action", "Thriller"],
            }
        }
    """
