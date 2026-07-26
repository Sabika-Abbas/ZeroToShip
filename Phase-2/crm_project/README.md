# Phase 2: Authentication & Authorization

## What I Built
This phase adds a secure authentication system and data integrity guards to the Personal CRM API.

## Features

### 1. User Registration (`/api/register/`)
- Users can create accounts with a username, password, and email.
- Passwords are securely hashed using Django's built-in `create_user()` method.

### 2. User Login (`/api/login/`)
- Users can log in using their username and password.
- Django creates a session for authenticated users.

### 3. Data Integrity Guard 🔒
- Users can **only** view, edit, or delete contacts that belong to them.
- When a user creates a new contact, it is automatically assigned to their `user_id`.
- This is enforced using `get_queryset()` to filter by `request.user`.

```python
def get_queryset(self):
    return Contact.objects.filter(user=self.request.user)