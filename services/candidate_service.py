from core.firebase import db
from algorithms.growth_velocity import calculate_growth_velocity
from algorithms.reliability import calculate_reliability_index
from datetime import datetime

CANDIDATE_COLLECTION = "candidates"

def create_candidate(uid: str, email: str):
    candidate = {
        "uid": uid,
        "email": email,
        "skills": {},
        "created_at": datetime.utcnow(),
        "growth_velocity": 0.0,
        "reliability": 1.0,
        "tasks_completed": 0,
        "tasks_assigned": 0,
        "available": True
    }
    db.collection(CANDIDATE_COLLECTION).document(uid).set(candidate)
    return candidate


def get_candidate(uid: str):
    doc = db.collection(CANDIDATE_COLLECTION).document(uid).get()
    return doc.to_dict() if doc.exists else None


def update_candidate_skill(uid: str, skill_name: str, score: float):
    ref = db.collection(CANDIDATE_COLLECTION).document(uid)
    candidate = ref.get().to_dict()

    previous_score = candidate["skills"].get(skill_name, {}).get("score", 0)
    first_date = candidate["skills"].get(skill_name, {}).get("first_attempt")

    if not first_date:
        first_date = datetime.utcnow()

    days_passed = max((datetime.utcnow() - first_date).days, 1)

    growth = calculate_growth_velocity(previous_score, score, days_passed)

    candidate["skills"][skill_name] = {
        "score": score,
        "verified": True,
        "first_attempt": first_date
    }

    candidate["growth_velocity"] = growth

    ref.update(candidate)
    return candidate


def update_reliability(uid: str, completed: bool):
    ref = db.collection(CANDIDATE_COLLECTION).document(uid)
    candidate = ref.get().to_dict()

    candidate["tasks_assigned"] += 1
    if completed:
        candidate["tasks_completed"] += 1

    candidate["reliability"] = calculate_reliability_index(
        candidate["tasks_completed"],
        candidate["tasks_assigned"]
    )

    ref.update(candidate)
    return candidate["reliability"]
