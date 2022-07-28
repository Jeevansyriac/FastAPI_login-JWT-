# thsi file is for sining , encoding,decoding and returning jwt token


import time  #its for setting time for token(expiry time of token)

import jwt

from decouple import config

# taking file from .env
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# this function is to return the generated token
def token_response(token: str):
    return {
        "access_token": token
    }


# function used for signing the JWT string
def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}