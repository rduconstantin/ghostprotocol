# GhostProtocol

GhostProtocol is a privacy-as-a-service OSINT engine that discovers a user's digital footprint, scores their privacy exposure, and orchestrates GDPR/CCPA erasure requests.

## Architecture

- **Backend:** FastAPI + Celery for async scanning tasks.
- **Frontend:** React (Vite) with a security dashboard aesthetic.
- **Database:** PostgreSQL with AES-256-at-rest expectations for sensitive metadata.
- **Auth:** OAuth 2.0 (Google + Microsoft) for inbox metadata discovery.

## Folder Structure

```
/backend   FastAPI API + Celery tasks
/frontend  React dashboard UI
/scripts   Automation scripts (OSINT + opt-out)
```

## Local Development

1. Configure environment variables (see **Required API Keys**).
2. Start the stack:

```bash
docker compose up --build
```

- API: http://localhost:8000
- Frontend: http://localhost:5173

## API Endpoints (MVP)

- `GET /health` - health check
- `POST /scan` - run a basic footprint scan

Example payload:

```json
{
  "username": "ghostuser",
  "email": "ghost@example.com"
}
```

## Required API Keys

Set these in your environment or `.env` file before running Docker:

- `OAUTH_GOOGLE_CLIENT_ID`
- `OAUTH_GOOGLE_CLIENT_SECRET`
- `OAUTH_MICROSOFT_CLIENT_ID`
- `OAUTH_MICROSOFT_CLIENT_SECRET`
- `STRIPE_SECRET_KEY`
- `BRANDFETCH_API_KEY`

## Product Guardrails

- **Zero-knowledge:** never store raw user data; process it in-memory for scans.
- **Consent:** require an explicit Power of Attorney checkbox prior to sending legal emails.

## Roadmap Highlights

- OSINT scraper to scan 500+ sources with adaptive rate limiting.
- Inbox metadata analyzer for account registration discovery.
- Privacy Health Score algorithm (0-100) with weighted exposure metrics.
- Data broker workflows (Whitepages, Spokeo, etc.).
- GDPR Article 17 + CCPA request automation with DPO directory mapping.
- Stripe-powered freemium / one-click deletion flows.
