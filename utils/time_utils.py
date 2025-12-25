"""
Time and date helpers
"""

from datetime import datetime

def current_utc_time():
    return datetime.utcnow()


def days_between(start_date: datetime, end_date: datetime) -> int:
    return abs((end_date - start_date).days)


def hours_between(start_date: datetime, end_date: datetime) -> int:
    return int(abs((end_date - start_date).total_seconds()) // 3600)
