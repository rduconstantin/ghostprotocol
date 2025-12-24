from .celery_app import celery_app
from .osint import discover_usernames
from .privacy_score import calculate_privacy_score


@celery_app.task
def run_osint_scan(username: str) -> dict:
    accounts = discover_usernames(username)
    return {
        "username": username,
        "accounts": accounts,
        "privacy_score": calculate_privacy_score(accounts),
    }
