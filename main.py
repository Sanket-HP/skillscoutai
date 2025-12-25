from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.security import verify_firebase_token

from services.candidate_service import get_candidate
from services.company_service import search_candidates
from services.skill_service import evaluate_and_update_skill
from services.invite_service import send_invite, get_candidate_invites


# --------------------------------------------------
# App Initialization
# --------------------------------------------------

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="SkillScout AI – Reverse hiring platform where companies discover skills"
)

# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "SkillScout AI Backend is live 🚀"
    }

# --------------------------------------------------
# Candidate APIs
# --------------------------------------------------

@app.get("/candidate/profile")
def candidate_profile(user=Depends(verify_firebase_token)):
    return get_candidate(user["uid"])


@app.post("/candidate/skill/submit")
def submit_skill(payload: dict, user=Depends(verify_firebase_token)):
    return evaluate_and_update_skill(
        uid=user["uid"],
        skill_name=payload["skill_name"],
        accuracy=payload["accuracy"],
        difficulty=payload["difficulty"],
        consistency=payload["consistency"]
    )


@app.get("/candidate/invites")
def candidate_invites(user=Depends(verify_firebase_token)):
    return get_candidate_invites(user["uid"])

# --------------------------------------------------
# Company APIs
# --------------------------------------------------

@app.post("/company/search")
def company_search(role_blueprint: dict, user=Depends(verify_firebase_token)):
    return search_candidates(role_blueprint)


@app.post("/company/invite")
def company_invite(payload: dict, user=Depends(verify_firebase_token)):
    return send_invite(
        company_id=user["uid"],
        candidate_id=payload["candidate_id"],
        role_name=payload["role_name"]
    )
