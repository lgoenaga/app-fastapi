from sqlalchemy import Column, Float, Integer, String, ARRAY


from sqlalchemy.ext.declarative import declarative_base

from config.database import db_td


class ModelMovie(db_td):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    categories = Column(String)

    """
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi película",
                    "description": "Descripción de mi película",
                    "rating": 8.0,
                    "year": 2020,
                    "categories": "Action",
                }
            ]
        }
    }
    """

    """
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi película",
                "description": "Descripción de mi película",
                "rating": 8.0,
                "year": 2020,
                "categories": "Thriller"
            }
        }
    """
