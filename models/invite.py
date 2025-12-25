"""
Invite Model
Represents a company inviting a candidate
"""

class Invite:
    def __init__(
        self,
        company_id: str,
        candidate_id: str,
        role_name: str,
        status: str = "pending",
        created_at=None
    ):
        self.company_id = company_id
        self.candidate_id = candidate_id
        self.role_name = role_name
        self.status = status  # pending / accepted / rejected
        self.created_at = created_at

    def to_dict(self):
        return {
            "company_id": self.company_id,
            "candidate_id": self.candidate_id,
            "role_name": self.role_name,
            "status": self.status,
            "created_at": self.created_at
        }
