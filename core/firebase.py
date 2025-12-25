"""
Firebase initialization (Auth + Firestore)
"""

import firebase_admin
from firebase_admin import credentials, firestore, auth

from core.config import settings


# --------------------------------------------------
# Initialize Firebase App (only once)
# --------------------------------------------------

if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)


# --------------------------------------------------
# Firestore Database Client
# --------------------------------------------------

db = firestore.client()


# --------------------------------------------------
# Firebase Authentication Client
# --------------------------------------------------

firebase_auth = auth
