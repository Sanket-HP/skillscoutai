"""
Firebase initialization (Auth + Firestore)

Supports:
- Local development using firebase_key.json
- Production (Render) using FIREBASE_SERVICE_ACCOUNT env variable
"""

import os
import json
import firebase_admin
from firebase_admin import credentials, firestore, auth


# --------------------------------------------------
# Initialize Firebase App (only once)
# --------------------------------------------------

if not firebase_admin._apps:

    # 🔹 Production / Render (recommended)
    firebase_env = os.getenv("FIREBASE_SERVICE_ACCOUNT")

    if firebase_env:
        # Firebase credentials from environment variable (JSON string)
        cred_dict = json.loads(firebase_env)
        cred = credentials.Certificate(cred_dict)

    else:
        # 🔹 Local development fallback
        cred = credentials.Certificate("firebase_key.json")

    firebase_admin.initialize_app(cred)


# --------------------------------------------------
# Firestore Database Client
# --------------------------------------------------

db = firestore.client()


# --------------------------------------------------
# Firebase Authentication Client
# --------------------------------------------------

firebase_auth = auth
