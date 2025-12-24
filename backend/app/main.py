from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

from .privacy_score import calculate_privacy_score
from .osint import discover_usernames
from .legal import build_deletion_requests

app = FastAPI(title="GhostProtocol API", version="0.1.0")


class ScanRequest(BaseModel):
    username: str
    email: EmailStr


class ScanResponse(BaseModel):
    username: str
    email: EmailStr
    discovered_accounts: list[str]
    privacy_score: int
    deletion_requests: list[dict]


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}


@app.post("/scan", response_model=ScanResponse)
async def run_scan(payload: ScanRequest) -> ScanResponse:
    accounts = discover_usernames(payload.username)
    privacy_score = calculate_privacy_score(accounts)
    deletion_requests = build_deletion_requests(payload.email, accounts)
    return ScanResponse(
        username=payload.username,
        email=payload.email,
        discovered_accounts=accounts,
        privacy_score=privacy_score,
        deletion_requests=deletion_requests,
    )
