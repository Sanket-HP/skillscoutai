"""
Candidate Model
Represents a skill-first job seeker
"""

class Candidate:
    def __init__(
        self,
        uid: str,
        email: str,
        skills: dict = None,
        growth_velocity: float = 0.0,
        reliability: float = 1.0,
        tasks_completed: int = 0,
        tasks_assigned: int = 0,
        available: bool = True,
        created_at=None
    ):
        self.uid = uid
        self.email = email
        self.skills = skills or {}  # { skill_name: Skill }
        self.growth_velocity = growth_velocity
        self.reliability = reliability
        self.tasks_completed = tasks_completed
        self.tasks_assigned = tasks_assigned
        self.available = available
        self.created_at = created_at

    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            "skills": {
                name: skill.to_dict() for name, skill in self.skills.items()
            },
            "growth_velocity": self.growth_velocity,
            "reliability": self.reliability,
            "tasks_completed": self.tasks_completed,
            "tasks_assigned": self.tasks_assigned,
            "available": self.available,
            "created_at": self.created_at
        }
