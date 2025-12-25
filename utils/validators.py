"""
Common validation utilities for SkillScout AI
"""

import re

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def is_valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_REGEX, email))


def is_valid_skill_name(skill_name: str) -> bool:
    return isinstance(skill_name, str) and len(skill_name.strip()) >= 2


def is_valid_score(score: float) -> bool:
    return isinstance(score, (int, float)) and 0 <= score <= 100


def is_valid_role(role: str) -> bool:
    return role in ["candidate", "company"]
