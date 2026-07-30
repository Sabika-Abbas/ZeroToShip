# Phase 3: REST APIs & AI Orchestration

## Overview
This phase adds full CRUD operations for contacts and an AI-powered follow-up draft generator. The AI endpoint fetches past interaction notes for a specific contact and uses LangChain with Groq's LLaMA 3.3 model to generate a personalized, professional follow-up message.

## Features

### 1. Contact CRUD (Already built in Phase 2, now fully operational)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/contacts/` | Create a new contact | ✅ Yes |
| GET | `/api/contacts/` | List all contacts (user's own) | ✅ Yes |
| GET | `/api/contacts/<id>/` | Retrieve a specific contact | ✅ Yes |
| PUT | `/api/contacts/<id>/` | Update a contact | ✅ Yes |
| DELETE | `/api/contacts/<id>/` | Delete a contact | ✅ Yes |

### 2. AI Draft Generator 🧠

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/generate-draft/` | Generate a personalized follow-up draft for a contact |

**Request Body:**
```json
{
  "contact_id": 2
}