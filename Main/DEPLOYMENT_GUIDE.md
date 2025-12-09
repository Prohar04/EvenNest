# EventNest Vercel Deployment Guide

Complete step-by-step guide to deploy EventNest to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at https://vercel.com
2. **GitHub Account**: Push your code to https://github.com
3. **MySQL Database**: Get a database from Aiven, AWS RDS, or similar
4. **Domain (Optional)**: Custom domain for production

## Step 1: Prepare Your Repository

### 1.1 Ensure code is ready
```bash
cd D:\EventNest\Main
git status
```

### 1.2 Create .env.production file (do NOT commit)
```bash
cp .env.example .env.production
```

Edit `.env.production`:
```env
DJANGO_SECRET_KEY=generate-a-secure-key
DJANGO_DEBUG=False
DATABASE_URL=mysql://username:password@host:port/dbname
ALLOWED_HOSTS=your-app.vercel.app,yourdomain.com
```

Generate a secure key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 1.3 Push to GitHub
```bash
git add -A
git commit -m "feat: ready for Vercel deployment"
git push origin main
```

## Step 2: Set Up MySQL Database

### Option A: Using Aiven (Recommended)
1. Go to https://aiven.io/
2. Create account
3. Create MySQL service
4. Get connection string: `mysql://username:password@hostname:port/dbname`

### Option B: Using AWS RDS
1. Create RDS MySQL instance
2. Get endpoint and credentials
3. Format: `mysql://username:password@endpoint:3306/dbname`

## Step 3: Deploy on Vercel

### 3.1 Connect GitHub
1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Select your EventNest repository
4. Click "Import"

### 3.2 Configure Project
1. **Project Name**: `eventnest` (or your choice)
2. **Framework**: Django
3. **Root Directory**: `Main/`

### 3.3 Add Environment Variables
In the environment variables section, add:

```
DJANGO_SECRET_KEY=your-generated-secret-key
DJANGO_DEBUG=False
DATABASE_URL=mysql://username:password@host:port/dbname
ALLOWED_HOSTS=your-app.vercel.app,yourdomain.com
PYTHONUNBUFFERED=1
```

### 3.4 Deploy
Click "Deploy" and wait for the deployment to complete.

## Step 4: Post-Deployment Setup

### 4.1 Initialize Database
After successful deployment, run migrations:

```bash
vercel env pull
python manage.py migrate --database=production
```

Or use Vercel CLI:
```bash
vercel env pull
python manage.py migrate
```

### 4.2 Create Superuser
```bash
python manage.py createsuperuser
```

### 4.3 Collect Static Files
Static files are automatically collected during build. Verify in deployment logs.

### 4.4 Test Admin Interface
- Visit: `https://your-app.vercel.app/admin/`
- Login with superuser credentials
- Verify everything is accessible

## Step 5: Add Custom Domain (Optional)

### 5.1 In Vercel Dashboard
1. Go to project settings
2. Click "Domains"
3. Add your custom domain
4. Follow DNS configuration steps

### 5.2 Update DNS
Point your domain's DNS records to Vercel nameservers or CNAME.

## Step 6: Load Initial Data

### 6.1 Load Fixtures
```bash
python manage.py loaddata fixtures/initial_products.json
```

### 6.2 Or Create Data Manually
Use admin interface to create:
- Service categories
- Services
- Store categories
- Store items

## Troubleshooting

### Database Connection Failed
```
Error: Can't connect to MySQL server
```
**Solution:**
- Verify DATABASE_URL is correct
- Check database credentials
- Ensure firewall allows Vercel IPs
- Test connection locally first

### Static Files Not Loading
```
404 Not Found for static files
```
**Solution:**
```bash
python manage.py collectstatic --noinput --clear
```

### Migration Errors
```
Error: Migrations don't exist
```
**Solution:**
```bash
python manage.py migrate --noinput
```

### ALLOWED_HOSTS Error
```
DisallowedHost at /
Invalid HTTP_HOST header
```
**Solution:**
Update ALLOWED_HOSTS in environment variables.

## Monitoring & Logs

### View Deployment Logs
1. Go to Vercel dashboard
2. Select project
3. Click "Deployments" tab
4. View logs for any deployment

### Check Application Logs
```bash
vercel logs
```

## Performance Optimization

### Enable Caching
Already configured in `settings.py` with:
- Whitenoise for static files
- Database query optimization
- Template caching

### Database Optimization
Consider:
- Adding indexes to frequently queried fields
- Using database connection pooling
- Regular backups

## Security Checklist

- [ ] DJANGO_DEBUG is False
- [ ] SECRET_KEY is strong and unique
- [ ] ALLOWED_HOSTS is configured
- [ ] CSRF protection enabled
- [ ] HTTPS enforced
- [ ] Database password is strong
- [ ] Admin password is secure
- [ ] Regular backups configured

## Continuous Deployment

Push to `main` branch to trigger automatic deployments:

```bash
git add -A
git commit -m "Update: new feature"
git push origin main
```

Vercel will automatically:
1. Build the application
2. Run migrations (if configured)
3. Deploy new version
4. Update DNS

## Rollback

If something goes wrong:

1. Go to Vercel dashboard
2. Click "Deployments"
3. Find previous stable deployment
4. Click three dots → "Redeploy"

## Database Backup

Regular backups are crucial:

### Using Aiven
- Automatic daily backups (retention varies)
- Manual backups available in console
- Restore from backup point

### Using AWS RDS
- Enable automated backups
- Set backup retention period (7-35 days)
- Create manual snapshots before major changes

## Maintenance

### Regular Tasks
- Monitor disk usage
- Review error logs weekly
- Update dependencies monthly
- Test functionality after each update

### Monthly
```bash
pip list --outdated
pip install --upgrade -r requirements.txt
```

## Support

For Vercel-specific issues:
- https://vercel.com/support
- https://vercel.com/docs

For Django issues:
- https://docs.djangoproject.com
- https://stackoverflow.com/questions/tagged/django

---

**Deployment Status**: ✅ Ready to Deploy

Your EventNest application is configured and ready for production deployment!
