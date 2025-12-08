# EvenNest Vercel Deployment Guide

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **PostgreSQL Database**: Choose one of:
   - [Vercel Postgres](https://vercel.com/storage/postgres)
   - [Supabase](https://supabase.com)
   - [Railway](https://railway.app)
   - [Neon](https://neon.tech)
3. **GitHub Repository**: Project must be pushed to GitHub

## Step 1: Prepare Your Repository

Ensure all files are committed and pushed:

```bash
git add -A
git commit -m "Prepare for Vercel deployment"
git push origin main
```

## Step 2: Set Up PostgreSQL Database

### Option A: Vercel Postgres (Recommended)

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to **Storage** tab
4. Click **Create Database** → **Postgres**
5. Follow the setup wizard
6. Copy the `POSTGRES_URL_NON_POOLING` (for Django migrations)

### Option B: Supabase

1. Go to [Supabase](https://supabase.com)
2. Create a new project
3. Get your connection string from **Settings** → **Database**
4. Format: `postgresql://postgres:password@host:5432/postgres`

### Option C: Railway

1. Go to [Railway](https://railway.app)
2. Create new project
3. Add PostgreSQL plugin
4. Copy the database URL

## Step 3: Configure Environment Variables in Vercel

1. Go to **Vercel Dashboard** → **Settings** → **Environment Variables**
2. Add the following variables:

```
DJANGO_SECRET_KEY = (generate a new Django secret key)
DJANGO_DEBUG = False
DATABASE_URL = (your PostgreSQL URL from Step 2)
ALLOWED_HOSTS = your-domain.vercel.app,your-custom-domain.com
CSRF_TRUSTED_ORIGINS = https://your-domain.vercel.app,https://your-custom-domain.com
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
VERCEL_ENV = production
```

### Generate Django Secret Key

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Step 4: Deploy to Vercel

### Option A: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
cd d:\EvenNest\Main
vercel --prod
```

### Option B: Via GitHub Integration (Recommended)

1. Go to [Vercel Import](https://vercel.com/import/git)
2. Select your GitHub repository
3. Framework: **Django**
4. Add environment variables from Step 3
5. Click **Deploy**

## Step 5: Configure Build Settings (if needed)

In Vercel Dashboard → **Settings** → **Build & Development**:

- **Build Command**: `python manage.py collectstatic --noinput && python manage.py migrate --noinput`
- **Output Directory**: (leave empty, using vercel.json)
- **Install Command**: `pip install -r requirements.txt`

The `vercel.json` file handles this automatically.

## Step 6: Verify Deployment

1. Check your Vercel deployment URL
2. Test the application:
   - Admin panel: `https://your-domain.vercel.app/admin/`
   - Services page: `https://your-domain.vercel.app/services/`
   - Store page: `https://your-domain.vercel.app/store/`

3. Create admin user:
   ```bash
   vercel env pull  # Pull environment variables locally
   python manage.py createsuperuser
   ```

## Step 7: Configure Custom Domain (Optional)

1. Go to Vercel Dashboard → **Domains**
2. Add your custom domain
3. Follow DNS configuration instructions
4. Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in Vercel environment variables

## Important Notes

### Static Files & Media Files

- **Static Files**: Served via Vercel's CDN (managed by `whitenoise`)
- **Media Files**: Consider using AWS S3 or Vercel KV for persistent storage
  - Local media uploads won't persist after each deployment
  - See `.env.example` for S3 configuration

### WebSocket Support

- **Current Status**: Vercel doesn't support long-running WebSocket connections for Django Channels
- **Chat Feature**: Currently disabled (migration 0015), but needs alternative implementation:
  - Use Vercel Functions with WebSocket-compatible services
  - Or use a separate server (Railway, Render, Heroku) for WebSocket features
  - Or implement polling-based chat instead of WebSockets

### Database Migrations

Vercel automatically runs the build script which includes:
```bash
python manage.py migrate --noinput
```

Ensure your database URL is set in environment variables.

### Monitoring & Logs

1. View logs in Vercel Dashboard → **Deployments** → **Logs**
2. Enable error tracking:
   - Set up Sentry integration
   - Configure email notifications for errors

## Troubleshooting

### Import Error: `dj_database_url`

Solution: This is in `requirements.txt`

### Database Connection Failed

- Verify `DATABASE_URL` environment variable
- Check database server is accessible
- For Vercel Postgres: Wait 1-2 minutes after creation
- Test locally first: `python manage.py migrate`

### Static Files Not Loading

- Run: `python manage.py collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` in settings
- Vercel's `whitenoise` middleware should serve them

### Admin Panel Not Accessible

- Create superuser via Vercel CLI:
  ```bash
  vercel env pull
  python manage.py createsuperuser
  ```

## Next Steps

1. **Update Copilot Instructions**: Update `.github/copilot-instructions.md` with Vercel-specific notes
2. **Set Up Monitoring**: Configure error logging and performance monitoring
3. **Configure Email**: Set up SMTP for user notifications
4. **Consider Media Storage**: Implement S3 or similar for production media files
5. **WebSocket Strategy**: Plan alternative for chat feature if needed

## Rollback

If deployment fails:

```bash
# Redeploy previous version
vercel rollback

# Or specify a deployment
vercel promote <deployment-id>
```

## Additional Resources

- [Vercel Django Documentation](https://vercel.com/guides/deploying-django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [Vercel Postgres Documentation](https://vercel.com/docs/storage/vercel-postgres)

---

**Questions?** Check the Vercel docs or create an issue in the GitHub repository.
