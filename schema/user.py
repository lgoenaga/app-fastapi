from pydantic import BaseModel, Field

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

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "lgoenaga",
                    "email": "lgoenaga@gmail.com",
                    "password": "fadfajfhajkha",
                    "is_active": "True",
                }
            ]
        }
    }
