from jose import jwt , JWTError

SECRET_KEY = "my-secret-key-123"
ALGORITHM = "HS256"

def create_token(user):

    payload = {
        "user_id" : user["id"],
        "username" : user["username"],
        "role" : user["role"]
    }

    token = jwt.encode(payload , SECRET_KEY , algorithm = ALGORITHM)

    return token 


def verify_token(token: str):

    try:
        payload = jwt.decode(
            token , 
            SECRET_KEY , 
            algorithms = [ALGORITHM]
        )

        return payload
    
    except JWTError:
        return None 
        