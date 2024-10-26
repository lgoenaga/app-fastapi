from fastapi import FastAPI

app = FastAPI()
app.title = "My API con FastAPI"
app.version = "1.0"
app.description = "Esta es una API de prueba con FastAPI"

@app.get("/", tags=["Inicio"])
def content_home():
    return {"Hello": "World"}