"""
Skill Authenticity Scoring Algorithm
Measures how real and strong a skill is based on performance.
"""

def calculate_skill_score(
    accuracy: float,
    difficulty: float,
    consistency: float
) -> float:
    """
    accuracy   : 0.0 - 1.0
    difficulty : 0.5 - 2.0 (easy → hard)
    consistency: 0.0 - 1.0

    returns skill score between 0 - 100
    """

    if not (0 <= accuracy <= 1):
        raise ValueError("Accuracy must be between 0 and 1")

    raw_score = accuracy * difficulty * consistency
    normalized_score = min(raw_score * 100, 100)

    return round(normalized_score, 2)
