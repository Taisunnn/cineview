from fastapi import HTTPException, status

def get_unauthorized_exception(detail="Could not validate user."):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )

def get_not_found_exception(detail="Not Found"):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )