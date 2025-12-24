from __future__ import annotations

DPO_DIRECTORY = {
    "github.com": "privacy@github.com",
    "twitter.com": "privacy@twitter.com",
    "instagram.com": "privacy@instagram.com",
    "linkedin.com": "privacy@linkedin.com",
}


def build_deletion_requests(user_email: str, accounts: list[str]) -> list[dict]:
    requests = []
    for account in accounts:
        domain = account.split("//")[-1].split("/")[0]
        dpo_email = DPO_DIRECTORY.get(domain, "privacy@company.example")
        requests.append(
            {
                "account": account,
                "dpo_email": dpo_email,
                "subject": "Request for Erasure (GDPR Article 17 / CCPA)",
                "body": (
                    f"Hello,\n\n"
                    f"I am requesting erasure of my data associated with {user_email}. "
                    "Please confirm deletion per GDPR Article 17 and CCPA.\n\n"
                    "Regards,\nGhostProtocol User"
                ),
            }
        )
    return requests
