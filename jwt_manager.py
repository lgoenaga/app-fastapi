from jwt import decode, encode
  

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="secret_key", algorithm="HS256")
    return token
  
def validar_token(token: str) -> dict:
    try:
        decoded_token = decode(token, key="secret_key", algorithms=["HS256"])
        return decoded_token
    except:
        return {"message": "Token invalid"}