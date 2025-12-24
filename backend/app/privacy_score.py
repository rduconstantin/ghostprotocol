from __future__ import annotations


def calculate_privacy_score(discovered_accounts: list[str]) -> int:
    """
    Calculate a privacy score based on the number of exposed accounts.
    """
    exposure = min(len(discovered_accounts) * 10, 100)
    return max(0, 100 - exposure)
