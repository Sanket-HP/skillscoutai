"""
Company Model
Represents a recruiter or organization
"""

class Company:
    def __init__(
        self,
        uid: str,
        company_name: str,
        role_blueprints: list = None,
        created_at=None
    ):
        self.uid = uid
        self.company_name = company_name
        self.role_blueprints = role_blueprints or []
        self.created_at = created_at

    def to_dict(self):
        return {
            "uid": self.uid,
            "company_name": self.company_name,
            "role_blueprints": self.role_blueprints,
            "created_at": self.created_at
        }
