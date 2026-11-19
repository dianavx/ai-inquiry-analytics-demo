# AI Inquiry Analytics — Workflow Demo

**A small, privacy-safe portfolio example of multichannel inquiry analytics.**

Businesses receive customer inquiries from voice assistants, website chat, and email. This project demonstrates one step in a larger automation workflow: transforming **already-classified** inquiries into structured insights that can help a team prioritize follow-ups and identify commercial opportunities.

> **Portfolio demonstration:** This repository contains entirely fictional sample data and standalone illustrative code. It is informed by the architecture of business communication and automation systems I have worked on, but it is **not** a copy of a deployed platform or proof of customer outcomes.

## How the workflow fits together

```text
Voice assistant ──┐
Web chat ─────────┼──> Normalized inquiry records ──> Analytics script ──> Dashboard / CRM / reports
Email ────────────┘              ↑                        │
                          classification happens          ├─ Channel mix
                          upstream (not in this repo)     ├─ Follow-up queue
                                                         └─ Opportunity indicators
```

## What this demo shows

- A consistent data structure for inquiries across voice, web chat and email
- Aggregation by **channel**, **request category**, and **priority**
- Follow-up and opportunity flags for downstream CRM workflows
- An easily auditable JSON summary ready for a dashboard or API integration
- Input validation and automated tests

The opportunity flags are **demonstrative input fields**, not AI predictions; the script does not classify free-form conversations or estimate revenue.

## Quick start

Python 3.10+; no external packages or credentials required.

```bash
python -m src.analyze examples/inquiries.json
```

Save a summary for dashboard development:

```bash
python -m src.analyze examples/inquiries.json --output summary.json
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Example output

The synthetic sample contains 8 inquiries from 3 channels, including 5 follow-ups and 4 flagged opportunities. These counts are **example data**, not real client KPIs.

## Practical applications

A production-grade system could connect this normalization and reporting layer to a CRM, business dashboard, or notification workflow, with appropriate access controls, monitoring and error handling. This repository deliberately excludes production connectors, AI prompts, customer data, proprietary business rules, credentials, and infrastructure details.

## About

Created as a compact technical portfolio example illustrating the intersection of customer communication, automation and business-oriented analytics.

**Tags:** `ai-automation` · `workflow-automation` · `crm-integration` · `analytics` · `python`
