# NGO Home Page Management Website

A simple and clean Django-based NGO website with a dynamic homepage and admin content management. The project is built with Python, Django, SQLite, HTML, CSS, Bootstrap 5, and basic JavaScript through Bootstrap components.

This is a beginner-friendly student project. It keeps the code simple while still showing realistic website features such as banners, mission and vision content, impact statistics, programs, news, testimonials, partner logos, image uploads, and admin-only management pages.

## Features

- Responsive NGO homepage
- NGO logo and navigation menu
- Hero banner carousel with smooth Bootstrap slider
- Tagline and short NGO description
- Donate, Volunteer, and Contact call-to-action buttons
- Mission and Vision section
- Impact statistics cards
- Initiatives / Programs section
- Success stories / testimonials section
- Latest news, events, and blog posts section
- Partners / supporters logo section
- Footer with contact information, quick links, social links, and copyright
- Django admin login using built-in authentication
- Custom staff dashboard for managing homepage content
- Image uploads using Django media configuration
- SQLite database for local development

## Admin Can Manage

The admin or staff user can add, edit, update, and delete:

- Banner slider images and text
- Vision and Mission content
- Impact statistics
- Initiatives / Programs
- News / Events / Blog posts
- Testimonials
- Partner logos

Content can be managed from both:

```text
http://127.0.0.1:8000/admin/
```

and the custom dashboard:

```text
http://127.0.0.1:8000/dashboard/
```

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap 5
- Basic JavaScript through Bootstrap
- Pillow for image uploads
- WhiteNoise and Gunicorn for deployment support

## Project Structure

```text
Project2/
+-- authproject/
|   +-- settings.py
|   +-- urls.py
|   +-- wsgi.py
|   +-- asgi.py
+-- home/
|   +-- admin.py
|   +-- forms.py
|   +-- models.py
|   +-- urls.py
|   +-- views.py
|   +-- migrations/
+-- users/
|   +-- forms.py
|   +-- urls.py
|   +-- views.py
|   +-- models.py
+-- templates/
|   +-- base.html
|   +-- navbar.html
|   +-- footer.html
|   +-- main_home.html
|   +-- dashboard.html
|   +-- manage_base.html
|   +-- manage_banner.html
|   +-- manage_statistics.html
|   +-- manage_initiatives.html
|   +-- manage_news.html
|   +-- manage_testimonials.html
|   +-- manage_partners.html
|   +-- manage_vision_mission.html
|   +-- login.html
|   +-- register.html
+-- static/
|   +-- css/
|   |   +-- style.css
|   +-- js/
|       +-- main.js
+-- media/
+-- db.sqlite3
+-- manage.py
+-- requirements.txt
```

## Database Models

The `home` app contains the main homepage content models:

- `Banner`
- `VisionMission`
- `Statistic`
- `Initiative`
- `NewsEvent`
- `Testimonial`
- `Partner`

These models are registered in Django admin and are also used by the custom dashboard pages.

## Local Setup

Open PowerShell or terminal and go to the project folder:

```powershell
cd Project2
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run migrations:

```powershell
python manage.py migrate
```

Create an admin user:

```powershell
python manage.py createsuperuser
```

Start the development server:

```powershell
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

## Admin Login

Open:

```text
http://127.0.0.1:8000/admin/
```

Login using the username and password created with:

```powershell
python manage.py createsuperuser
```

Django admin login uses username and password. Email is stored in the account but is not used for login by default.

## Custom Dashboard

After logging in as a staff/admin user, open:

```text
http://127.0.0.1:8000/dashboard/
```

Dashboard pages include:

```text
/dashboard/banners/
/dashboard/vision-mission/
/dashboard/statistics/
/dashboard/initiatives/
/dashboard/news/
/dashboard/testimonials/
/dashboard/partners/
```

## Media Uploads

Uploaded images are stored inside:

```text
media/
```

Django media settings are configured in `authproject/settings.py`:

```python
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
```

During local development, media files are served from `authproject/urls.py` when `DEBUG=True`.

## Useful Commands

```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py collectstatic --noinput
```

If the normal `python` command uses the wrong Python installation, use the virtual environment directly:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

## Notes

- This project uses Django's built-in authentication system.
- Only staff/admin users should access the custom dashboard.
- SQLite is used for local development and student project demos.
- Pillow is required because the project uses Django `ImageField` for uploads.
- Bootstrap 5 is used for responsive layout and the homepage carousel.
- The design is intentionally simple, clean, and beginner-friendly.
