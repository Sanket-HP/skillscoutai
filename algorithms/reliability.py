"""
Reliability Index Algorithm
Measures dependability and task completion behavior.
"""

def calculate_reliability_index(
    tasks_completed: int,
    tasks_assigned: int
) -> float:
    """
    tasks_completed : number of completed tasks
    tasks_assigned  : total tasks assigned

    returns reliability score between 0 - 1
    """

    if tasks_assigned == 0:
        return 1.0

    reliability = tasks_completed / tasks_assigned
    reliability = min(max(reliability, 0), 1)

    return round(reliability, 2)
