"""
Role Match Algorithm
Matches candidate skills against company role blueprint.
"""

def calculate_role_match_score(
    candidate_skills: dict,
    role_blueprint: dict
) -> float:
    """
    candidate_skills = {
        "Python": 82,
        "SQL": 74
    }

    role_blueprint = {
        "Python": 0.4,
        "SQL": 0.3,
        "Problem Solving": 0.3
    }

    returns role match score between 0 - 100
    """

    total_score = 0.0

    for skill, weight in role_blueprint.items():
        candidate_score = candidate_skills.get(skill, 0)
        total_score += candidate_score * weight

    return round(total_score, 2)
