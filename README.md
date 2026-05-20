# Login Registration Django App

A simple Django web application for user registration, login, logout, and a protected dashboard page. The project uses Django's built-in authentication system, SQLite, Bootstrap, and the built-in Django admin panel for user management.

## Features

- Public home page with Login and Register buttons
- User registration with username, email, and password
- Secure password storage using Django authentication
- Username and password login
- Error and success messages using Django messages
- Protected dashboard page for logged-in users only
- Secure logout with redirect to login
- Django admin panel for managing users
- SQLite database for local development
- Bootstrap responsive UI
- Function-based views and simple URL routing

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- Gunicorn and WhiteNoise for deployment

## Project Structure

```text
project/
+-- authproject/
|   +-- settings.py
|   +-- urls.py
|   +-- wsgi.py
+-- users/
|   +-- forms.py
|   +-- urls.py
|   +-- views.py
+-- templates/
|   +-- base.html
|   +-- dashboard.html
|   +-- login.html
|   +-- main_home.html
|   +-- navbar.html
|   +-- register.html
+-- static/
|   +-- css/
|   +-- js/
+-- manage.py
+-- requirements.txt
+-- Procfile
+-- runtime.txt
```

## Local Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Website Flow

```text
Home Page -> Register -> Login -> Dashboard -> Logout -> Login
```

## Admin Panel

Open:

```text
http://127.0.0.1:8000/admin/
```

Login with the superuser account created using:

```bash
python manage.py createsuperuser
```

The admin can view, add, edit, and delete users from Django's built-in Users section.

## Database

The app uses SQLite by default.

Local database file:

```text
db.sqlite3
```

Registered users are stored in Django's built-in:

```text
auth_user
```

For GitHub, the database file should not be committed. Keep `db.sqlite3` ignored in `.gitignore`.

## GitHub Push

Initialize and push:

```bash
git init
git add .
git commit -m "Initial Django login registration app"
git branch -M main
git remote add origin https://github.com/shravanishinde602/login-registration.git
git push -u origin main
```

## Render Deployment

Create a new Render Web Service and connect the GitHub repository.

Use these settings:

```text
Language: Python
Branch: main
Root Directory: leave empty
```

Build Command:

```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

Start Command:

```bash
gunicorn authproject.wsgi:application
```

Environment Variables:

```text
SECRET_KEY=your-long-random-secret-key
DEBUG=False
ALLOWED_HOSTS=.onrender.com
```

You can also set `ALLOWED_HOSTS` to your exact Render domain:

```text
your-app-name.onrender.com
```

Do not include `https://` or a trailing slash in `ALLOWED_HOSTS`.

## Common Render Issue: Bad Request 400

If the deployed site shows `Bad Request (400)`, check `ALLOWED_HOSTS`.

Correct examples:

```text
.onrender.com
your-app-name.onrender.com
```

Wrong examples:

```text
https://your-app-name.onrender.com
https://your-app-name.onrender.com/
```

After changing environment variables, redeploy from Render:

```text
Manual Deploy -> Deploy latest commit
```

## Useful Commands

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py collectstatic --noinput
```

## Notes

- This project uses Django's built-in `User` model. No custom user model is required.
- SQLite is fine for local development and demos.
- For a production app with permanent data on Render, PostgreSQL is recommended.
