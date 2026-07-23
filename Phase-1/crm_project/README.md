# Phase 1: Database Schema for Smart Personal CRM

## What I Built
The foundational database for a Personal CRM that helps students track professional contacts. 
I created three interlinked tables:

- **User** – Stores student account details (extends Django's built-in User).
- **Contact** – Stores professional contacts, linked to a User.
- **Interaction** – Stores meeting notes and conversation logs, linked to a Contact.

## Tech Stack
- Django 5.x (Python)
- SQLite (development database)

## How to Run This Project

1. Clone the repository.
2. Navigate to `Phase-1/crm_project/`.
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Run migrations:
   ```bash
   python manage.py migrate