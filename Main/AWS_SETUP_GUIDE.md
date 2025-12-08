# AWS Setup Guide for EvenNest Deployment

## Part 1: AWS RDS PostgreSQL Database Setup

### Step 1: Create RDS Instance

1. Go to [AWS RDS Console](https://console.aws.amazon.com/rds)
2. Click **Create database**
3. Choose:
   - **Engine**: PostgreSQL
   - **Version**: PostgreSQL 16.1 (or latest)
   - **Templates**: Free tier (if eligible) or Production
   - **DB Instance Identifier**: `evenest-db` or similar

### Step 2: Configure Database Settings

- **Master username**: `evenest_admin`
- **Master password**: Generate a strong password (save it!)
- **DB Instance Class**: `db.t3.micro` (free tier eligible)
- **Storage**: 20 GB (free tier)
- **Public accessibility**: Yes (for development; restrict in production)

### Step 3: Configure Network & Security

- **VPC**: Default VPC
- **Public accessibility**: Yes
- **VPC security group**: Create new or select existing
- **Database port**: 5432 (default)

**Important**: After creation, modify the security group to allow inbound traffic:
- **Type**: PostgreSQL
- **Protocol**: TCP
- **Port**: 5432
- **Source**: `0.0.0.0/0` (or your Vercel IP if known)

### Step 4: Get Connection Details

After RDS instance is created:
1. Go to **RDS Dashboard** → **Databases**
2. Click your database name
3. Copy these values under **Connectivity & security**:
   - **Endpoint**: `evenest-db.xxxxx.us-east-1.rds.amazonaws.com`
   - **Port**: `5432`
   - **Username**: `evenest_admin`
   - **Password**: (what you set earlier)

### Step 5: Create Application Database

Connect to your RDS instance using a PostgreSQL client:

```bash
# Install PostgreSQL client (if not already installed)
# On Windows: Download from https://www.postgresql.org/download/windows/
# On macOS: brew install postgresql
# On Linux: apt-get install postgresql-client

# Connect to PostgreSQL
psql -h evenest-db.xxxxx.us-east-1.rds.amazonaws.com -U evenest_admin -p 5432 -d postgres

# When prompted, enter your master password

# Create application database
CREATE DATABASE evenest_prod;

# List databases to confirm
\l

# Exit
\q
```

**Connection String** (save for Vercel):
```
postgresql://evenest_admin:YOUR_PASSWORD@evenest-db.xxxxx.us-east-1.rds.amazonaws.com:5432/evenest_prod
```

---

## Part 2: AWS S3 Bucket for Media Files

### Step 1: Create S3 Bucket

1. Go to [AWS S3 Console](https://console.aws.amazon.com/s3)
2. Click **Create bucket**
3. **Bucket name**: `evenest-media-prod` (must be globally unique)
4. **Region**: Same as RDS (e.g., us-east-1)
5. **Block Public Access**: 
   - Uncheck "Block all public access"
   - Check "Block public access to ACLs"
   - Leave others unchecked (for media serving)
6. Click **Create bucket**

### Step 2: Configure Bucket Permissions

1. Go to **Bucket Policy**
2. Click **Edit**
3. Add this policy (replace `evenest-media-prod` with your bucket name):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::evenest-media-prod/*"
        }
    ]
}
```

4. Click **Save changes**

### Step 3: Enable Static Website Hosting (Optional)

1. Go to **Properties** tab
2. Scroll to **Static website hosting**
3. Click **Edit**
4. Enable static website hosting
5. Set Index document: `index.html`
6. Click **Save**

### Step 4: Create IAM User for Django App

1. Go to [AWS IAM Console](https://console.aws.amazon.com/iam)
2. Click **Users** → **Create user**
3. **User name**: `evenest-app`
4. Click **Next**
5. Click **Create policy** (new tab opens)

#### Create S3 Policy

1. Go to **Policy editor** (JSON tab)
2. Paste this policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::evenest-media-prod",
                "arn:aws:s3:::evenest-media-prod/*"
            ]
        }
    ]
}
```

3. Click **Next**
4. **Policy name**: `evenest-s3-policy`
5. Click **Create policy**

#### Attach Policy to User

1. Go back to IAM Users tab
2. Click the `evenest-app` user
3. Go to **Permissions** → **Add permissions** → **Attach policies directly**
4. Search for `evenest-s3-policy`
5. Check it and click **Add permissions**

### Step 5: Create Access Keys

1. Still in IAM User page, go to **Security credentials**
2. Click **Create access key**
3. Choose **Application running outside AWS**
4. Click **Next**
5. **Description**: `Django S3 Access`
6. Click **Create access key**
7. **Copy and save**:
   - Access Key ID
   - Secret Access Key

---

## Part 3: Configure Vercel Environment Variables

Add these to [Vercel Dashboard](https://vercel.com) → Your Project → **Settings** → **Environment Variables**:

### Database Variables
```
DB_ENGINE=postgresql
DB_HOST=evenest-db.xxxxx.us-east-1.rds.amazonaws.com
DB_PORT=5432
DB_NAME=evenest_prod
DB_USER=evenest_admin
DB_PASSWORD=<your-postgres-password>
```

### S3 Variables
```
USE_S3=True
AWS_STORAGE_BUCKET_NAME=evenest-media-prod
AWS_S3_REGION_NAME=us-east-1
AWS_S3_ACCESS_KEY_ID=<your-access-key-id>
AWS_S3_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_S3_CUSTOM_DOMAIN=evenest-media-prod.s3.amazonaws.com
```

### Django Variables
```
DJANGO_SECRET_KEY=<generate-with-script-below>
DJANGO_DEBUG=False
USE_SQLITE=False
VERCEL_URL=your-vercel-url.vercel.app
```

### Generate Secure Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Part 4: Update Django Settings for S3

Update `myproject/settings.py`:

```python
import os

# S3 Configuration
USE_S3 = os.getenv('USE_S3', 'False') == 'True'

if USE_S3:
    # AWS S3 settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-east-1')
    AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'media'
    
    # Override static and media URLs
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
else:
    STATIC_URL = 'static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_ROOT = BASE_DIR / 'media'

# PostgreSQL Database Configuration
if not os.getenv('USE_SQLITE', 'True') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'evenest_prod'),
            'USER': os.getenv('DB_USER', 'evenest_admin'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
```

---

## Part 5: Deploy to Vercel

### Step 1: Update requirements.txt

```bash
pip install django-storages boto3 psycopg2-binary
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add S3 and PostgreSQL dependencies"
git push origin main
```

### Step 2: Add Environment Variables to Vercel

1. Go to [Vercel Dashboard](https://vercel.com)
2. Select your EvenNest project
3. Go to **Settings** → **Environment Variables**
4. Add all variables from Part 3 above

### Step 3: Run Migrations on Production

After Vercel builds successfully, run migrations:

```bash
# Option 1: Using Vercel CLI
vercel env pull  # Download environment variables
python manage.py migrate

# Option 2: Create a migration endpoint (recommended)
# See migration instructions below
```

### Step 4: Create Superuser for Production

```bash
# If using Vercel CLI
python manage.py createsuperuser

# Otherwise, use Django admin to create user after deployment
```

---

## Part 6: Test Everything

### Test Database Connection

```bash
python manage.py dbshell
```

### Test S3 Connection

```bash
python manage.py collectstatic --noinput
```

### Test Migration

```bash
python manage.py migrate
```

### Create Test Data

```bash
python manage.py loaddata core/fixtures/initial_products.json
```

---

## Troubleshooting

### RDS Connection Failed
```
Error: could not translate host name "evenest-db.xxxxx..." to address
```
- Check security group allows inbound TCP 5432
- Verify endpoint is correct
- Check password doesn't have special characters requiring escaping

### S3 Upload Fails
```
Error: NoCredentialsError or InvalidAccessKeyId
```
- Verify AWS_S3_ACCESS_KEY_ID and AWS_S3_SECRET_ACCESS_KEY are correct
- Ensure IAM user has S3 permissions
- Check bucket name is exact

### Vercel Build Fails
```
Error: psycopg2 not found or database driver not available
```
- Add `psycopg2-binary` to requirements.txt
- Regenerate requirements.txt: `pip freeze > requirements.txt`
- Push and redeploy

### Static Files Not Loading
```
CSS/JS not found on Vercel
```
- Run `python manage.py collectstatic`
- Ensure S3 bucket is configured
- Check AWS_S3_CUSTOM_DOMAIN is correct

---

## Cost Estimates (as of Dec 2024)

| Service | Free Tier | Monthly Cost |
|---------|-----------|--------------|
| **RDS (db.t3.micro)** | 12 months | $10-15 after free tier |
| **S3 (100GB storage)** | 1 GB for 1 year | $2-5 for media |
| **Data Transfer Out** | 1 GB/month | $0.09 per GB over limit |
| **Vercel Serverless** | 100 hours | Included in Pro plan ($20) |

**Total Estimated**: $30-40/month after free tier expires

---

## Next Steps

1. ✅ Create RDS PostgreSQL instance
2. ✅ Create S3 bucket with IAM user
3. ✅ Add environment variables to Vercel
4. ✅ Update Django settings.py (code below)
5. ✅ Push to GitHub
6. ✅ Vercel auto-deploys
7. ✅ Run migrations on production
8. ✅ Test application

**Once complete, your EvenNest app will be live!** 🎉

---

## Security Best Practices

1. **Rotate Access Keys** quarterly
2. **Use VPC Endpoint** for S3 (reduces data transfer costs)
3. **Enable CloudTrail** for audit logging
4. **Use RDS encryption** at rest
5. **Set ALLOWED_HOSTS** to exact domain only
6. **Use HTTPS only** (Vercel provides free SSL)
7. **Never commit .env files** to Git
8. **Use Vercel secrets** for sensitive data, not environment variables

