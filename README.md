# Django User Authentication and CMS

A professional internship-level Django project with email login, registration, email verification, password reset, role-based access control, an admin dashboard, and CMS post management.

## Features

- Custom Django user model using `AbstractUser`
- Email and password login
- Registration with full name, username, email, password, and role
- Email uniqueness validation
- Email verification link after registration
- Forgot password and reset password flow
- Session timeout after 30 minutes of inactivity
- Admin and Salesperson roles
- Admin-only dashboard and CMS CRUD
- Bootstrap 5 responsive UI
- Django messages, CSRF protection, ORM, and admin panel
- Render and PythonAnywhere deployment files

## Project Structure

```text
project/
├── authproject/
├── users/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Email Verification During Development

The project uses Django's console email backend by default. Verification and password reset links appear in the terminal where `runserver` is running.

## User Flow

Public Home Page -> Register -> Verify Email -> Login -> Dashboard -> Logout -> Login

## Roles

- Admin: can access the admin dashboard and manage CMS posts.
- Salesperson: can access the user dashboard but is blocked from admin-only pages.

To make a user an admin, open Django Admin or the shell and set:

```python
user.role = "admin"
user.is_staff = True
user.status = "active"
user.is_active = True
user.save()
```

## Render Deployment

1. Push this project to GitHub.
2. Create a new Render Web Service.
3. Use these commands:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

4. Start command:

```bash
gunicorn authproject.wsgi:application
```

5. Add environment variables:

```text
SECRET_KEY=your-secure-secret
DEBUG=False
ALLOWED_HOSTS=your-app.onrender.com
```

## PythonAnywhere Deployment

1. Upload or clone the GitHub project.
2. Create a virtual environment and install requirements.
3. Run migrations and collect static files.
4. Configure the WSGI file to use `authproject.wsgi`.
5. Add your PythonAnywhere domain to `ALLOWED_HOSTS`.

## Useful Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
