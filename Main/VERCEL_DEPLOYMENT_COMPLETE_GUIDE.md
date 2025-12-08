# Django + Vercel + Aiven Deployment Guide

## Overview

This guide provides step-by-step instructions for deploying your Django 5.2 project with:
- **Local Development**: SQLite (no internet/Aiven required)
- **Production (Vercel)**: Aiven MySQL with PyMySQL driver

---

## Table of Contents

1. [Key Architecture Decisions](#key-architecture-decisions)
2. [Local Development Setup](#local-development-setup)
3. [Testing Migrations Against Aiven](#testing-migrations-against-aiven)
4. [Deploying to Vercel](#deploying-to-vercel)
5. [Verification Checklist](#verification-checklist)
6. [Troubleshooting](#troubleshooting)

---

## Key Architecture Decisions

### Why This Approach?

| Component | Local Dev | Production (Vercel) | Reason |
|-----------|-----------|-------------------|--------|
| **Database** | SQLite | Aiven MySQL | SQLite works offline; Aiven required for production |
| **MySQL Driver** | N/A | PyMySQL | No C extension compilation needed; works on Vercel |
| **Database URL** | Not set | Set via `DATABASE_URL` | Cleaner separation of concerns |
| **Debug Mode** | `True` by default | `False` via env | Safer defaults |
| **SSL for MySQL** | N/A | Handled via `OPTIONS` | Aiven requires SSL; PyMySQL configured in settings |
| **Static Files** | Django dev server | Whitenoise + Vercel | Vercel is read-only; Whitenoise serves static files |

### Why NOT Other Solutions?

- **mysqlclient**: Requires C extensions (gcc, mysql-dev). Vercel doesn't provide these; compilation fails.
- **SQLite on Vercel**: Vercel's filesystem is ephemeral and read-only. SQLite file can't persist between deployments.
- **Docker**: Vercel supports Python, so no need for Docker overhead.

---

## Local Development Setup

### Prerequisites

- Python 3.11+ installed
- Git installed
- (Optional) A local MySQL/Aiven instance to test migrations against

### Step 1: Clone and Navigate

```powershell
cd D:\EvenNest\Main
```

### Step 2: Create Virtual Environment

```powershell
# Create venv
python -m venv venv

# Activate venv
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activation again
```

### Step 3: Install Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Create `.env` File for Local Development

Copy `.env.local` to `.env`:

```powershell
Copy-Item .env.local .env
```

Edit `.env` if needed (but defaults should work for local SQLite):

```ini
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=your-local-dev-secret-key-change-this-in-production
```

### Step 5: Run Migrations (SQLite)

```powershell
python manage.py migrate
```

**Expected Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, core
Running migrations:
  Applying core.0001_initial... OK
  ...
```

If you see "unable to open database file", check:
- You're in the correct directory (`D:\EvenNest\Main`)
- `.env` is present and `DATABASE_URL` is NOT set
- File permissions on the directory are correct

### Step 6: Create Superuser (Admin Account)

```powershell
python manage.py createsuperuser
```

Follow the prompts:
```
Username: admin
Email: admin@example.com
Password: (choose a strong password)
Password (again): (confirm)
```

### Step 7: Run Development Server

```powershell
python manage.py runserver
```

**Expected Output:**
```
Starting development server at http://127.0.0.1:8000/
...
```

Visit:
- `http://localhost:8000/` — Main app
- `http://localhost:8000/admin/` — Django admin (use superuser credentials)

Press `Ctrl+C` to stop the server.

---

## Testing Migrations Against Aiven

**Caution**: This runs migrations against your production database. Be careful!

### Step 1: Set DATABASE_URL Environment Variable

Get your Aiven connection string from the Aiven dashboard.

**Format your DATABASE_URL** (note: remove `ssl-mode=REQUIRED`):

```
mysql://avnadmin:YOUR_PASSWORD@mysql-3d02263f-proharsaha04-033f.c.aivencloud.com:13270/defaultdb
```

Set it in your terminal session:

```powershell
# Temporarily set DATABASE_URL in this PowerShell session only
$env:DATABASE_URL = 'mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb'

# Verify it's set
echo $env:DATABASE_URL
```

### Step 2: Test the Connection

```powershell
python manage.py dbshell
```

If successful, you'll see a MySQL prompt. Type `exit` to quit.

If you get connection errors:
- Check the Aiven URI (copy from Aiven dashboard)
- Verify Aiven network access rules allow your IP
- Check that password is correct

### Step 3: Run Migrations

```powershell
python manage.py migrate
```

This will apply all migrations to the Aiven database.

### Step 4: Verify in Aiven Dashboard

Log into Aiven dashboard → MySQL service → SQL Editor:
```sql
SHOW TABLES;
```

You should see Django tables: `auth_user`, `core_service`, etc.

### Step 5: Unset DATABASE_URL

Once done testing, unset the environment variable to return to SQLite:

```powershell
# PowerShell: Remove the environment variable from this session
Remove-Item env:DATABASE_URL

# Or just close and reopen PowerShell
```

---

## Deploying to Vercel

### Prerequisites

- [Vercel CLI](https://vercel.com/docs/cli) installed: `npm install -g vercel`
- A Vercel account (free tier works)
- Git repo pushed to GitHub/GitLab/Bitbucket
- Aiven MySQL instance set up

### Step 1: Prepare Your Git Repository

Ensure `.env`, `.env.local`, and `db.sqlite3` are in `.gitignore`:

```
# .gitignore
.env
.env.local
.env.*.local
db.sqlite3
venv/
__pycache__/
*.pyc
staticfiles/
media/
.DS_Store
```

Commit your changes:

```powershell
git add -A
git commit -m "Setup: Django 5.2 with Vercel + Aiven MySQL deployment"
git push origin main
```

### Step 2: Configure Vercel Project

If this is your first time deploying:

```powershell
vercel
```

Follow the prompts:
- **Create a new project?** Yes
- **Project name?** (default is fine, e.g., "EvenNest")
- **Which directory?** Current directory (.)
- **Override settings?** No (unless you know what you're doing)

Vercel will create a `.vercel/` folder (add to `.gitignore` if not already there).

### Step 3: Set Environment Variables in Vercel Dashboard

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to **Settings → Environment Variables**
4. Add the following variables:

| Variable | Value | Notes |
|----------|-------|-------|
| `DJANGO_DEBUG` | `False` | Always False in production |
| `DJANGO_SECRET_KEY` | (strong random key) | Use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` to generate |
| `DATABASE_URL` | `mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb` | Your Aiven connection string (no `ssl-mode=REQUIRED`) |
| `PYTHONUNBUFFERED` | `1` | Ensures Python output is sent straight to logs |

**To generate a strong DJANGO_SECRET_KEY locally:**

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Example output: `4f_9d2@y!q%5x^1h-2*g&p3@k!l5m6n7o8p9q0r1s2t`

Copy this and paste into Vercel dashboard.

### Step 4: Deploy to Vercel

```powershell
# Preview deployment (optional, tests build without affecting prod)
vercel --prod

# Or go straight to production
vercel --prod
```

**During deployment, Vercel will:**

1. Install dependencies from `requirements.txt`
2. Run `python manage.py collectstatic --noinput --clear`
3. Deploy your Django app to `https://evennest.vercel.app` (or your custom domain)

**Monitor the build:**

```powershell
# View logs in real-time
vercel logs --tail
```

### Step 5: Verify Deployment

Once deployment is complete:

1. Visit your deployment URL in a browser: `https://evennest.vercel.app/`
2. You should see your Django app home page
3. Test `/admin/` login with your superuser credentials
4. Check logs for any errors: `vercel logs`

### Step 6: Create Superuser on Production (Optional)

If you want to create a new superuser on the production database:

```powershell
# Set DATABASE_URL to your Aiven instance
$env:DATABASE_URL = 'mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb'

# Run createsuperuser
python manage.py createsuperuser

# Clear the env var
Remove-Item env:DATABASE_URL
```

---

## Verification Checklist

### Local Development

- [ ] `.env` file exists with `DJANGO_DEBUG=True`
- [ ] `python manage.py migrate` succeeds with SQLite
- [ ] `python manage.py createsuperuser` creates admin user
- [ ] `python manage.py runserver` starts without errors
- [ ] Django admin page loads at `http://localhost:8000/admin/`
- [ ] Main app pages load without 500 errors
- [ ] Static files (CSS, images) load correctly

### Testing Against Aiven Locally

- [ ] `DATABASE_URL` environment variable set correctly
- [ ] `python manage.py dbshell` connects successfully
- [ ] `python manage.py migrate` applies migrations to Aiven database
- [ ] Tables appear in Aiven dashboard SQL editor
- [ ] No connection timeout or SSL errors

### Production (Vercel)

- [ ] `vercel --prod` deployment succeeds
- [ ] Build logs show: "Successfully deployed to..."
- [ ] Deployment URL is reachable in browser
- [ ] Django admin login works with superuser credentials
- [ ] Main app pages load without errors
- [ ] Static files (CSS, JS, images) load correctly
- [ ] Logs show no 500 errors: `vercel logs`
- [ ] Database queries work (e.g., view list of items in admin)

---

## Troubleshooting

### Issue: "unable to open database file" locally

**Cause**: `DATABASE_URL` is set in `.env`, forcing MySQL instead of SQLite.

**Solution**:
```powershell
# Edit .env and remove or comment out DATABASE_URL
# Ensure it looks like:
# DJANGO_DEBUG=True
# DJANGO_SECRET_KEY=...
# (DATABASE_URL is NOT set)
```

### Issue: Connection timeout to Aiven

**Cause**: 
- Aiven firewall blocking your IP
- Incorrect host/port/password
- Network connectivity issue

**Solution**:
1. Check Aiven dashboard → MySQL service → Connection info
2. Verify your IP is whitelisted in Aiven firewall
3. Test with MySQL Workbench or `mysql` CLI:
   ```powershell
   mysql -u avnadmin -p -h mysql-XXXXX.c.aivencloud.com -P 13270 defaultdb
   ```
4. Check password for special characters (may need URL encoding)

### Issue: "ssl-mode=REQUIRED" causing PyMySQL errors

**Cause**: PyMySQL doesn't recognize `ssl-mode` as a keyword argument.

**Solution**: This is already handled in settings.py. Remove `ssl-mode=REQUIRED` from your `DATABASE_URL` environment variable. Django will handle SSL correctly via the `OPTIONS` dict.

### Issue: Vercel build fails with "ModuleNotFoundError: No module named 'pymysql'"

**Cause**: `requirements.txt` missing `PyMySQL` or it didn't install during build.

**Solution**:
```powershell
# Verify PyMySQL in requirements.txt
type requirements.txt | findstr PyMySQL

# If missing, add it:
echo "PyMySQL==1.1.2" >> requirements.txt

# Commit and redeploy
git add requirements.txt
git commit -m "Fix: Ensure PyMySQL in requirements"
git push origin main
vercel --prod
```

### Issue: Static files not loading on Vercel (`/static/...` returns 404)

**Cause**: `collectstatic` didn't run or failed during build.

**Solution**:
1. Check build logs: `vercel logs --tail`
2. Ensure `vercel.json` has correct `buildCommand`:
   ```json
   "buildCommand": "pip install -r requirements.txt && python manage.py collectstatic --noinput --clear"
   ```
3. Ensure `STATIC_ROOT = BASE_DIR / 'staticfiles'` in `settings.py`
4. Redeploy: `vercel --prod`

### Issue: "CSRF token missing or incorrect" on POST requests

**Cause**: Development expects insecure cookies; production requires secure cookies.

**Solution**: This is automatically handled by settings.py based on `DEBUG` value. If still seeing issues:
1. Clear browser cookies
2. Ensure `CSRF_COOKIE_SECURE = True` is set when `DEBUG=False`
3. Check browser console for CSRF token errors

### Issue: Superuser can't log into admin on production

**Cause**: Superuser was created locally (SQLite) but doesn't exist in Aiven database.

**Solution**:
```powershell
# Set DATABASE_URL to point to Aiven
$env:DATABASE_URL = 'mysql://avnadmin:YOUR_PASSWORD@mysql-XXXXX.c.aivencloud.com:13270/defaultdb'

# Create superuser on Aiven
python manage.py createsuperuser

# Clear the env var
Remove-Item env:DATABASE_URL
```

Then use the new credentials to log in on Vercel.

---

## Summary

You now have a **production-ready Django setup** with:

✅ Local SQLite development (no Aiven required)  
✅ Aiven MySQL for production  
✅ PyMySQL driver (no C extensions)  
✅ Proper SSL handling for Aiven  
✅ Vercel deployment ready  
✅ Static files served correctly  
✅ Secure settings for production  

**Next steps:**
1. Follow "Local Development Setup" to get running locally
2. Run migrations and verify everything works
3. Follow "Deploying to Vercel" when ready
4. Use "Verification Checklist" to confirm each environment works
5. Reference "Troubleshooting" if issues arise

Good luck! 🚀
