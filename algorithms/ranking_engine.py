"""
Bias-Free Ranking Engine
Final candidate ranking used by companies.
"""

def calculate_final_ranking_score(
    role_match_score: float,
    trust_score: float,
    growth_velocity: float
) -> float:
    """
    role_match_score : 0 - 100
    trust_score      : 0 - 1
    growth_velocity  : usually small decimal

    returns final ranking score
    """

    # Normalize trust to 100
    trust_normalized = trust_score * 100

    final_score = (
        role_match_score * 0.6 +
        trust_normalized * 0.25 +
        (growth_velocity * 100) * 0.15
    )

    return round(final_score, 2)
