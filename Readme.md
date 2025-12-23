
---

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
