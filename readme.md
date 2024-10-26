# Ejemplo-fastapi
Ejemplo de un pequeño proyecto en python para usar con FastAPI

## Iniciar
1. Crear entorno virtual
```
python -m venv movie-api
```
2. Activar entorno virtual
```
source movie-api/bin/activate
```
3. Instalar Dependencias
```zsh
pip install -r requirements.txt
```
4. Iniciar app FastAPI
```
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```
5. Documentación Swagguer
```
local API docs 
http://localhost:5000/docs
```
