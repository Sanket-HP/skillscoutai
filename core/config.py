"""
Central configuration for SkillScout AI
"""

import os

class Settings:
    PROJECT_NAME: str = "SkillScout AI"
    API_VERSION: str = "v1"

    # Firebase
    FIREBASE_CREDENTIALS: str = os.getenv(
        "FIREBASE_CREDENTIALS",
        "firebase_key.json"
    )

    # Security
    TOKEN_HEADER: str = "Authorization"

settings = Settings()
