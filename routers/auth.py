from fastapi import APIRouter
from fastapi.responses import JSONResponse

from jwt_manager import create_token
from model import UserModel

auth_router = APIRouter()

@auth_router.post("/login", tags=["Auth"], response_model=dict, status_code=200)
def login(user: UserModel):
    token = create_token(user.model_dump())
    if token:
        return JSONResponse(status_code=200, content={"token": token})
    else:
        return JSONResponse(
            status_code=401, content={"message": "Credenciales incorrectas"}
        )
