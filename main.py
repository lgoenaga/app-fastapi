from fastapi import FastAPI

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
