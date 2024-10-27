from fastapi import FastAPI, Body

from models import Movie


app = FastAPI()
app.title = "My API con FastAPI"
app.version = "1.0"
app.description = "Esta es una API de prueba con FastAPI"

movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "rating": 9.3,
        "year": 1994,
        "categories": ["Drama"]
    },
    {
        "id": 2,
        "title": "Forrest Gump",
        "description": "The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other history unfold through the perspective of an Alabama man with an IQ of 75.",
        "rating": 8.8,
        "year": 1994,
        "categories": ["Drama", "Romance"]
    },
    {
        "id": 3,
        "title": "The Godfather",
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "rating": 9.2,
        "year": 1972,
        "categories": ["Crime", "Drama"]
    },
    {
        "id": 4,
        "title": "Die Hard",
        "description": "An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza in Los Angeles.",
        "rating": 8.2,
        "year": 1988,
        "categories": ["Action", "Thriller"]
    },
    {
        "id": 5,
        "title": "Mad Max: Fury Road",
        "description": "In a post-apocalyptic wasteland, Max teams up with a mysterious woman, Furiosa, to try and survive.",
        "rating": 8.1,
        "year": 2015,
        "categories": ["Action", "Adventure", "Sci-Fi"]
    }
]

@app.get("/", tags=["Inicio"])
def content_home():
    return {"Hello": "World"}

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return "Pelicula no encontrada"

@app.get("/movies/", tags=["Movies"])
def get_movies_by_categories(categories: str, year: int=None):
    movies_categories=[]
    for item in movies:
        if categories in item["categories"]:
            if year!=None:
                if item["year"]==year:
                    movies_categories.append(item)
            else:
                movies_categories.append(item)    
    return movies_categories

@app.post ("/movies", tags=["Movies"])
def create_movie(movie: Movie):
    movies.append(movie)
    return movie

@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["description"] = movie.description
            item["rating"] = movie.rating
            item["year"] = movie.year
            item["categories"] = movie.categories
            return item
    return "Pelicula no encontrada"

@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return "Pelicula eliminada"
    return "Pelicula no encontrada"