
---

# AI-Powered Surveillance & Threat Monitoring Backend

A backend application built using **Django REST Framework** to ingest security events, automatically generate alerts for high-risk activities, and manage them using **role-based access control**.

This project is designed to be **assignment-ready**, **interview-friendly**, and **deployable on free hosting platforms** without shell access.

## Features

- JWT-based authentication
- Role-based access control (ADMIN, ANALYST)
- Secure admin bootstrap using environment variables
- Public signup restricted to analyst users
- Event ingestion with severity classification
- Automatic alert creation for HIGH / CRITICAL events
- Alert status management
- PostgreSQL support for production
- SQLite fallback for local development
- Dockerized deployment

## Project Structure

```
threat_platform/
├── core/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ ├── apps.py
│ └── permissions.py
│
├── threat_platform/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── README.md
```
___

## Authentication & Roles

### Roles

- **ADMIN**
  - Create security events
  - View and update alerts
  - Access Django admin panel

- **ANALYST**
  - View alerts only

### Important Notes

- Admin users are **not created via public signup**
- Admin is securely created at application startup using environment variables
- Public signup always creates **ANALYST** users

---

## Environment Variables

### Sample `.env`

```env
# Django Settings
SECRET_KEY=your-secret-key
DEBUG=False
ADMIN_USERNAME=admin
ADMIN_PASSWORD=Admin@123
ADMIN_EMAIL=admin@example.com
DATABASE_URL=postgresql://username:password@host:5432/dbname
```

## Running Locally (Without Docker)

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Application will be available at:
http://127.0.0.1:8000

```

## Running with Docker
```
docker build -t threat-monitoring-backend .
docker run -p 8000:8000 --env-file .env threat-monitoring-backend
```
