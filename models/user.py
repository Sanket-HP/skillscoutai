"""
Base User Model
Used for both Candidate and Company
"""

class User:
    def __init__(
        self,
        uid: str,
        email: str,
        role: str,
        created_at=None
    ):
        self.uid = uid
        self.email = email
        self.role = role  # "candidate" or "company"
        self.created_at = created_at

    def to_dict(self):
        return {
            "uid": self.uid,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at
        }
