import fastapi

from .core.security.bearer import BearerToken, HTTPBearer


def FernAuth(auth: BearerToken = fastapi.Depends(HTTPBearer)) -> BearerToken:
    return auth
