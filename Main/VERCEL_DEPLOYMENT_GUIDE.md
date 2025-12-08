# Vercel Deployment Guide for EvenNest

## Prerequisites

1. **Vercel Account** - Sign up at https://vercel.com
2. **GitHub Repository** - Push your code to GitHub
3. **PostgreSQL Database** - Use Vercel's PostgreSQL or an external provider (e.g., AWS RDS, Heroku Postgres)
4. **Environment Variables** - Set up in Vercel dashboard

## Step 1: Prepare Your Repository

```bash
cd d:\EvenNest\Main

# Ensure all changes are committed
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

## Step 2: Database Configuration

Since Vercel doesn't support SQLite for persistent data, you must use PostgreSQL:

1. Create a PostgreSQL database:
   - Use AWS RDS (https://aws.amazon.com/rds/)
   - Use Heroku Postgres (https://elements.heroku.com/addons/heroku-postgresql)
   - Use Vercel Postgres (if available in your region)

2. Get your database credentials:
   - Database URL: `postgresql://user:password@host:port/dbname`

## Step 3: Set Up Vercel Project

1. Go to https://vercel.com/dashboard
2. Click "New Project"
3. Import your GitHub repository
4. Choose "Django" as framework (if available) or "Other"
5. Configure build & output settings

## Step 4: Environment Variables

In Vercel dashboard, go to **Settings → Environment Variables** and add:

```
DJANGO_SECRET_KEY=<your-long-random-secret-key>
DJANGO_DEBUG=False
USE_SQLITE=False

# Database Configuration
DB_ENGINE=postgresql
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
DB_PORT=5432

# Vercel specific
VERCEL_URL=<your-vercel-url>.vercel.app
```

To generate a secure SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Step 5: Update Settings for PostgreSQL

Create/update `.env.production`:

```bash
DJANGO_DEBUG=False
USE_SQLITE=False
DB_ENGINE=postgresql
DB_HOST=<your-postgres-host>
DB_PORT=5432
DB_NAME=<your-db-name>
DB_USER=<your-db-user>
DB_PASSWORD=<your-db-password>
DJANGO_SECRET_KEY=<your-secret-key>
```

## Step 6: Run Migrations on Production

After deployment, you need to run migrations on the production database:

```bash
# SSH into Vercel function (not directly supported)
# Instead, create a temporary endpoint to run migrations
```

Alternative approach - use Django management command as a Vercel Function:

Create `api/migrate.py`:
```python
from django.core.management import call_command
import os

def handler(request):
    if request.method == 'POST' and request.headers.get('Authorization') == f"Bearer {os.getenv('MIGRATION_SECRET')}":
        try:
            call_command('migrate')
            return {
                'statusCode': 200,
                'body': 'Migrations completed successfully'
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'Migration failed: {str(e)}'
            }
    return {
        'statusCode': 403,
        'body': 'Unauthorized'
    }
```

Then call it with:
```bash
curl -X POST https://your-app.vercel.app/api/migrate \
  -H "Authorization: Bearer your-migration-secret"
```

## Step 7: Upload Media Files

Vercel functions have ephemeral filesystems. For persistent media storage, use:

1. **AWS S3** - Recommended
2. **Google Cloud Storage**
3. **Azure Blob Storage**

Install storage backend:
```bash
pip install django-storages boto3
```

Update `settings.py`:
```python
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
    AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
```

Add S3 credentials to Vercel environment variables.

## Step 8: Static Files

Run locally to collect static files:
```bash
python manage.py collectstatic --noinput
```

Vercel will serve static files automatically. Ensure `STATIC_ROOT` is set in settings.py.

## Step 9: Deploy

```bash
# Push your changes
git add .
git commit -m "Configure for Vercel deployment"
git push origin main

# Vercel will automatically redeploy
```

Monitor deployment at https://vercel.com/dashboard

## Troubleshooting

### 502 Bad Gateway
- Check Vercel logs: Dashboard → Deployments → Function Logs
- Verify database connection string
- Check `ALLOWED_HOSTS` includes Vercel domain

### ImportError for modules
- Add missing packages to `requirements.txt`
- Run `pip freeze > requirements.txt` locally
- Push changes and redeploy

### Static files not loading
- Run `python manage.py collectstatic`
- Verify `STATIC_ROOT` and `STATIC_URL` in settings
- Check Vercel build logs

### Media files not persisting
- Implement S3 storage (see Step 7)
- Don't rely on local filesystem

## Key Differences from Development

| Feature | Development | Vercel |
|---------|------------|--------|
| Database | SQLite | PostgreSQL (required) |
| Media Files | Local filesystem | S3 or external storage |
| Debug Mode | True | False (required) |
| Logs | Console | Vercel dashboard |
| Environment Variables | .env file | Vercel dashboard |
| URL | http://localhost:8000 | https://your-app.vercel.app |

## Monitoring

1. **Vercel Analytics** - Built-in performance monitoring
2. **Django Logging** - Configure logging to Vercel
3. **Database Monitoring** - Monitor PostgreSQL usage
4. **Error Tracking** - Use Sentry.io for error reporting

## Rollback

If deployment fails:
1. Go to Vercel Dashboard
2. Select previous deployment
3. Click "Redeploy"

---

For more help, see:
- Vercel Django docs: https://vercel.com/docs/frameworks/django
- Django deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
