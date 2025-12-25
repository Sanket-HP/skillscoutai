from algorithms.skill_scoring import calculate_skill_score
from services.candidate_service import update_candidate_skill

def evaluate_and_update_skill(
    uid: str,
    skill_name: str,
    accuracy: float,
    difficulty: float,
    consistency: float
):
    """
    Called after a candidate submits a task.
    """

    score = calculate_skill_score(
        accuracy=accuracy,
        difficulty=difficulty,
        consistency=consistency
    )

    candidate = update_candidate_skill(
        uid=uid,
        skill_name=skill_name,
        score=score
    )

    return {
        "skill": skill_name,
        "score": score,
        "verified": True,
        "growth_velocity": candidate["growth_velocity"]
    }
