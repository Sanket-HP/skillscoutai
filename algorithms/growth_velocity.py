"""
Growth Velocity Algorithm
Measures how fast a candidate improves over time.
"""

def calculate_growth_velocity(
    initial_score: float,
    latest_score: float,
    days_passed: int
) -> float:
    """
    initial_score : skill score at first attempt
    latest_score  : most recent skill score
    days_passed   : days between attempts

    returns growth velocity score
    """

    if days_passed <= 0:
        return 0.0

    velocity = (latest_score - initial_score) / days_passed

    return round(velocity, 4)
