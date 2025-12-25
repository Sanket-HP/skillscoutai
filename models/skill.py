"""
Skill Model
Represents a single verified or unverified skill
"""

class Skill:
    def __init__(
        self,
        name: str,
        score: float = 0.0,
        verified: bool = False,
        first_attempt=None
    ):
        self.name = name
        self.score = score
        self.verified = verified
        self.first_attempt = first_attempt

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score,
            "verified": self.verified,
            "first_attempt": self.first_attempt
        }
