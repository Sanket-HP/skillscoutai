from core.firebase import db
from algorithms.role_match import calculate_role_match_score
from algorithms.ranking_engine import calculate_final_ranking_score

CANDIDATE_COLLECTION = "candidates"
COMPANY_COLLECTION = "companies"

def create_company(uid: str, company_name: str):
    company = {
        "uid": uid,
        "company_name": company_name,
        "role_blueprints": [],
        "created_at": db.SERVER_TIMESTAMP
    }
    db.collection(COMPANY_COLLECTION).document(uid).set(company)
    return company


def search_candidates(role_blueprint: dict):
    """
    role_blueprint example:
    {
        "Python": 0.4,
        "SQL": 0.3,
        "Problem Solving": 0.3
    }
    """

    candidates = db.collection(CANDIDATE_COLLECTION).stream()
    results = []

    for doc in candidates:
        c = doc.to_dict()
        if not c.get("available", False):
            continue

        candidate_skills = {
            skill: data["score"]
            for skill, data in c.get("skills", {}).items()
        }

        role_match = calculate_role_match_score(
            candidate_skills,
            role_blueprint
        )

        trust_score = c.get("reliability", 1.0)
        growth_velocity = c.get("growth_velocity", 0.0)

        final_rank = calculate_final_ranking_score(
            role_match_score=role_match,
            trust_score=trust_score,
            growth_velocity=growth_velocity
        )

        results.append({
            "candidate_id": c["uid"],
            "role_match": role_match,
            "trust": trust_score,
            "growth_velocity": growth_velocity,
            "final_rank": final_rank,
            "skills": candidate_skills
        })

    results.sort(key=lambda x: x["final_rank"], reverse=True)
    return results
