"""
Security utilities for FastAPI using Firebase Auth
"""

from fastapi import HTTPException, status, Header
from core.firebase import firebase_auth


def verify_firebase_token(
    authorization: str = Header(None)
):
    """
    Extracts and verifies Firebase JWT token from request header.
    Expected header format:
    Authorization: Bearer <Firebase_ID_Token>
    """

    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing"
        )

    try:
        # Remove "Bearer " prefix
        token = authorization.replace("Bearer ", "").strip()

        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
