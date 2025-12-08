# 🚀 Quick Start Guide - Django + Vercel + Aiven

## The 5-Minute Local Setup

This guide gets you running locally in 5 minutes with SQLite (no Aiven needed).

### Step 1: Activate Virtual Environment (30 seconds)

```powershell
cd D:\EvenNest\Main
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 2: Install Dependencies (2 minutes)

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Setup Environment (30 seconds)

```powershell
Copy-Item .env.local .env
```

The `.env` file should contain:
```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=local-dev-key-change-in-production
```

### Step 4: Run Migrations (1 minute)

```powershell
python manage.py migrate
```

### Step 5: Create Admin User & Run Server (1 minute)

```powershell
python manage.py createsuperuser
python manage.py runserver
```

✅ **Done!** Visit `http://localhost:8000/admin/` and log in.

---

## Database Strategy

| Environment | Database | Setup | Commands |
|---|---|---|---|
| **Local Dev** | SQLite (db.sqlite3) | Automatic | `migrate`, `runserver` |
| **Testing** | Aiven MySQL | Set `$env:DATABASE_URL` | `migrate`, test, unset |
| **Production** | Aiven MySQL | Vercel dashboard env vars | Auto on deploy |

---

## Testing Against Aiven (Optional, 5 minutes)

If you want to test migrations against your actual production database:

```powershell
# 1. Set DATABASE_URL (get from Aiven dashboard, remove ssl-mode=REQUIRED)
$env:DATABASE_URL = 'mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb'

# 2. Test connection
python manage.py dbshell

# 3. Run migrations
python manage.py migrate

# 4. Verify in Aiven dashboard → SQL Editor: SHOW TABLES;

# 5. Clear environment variable
Remove-Item env:DATABASE_URL
```

⚠️ **Note:** This modifies your production database. Be careful!

---

## Deploying to Vercel (10 minutes)

### Prerequisites

```powershell
# Install Vercel CLI (one time only)
npm install -g vercel
```

### Deploy

```powershell
# 1. Commit your code
cd D:\EvenNest\Main
git add -A
git commit -m "Django + Vercel + Aiven setup"
git push origin main

# 2. Deploy to Vercel
vercel --prod
```

### Configure Environment Variables in Vercel Dashboard

1. Go to https://vercel.com/dashboard
2. Select your project
3. Settings → Environment Variables
4. Add these variables:

| Name | Value |
|------|-------|
| `DJANGO_DEBUG` | `False` |
| `DJANGO_SECRET_KEY` | Generate: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DATABASE_URL` | `mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb` |
| `PYTHONUNBUFFERED` | `1` |

5. Click "Save"
6. Redeploy: `vercel --prod`

---

## Troubleshooting in 30 Seconds

### Local: "unable to open database file"
```powershell
# Make sure DATABASE_URL is NOT set in .env
type .env  # Should NOT have DATABASE_URL line
```

### Local: Connection timeout
```powershell
# Check DATABASE_URL format (if testing with Aiven)
echo $env:DATABASE_URL
# Should look like: mysql://avnadmin:password@host:port/db
# Should NOT have: ssl-mode=REQUIRED
```

### Vercel: Static files 404
```powershell
# Ensure STATIC_ROOT is correct in settings.py
# Should be: STATIC_ROOT = BASE_DIR / 'staticfiles'

# Check vercel.json has buildCommand:
# "buildCommand": "pip install -r requirements.txt && python manage.py collectstatic --noinput --clear"

# Redeploy:
vercel --prod
```

### Vercel: Can't log in to admin
```powershell
# Create superuser on Aiven database
$env:DATABASE_URL = 'mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb'
python manage.py createsuperuser
Remove-Item env:DATABASE_URL
```

---

## What Files Were Changed/Created?

| File | Status | What Changed |
|------|--------|--------------|
| `myproject/settings.py` | ✏️ Modified | Complete rewrite: SQLite/Aiven logic, PyMySQL, SSL handling, Whitenoise |
| `requirements.txt` | ✏️ Modified | Removed mysqlclient, channels_redis; added PyMySQL, whitenoise, python-dotenv |
| `myproject/__init__.py` | ✏️ Modified | Enhanced PyMySQL setup with comments |
| `vercel.json` | ✏️ Modified | Updated to use Django framework, proper build/install commands, static file routing |
| `.env.local` | 📄 New | Local dev environment template (SQLite) |
| `.env.production` | 📄 New | Production environment template (reference only) |
| `VERCEL_DEPLOYMENT_COMPLETE_GUIDE.md` | 📄 New | Comprehensive 500+ line guide |
| `SETUP_REFERENCE_COMPLETE.md` | 📄 New | Complete file contents + checklist |

---

## Key Assumptions

1. **Python 3.11+** installed locally
2. **Aiven MySQL instance** accessible and you have connection details
3. **Git repo** (GitHub/GitLab/Bitbucket) with your code
4. **You're NOT using Redis** for caching in production (in-memory channels layer is fine)
5. **You're NOT using S3** for static files (Whitenoise handles it)

---

## Architecture Summary

```
┌─────────────────────┐
│  Local Development  │
│  SQLite (db.sqlite3)│
│  DEBUG=True         │
│  No internet needed │
└──────────┬──────────┘
           │
           │ (set $env:DATABASE_URL to test)
           ↓
┌─────────────────────┐
│   Aiven MySQL       │
│   (Production DB)   │
│   Testing only      │
└──────────┬──────────┘
           │
           │ (git push origin main)
           ↓
┌─────────────────────┐
│  Vercel Deployment  │
│  DATABASE_URL set   │
│  PyMySQL driver     │
│  DEBUG=False        │
│  Static via WN      │
└─────────────────────┘
```

---

## Next Steps

1. ✅ Follow "The 5-Minute Local Setup" above
2. ✅ Run `python manage.py runserver` and verify `http://localhost:8000/` works
3. ✅ (Optional) Test migrations against Aiven
4. ✅ Deploy to Vercel following "Deploying to Vercel" section
5. ✅ Verify production at your Vercel URL
6. 📚 Reference `VERCEL_DEPLOYMENT_COMPLETE_GUIDE.md` for detailed docs

---

## Questions?

Check these files:
- `VERCEL_DEPLOYMENT_COMPLETE_GUIDE.md` — Full deployment guide with troubleshooting
- `SETUP_REFERENCE_COMPLETE.md` — All file contents + detailed reference
- `myproject/settings.py` — Inline comments explaining each section
