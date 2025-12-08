# Quick Vercel Deployment Guide - Direct from GitHub

## Fastest Way to Deploy (2 minutes!)

### Step 1: Go to Vercel Dashboard
1. Open https://vercel.com
2. Sign in with GitHub account (or create one)

### Step 2: Import Your Repository
1. Click **"New Project"** button
2. Click **"Import Git Repository"**
3. Search for and select **"Prohar04/EvenNest"**
4. Click **"Import"**

### Step 3: Configure Project
**Framework**: Leave as "Other"  
**Root Directory**: `Main` (very important!)  
**Environment Variables**: Add these from Vercel dashboard

```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
USE_SQLITE=False
USE_S3=True
DB_ENGINE=postgresql
DB_NAME=evenest_prod
DB_USER=evenest_admin
DB_PASSWORD=your-password
DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_PORT=5432
AWS_STORAGE_BUCKET_NAME=evenest-media-prod
AWS_S3_REGION_NAME=us-east-1
AWS_S3_ACCESS_KEY_ID=your-access-key
AWS_S3_SECRET_ACCESS_KEY=your-secret-key
AWS_S3_CUSTOM_DOMAIN=evenest-media-prod.s3.amazonaws.com
VERCEL_URL=your-deployment-url
```

### Step 4: Click "Deploy"
Vercel will automatically:
- ✅ Build your Django app
- ✅ Set up serverless functions
- ✅ Deploy to production
- ✅ Provide you a URL like: `https://evenest-xxx.vercel.app`

---

## But First: Set Up AWS Resources

Before deploying, you MUST create:

### 1. PostgreSQL Database (5 mins)
Go to: https://console.aws.amazon.com/rds
- Create RDS PostgreSQL instance
- Get endpoint, username, password

### 2. S3 Bucket (5 mins)
Go to: https://console.aws.amazon.com/s3
- Create S3 bucket for media
- Create IAM user with S3 access
- Get access key and secret key

**See AWS_SETUP_GUIDE.md for detailed steps**

---

## Alternative: Deploy with SQLite (No AWS Needed)

If you want to test on Vercel WITHOUT AWS:

### Step 1: Keep vercel.json as is

### Step 2: Use SQLite Environment Variables
```
DJANGO_DEBUG=False
USE_SQLITE=True
USE_S3=False
```

### Step 3: Deploy

⚠️ **WARNING**: SQLite doesn't work well on Vercel because:
- Database resets on every deploy
- No persistent storage
- Not recommended for production

---

## Detailed Steps: Deploy NOW

### 1. Push Latest Code (Already Done ✅)
```bash
git push origin main
```

### 2. Go to Vercel
https://vercel.com/dashboard

### 3. Create New Project
- Click "New Project"
- Select "Import Git Repository"
- Search "EvenNest"
- Click "Import"

### 4. Configure Before Deploy

```
Project Name: evenest
Framework Preset: Other
Root Directory: Main
Build Command: python manage.py collectstatic --noinput
Output Directory: staticfiles
```

### 5. Add Environment Variables

In Vercel Dashboard → Project Settings → Environment Variables

**Without AWS (Test Only):**
```
DJANGO_SECRET_KEY=django-insecure-test-key-change-in-production
DJANGO_DEBUG=False
USE_SQLITE=True
USE_S3=False
```

**With AWS (Production):**
```
DJANGO_SECRET_KEY=<generate-new>
DJANGO_DEBUG=False
USE_SQLITE=False
USE_S3=True
DB_ENGINE=postgresql
DB_HOST=<your-rds-endpoint>
DB_NAME=evenest_prod
DB_USER=evenest_admin
DB_PASSWORD=<your-password>
DB_PORT=5432
AWS_STORAGE_BUCKET_NAME=evenest-media-prod
AWS_S3_REGION_NAME=us-east-1
AWS_S3_ACCESS_KEY_ID=<your-key>
AWS_S3_SECRET_ACCESS_KEY=<your-secret>
AWS_S3_CUSTOM_DOMAIN=evenest-media-prod.s3.amazonaws.com
VERCEL_URL=evenest-xxxx.vercel.app
```

### 6. Click "Deploy"
Wait for build to complete (~3-5 minutes)

### 7. Get Your URL
Once deployed, you'll get: `https://evenest-xxxx.vercel.app`

---

## Post-Deployment Steps

### Run Migrations
```bash
# Option 1: SSH into Vercel (if available)
vercel env pull
python manage.py migrate

# Option 2: Create migration endpoint
# See section below
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Upload Seed Data
```bash
python manage.py loaddata core/fixtures/initial_products.json
```

---

## Create Migration Endpoint (Important!)

Since Vercel is serverless, you need a way to run migrations. Create `api/migrate.py`:

```python
import os
import django
from django.core.management import call_command
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def handler(request):
    """
    Endpoint to run Django migrations
    Call with: POST /api/migrate?token=YOUR_SECRET_TOKEN
    """
    token = request.GET.get('token')
    migration_secret = os.getenv('MIGRATION_SECRET')
    
    if token != migration_secret:
        return {
            'statusCode': 403,
            'body': 'Unauthorized'
        }
    
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
```

Then in Vercel add environment variable:
```
MIGRATION_SECRET=your-random-secret-token
```

Call migration endpoint:
```bash
curl "https://evenest-xxxx.vercel.app/api/migrate?token=your-random-secret-token"
```

---

## Troubleshooting

### Build Fails: "psycopg2 not found"
- Ensure `psycopg2-binary` is in requirements.txt
- Run: `pip freeze > requirements.txt`
- Push and redeploy

### Build Fails: "Module not found"
- Check all imports in views.py
- Ensure all packages in requirements.txt are available
- Add missing packages: `pip install package_name`

### 502 Bad Gateway
- Check Vercel function logs
- Verify all environment variables are set
- Check ALLOWED_HOSTS includes your Vercel domain

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- If using S3, verify bucket policy allows public read

### Database Connection Failed
- Test RDS endpoint is reachable
- Check security group allows TCP 5432
- Verify credentials are exactly correct

---

## Success! ✅

Once deployed, you can:
- Visit: https://evenest-xxxx.vercel.app/
- Admin panel: https://evenest-xxxx.vercel.app/admin/
- Login: username `admin2` / password `admin123`

---

## Cost Summary

| Service | Free Tier | Cost |
|---------|-----------|------|
| **Vercel Pro** | - | $20/month |
| **RDS PostgreSQL** | 12 months | $10-15/month after |
| **S3 Storage** | 1GB/year | $2-5/month |
| **Total** | First year | ~$32-40/month |

**During free tier: Only Vercel Pro needed at $20/month**

---

## Need Help?

1. **Deployment stuck?** Check Vercel logs: Dashboard → Deployments → Latest
2. **Database issues?** Follow AWS_SETUP_GUIDE.md exactly
3. **S3 upload failing?** Verify IAM permissions
4. **Static files missing?** Run collectstatic locally

**All documentation available in GitHub repo!**

