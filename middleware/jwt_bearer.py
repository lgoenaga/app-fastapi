from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from jwt_manager import validar_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        try:
            data = validar_token(auth.credentials)
            if data["username"] != "admin" or data["password"] != "admin":
                raise HTTPException(status_code=403, detail="Credenciales Invalidas")
        except Exception as e:
            raise HTTPException(status_code=403, detail=str(e))
