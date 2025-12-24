DIRECTORY_SOURCES = [
    "https://github.com", 
    "https://twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
]


def discover_usernames(username: str) -> list[str]:
    """
    Placeholder OSINT discovery logic.

    Replace with a real scanning pipeline that checks 500+ sources, rate limits,
    and uses provider-specific adapters.
    """
    return [f"{source}/{username}" for source in DIRECTORY_SOURCES]
