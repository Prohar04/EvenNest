# Pre-Launch Checklist

Use this checklist before deploying to Vercel. Print it or reference it during setup.

---

## Phase 1: Local Setup (Before Any Aiven Testing)

### Environment Setup
- [ ] Virtual environment created: `python -m venv venv`
- [ ] Virtual environment activated: `.\venv\Scripts\Activate.ps1`
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] `.env` file created from `.env.local`
- [ ] `.env` does NOT contain `DATABASE_URL` line

### Database Setup (SQLite)
- [ ] Migrations run successfully: `python manage.py migrate`
- [ ] No errors about "unable to open database file"
- [ ] `db.sqlite3` file exists in project root
- [ ] File permissions allow read/write

### Application Verification
- [ ] Superuser created: `python manage.py createsuperuser`
- [ ] Development server starts: `python manage.py runserver`
- [ ] No 500 errors at startup
- [ ] Web server running at `http://127.0.0.1:8000/`

### Frontend Verification
- [ ] Home page loads at `http://localhost:8000/`
- [ ] Admin page loads at `http://localhost:8000/admin/`
- [ ] Can log in with superuser credentials
- [ ] CSS/static files load (page not plain HTML)
- [ ] Images/media load correctly
- [ ] No JavaScript console errors
- [ ] No 404 errors for static files

### Code Quality
- [ ] No Python syntax errors: `python -m py_compile myproject/settings.py`
- [ ] No obvious import errors
- [ ] Settings file has no hardcoded secrets
- [ ] `.gitignore` includes `.env`, `db.sqlite3`, `venv/`

---

## Phase 2: Aiven Testing (Optional but Recommended)

### Connection Testing
- [ ] Aiven MySQL service is running
- [ ] Connection details obtained from Aiven dashboard
- [ ] Copied Aiven URL (example: `mysql://avnadmin:PASS@host:port/db`)
- [ ] Removed `ssl-mode=REQUIRED` from URL for Django
- [ ] Network access rule allows your IP

### Environment Variable Setup
- [ ] PowerShell session open in project directory
- [ ] Run: `$env:DATABASE_URL = 'mysql://avnadmin:PASSWORD@host:port/db'`
- [ ] Verify with: `echo $env:DATABASE_URL`

### Database Connection
- [ ] Run: `python manage.py dbshell`
- [ ] MySQL prompt appears (not an error)
- [ ] Type `exit` to close
- [ ] Connection successful (no timeout/auth errors)

### Migrations on Aiven
- [ ] Run: `python manage.py migrate`
- [ ] All migrations apply without errors
- [ ] No SSL errors
- [ ] No connection timeout errors
- [ ] Aiven dashboard shows tables created (verify with SQL editor)

### Verification
- [ ] Run: `python manage.py shell`
- [ ] Test: `from core.models import YourModel; YourModel.objects.count()`
- [ ] Returns count without error
- [ ] Type `exit()` to close
- [ ] Unset variable: `Remove-Item env:DATABASE_URL`
- [ ] Verify unset: `echo $env:DATABASE_URL` (should be blank)

---

## Phase 3: Git Preparation

### Repository Status
- [ ] All changes staged: `git add -A`
- [ ] Changes committed: `git commit -m "Production-ready Django setup"`
- [ ] Remote added: `git remote -v` shows origin
- [ ] Code pushed: `git push origin main`
- [ ] GitHub/GitLab shows latest commit

### .gitignore Review
- [ ] `.env*` entries present
- [ ] `db.sqlite3` entry present
- [ ] `venv/` entry present
- [ ] `__pycache__/` entry present
- [ ] `*.pyc` entry present
- [ ] `staticfiles/` entry present
- [ ] `.vercel/` entry present (optional but recommended)

---

## Phase 4: Vercel Setup

### Vercel CLI Installation
- [ ] Vercel CLI installed: `npm install -g vercel`
- [ ] Vercel account created at https://vercel.com
- [ ] Git connected to Vercel (GitHub/GitLab/Bitbucket)

### Vercel Project Creation
- [ ] Project created in Vercel dashboard
- [ ] Project name set (e.g., "evennest")
- [ ] Git repo connected
- [ ] Framework auto-detected as Django (or manually set)

### Environment Variables - Part 1
- [ ] Vercel dashboard open → Project Settings
- [ ] Go to Environment Variables section
- [ ] **Variable 1: DJANGO_DEBUG**
  - [ ] Name: `DJANGO_DEBUG`
  - [ ] Value: `False`
  - [ ] Environments: Production, Preview, Development (all selected)
  - [ ] Saved

- [ ] **Variable 2: DJANGO_SECRET_KEY**
  - [ ] Generate locally: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
  - [ ] Copy generated key
  - [ ] Name: `DJANGO_SECRET_KEY`
  - [ ] Value: [pasted key from above]
  - [ ] Environments: Production, Preview, Development (all selected)
  - [ ] Saved

- [ ] **Variable 3: DATABASE_URL**
  - [ ] Get from Aiven dashboard → MySQL service → Overview
  - [ ] URL format: `mysql://avnadmin:PASSWORD@host:port/defaultdb`
  - [ ] **Important:** Remove `ssl-mode=REQUIRED` from end
  - [ ] Name: `DATABASE_URL`
  - [ ] Value: [Aiven URL without ssl-mode]
  - [ ] Environments: Production only (not Preview/Development)
  - [ ] Saved

- [ ] **Variable 4: PYTHONUNBUFFERED**
  - [ ] Name: `PYTHONUNBUFFERED`
  - [ ] Value: `1`
  - [ ] Environments: Production, Preview, Development (all selected)
  - [ ] Saved

### Verify Settings Files
- [ ] `vercel.json` exists and is valid JSON
- [ ] `myproject/settings.py` exists and has no syntax errors
- [ ] `requirements.txt` exists and has no duplicates
- [ ] `myproject/__init__.py` has PyMySQL setup
- [ ] All files committed and pushed to git

---

## Phase 5: Initial Deployment

### Pre-Deployment Checks
- [ ] All Phase 1-4 items completed
- [ ] Latest code pushed to main branch: `git push origin main`
- [ ] Vercel environment variables all set
- [ ] No uncommitted changes locally

### Deploy to Vercel
- [ ] Terminal open in project directory
- [ ] Virtual environment activated (optional but safe)
- [ ] Run: `vercel --prod`
- [ ] Follow prompts (usually just hit Enter to use defaults)
- [ ] Deployment begins
- [ ] URL provided: `https://your-project.vercel.app`

### Monitor Deployment
- [ ] Build starts in Vercel dashboard
- [ ] "Installing dependencies" step completes
- [ ] "python manage.py collectstatic" runs without errors
- [ ] Deployment shows "Ready"
- [ ] No build errors in logs

### View Logs
- [ ] Terminal: `vercel logs --tail`
- [ ] Logs stream in real-time
- [ ] No critical errors (INFO/WARNING is OK)
- [ ] Watch for at least 30 seconds

---

## Phase 6: Production Verification

### Basic Functionality
- [ ] Visit deployment URL in browser
- [ ] Home page loads (not 500 error)
- [ ] Page title and content correct
- [ ] No JavaScript console errors (F12)
- [ ] CSS loads (page is styled, not plain)
- [ ] Images load correctly

### Admin Access
- [ ] Visit `/admin/` on deployment
- [ ] Login page appears
- [ ] Try login with **production superuser credentials**
  - [ ] If local credentials don't work, see "Creating Production Superuser" below
- [ ] Admin dashboard loads
- [ ] Can view core app models
- [ ] Can navigate around admin

### Database Connection
- [ ] Admin works (proves DB connection works)
- [ ] Create a test item in admin (or click existing)
- [ ] Item displays correctly
- [ ] No database errors in logs

### Static Files
- [ ] All CSS loads (check with F12 Network tab)
- [ ] All JavaScript loads
- [ ] All images load
- [ ] No 404 errors for `/static/` files
- [ ] Vercel logs show `/static/` routes working

### Error Monitoring
- [ ] Run: `vercel logs` (in terminal)
- [ ] Look for ERROR or CRITICAL level messages
- [ ] No "ModuleNotFoundError" messages
- [ ] No "OperationalError" messages (database errors)
- [ ] No "TemplateDoesNotExist" messages

---

## Phase 7: Post-Deployment

### Create Production Superuser (if needed)
If you can't log in with local credentials, create a new superuser on production:

```powershell
# Set DATABASE_URL to Aiven
$env:DATABASE_URL = 'mysql://avnadmin:PASSWORD@host:port/db'

# Create superuser
python manage.py createsuperuser

# Follow prompts and create credentials
# Note: Use different password than local dev

# Unset after
Remove-Item env:DATABASE_URL
```

Then try logging in with new credentials at `https://your-project.vercel.app/admin/`

### Monitoring Setup
- [ ] Save Vercel logs command: `vercel logs --tail`
- [ ] Monitor for first 24 hours post-deployment
- [ ] Check daily for error patterns
- [ ] Set up error notifications (optional: in Vercel dashboard)

### Backups
- [ ] Aiven MySQL backups enabled (check dashboard)
- [ ] Backup retention set appropriately
- [ ] Know how to restore from backup if needed

---

## Phase 8: Cleanup & Handoff

### Local Repository
- [ ] All changes committed: `git log` shows recent commit
- [ ] `.env` file exists but is gitignored
- [ ] `db.sqlite3` exists locally but is gitignored
- [ ] Virtual environment folder exists but is gitignored

### Documentation
- [ ] This checklist completed
- [ ] Read `QUICKSTART.md` for future reference
- [ ] Bookmarked `VERCEL_DEPLOYMENT_COMPLETE_GUIDE.md`
- [ ] Shared guides with team if applicable

### Production Access
- [ ] Vercel URL bookmarked: `https://your-project.vercel.app`
- [ ] Vercel dashboard bookmarked: https://vercel.com/dashboard
- [ ] Aiven dashboard bookmarked: https://console.aiven.io
- [ ] Aiven connection string saved securely (password manager)

### Team Communication
- [ ] Team notified of deployment
- [ ] URL shared with team
- [ ] Access credentials shared securely
- [ ] Deployment notes documented
- [ ] Any rollback plan communicated

---

## Emergency Procedures

### If Deployment Fails

**Step 1: Check Logs**
```powershell
vercel logs --follow
```

**Step 2: Check Common Issues**
- [ ] `DATABASE_URL` set in Vercel (without `ssl-mode=REQUIRED`)
- [ ] `DJANGO_SECRET_KEY` is strong and set
- [ ] `DJANGO_DEBUG=False` in Vercel
- [ ] `requirements.txt` has all packages
- [ ] No syntax errors in `settings.py`

**Step 3: Redeploy**
```powershell
git push origin main
vercel --prod
```

### If Database Connection Fails

**Check in Order:**
1. [ ] `DATABASE_URL` format correct (no ssl-mode)
2. [ ] Password in URL correct (check Aiven dashboard)
3. [ ] Aiven firewall allows Vercel IP (usually automatic)
4. [ ] Aiven service is running
5. [ ] Try connecting locally first: `$env:DATABASE_URL = '...' && python manage.py dbshell`

### If Static Files Don't Load

1. [ ] Check `vercel.json` has static route
2. [ ] Run `python manage.py collectstatic --noinput` locally
3. [ ] Verify `staticfiles/` directory created
4. [ ] Check Vercel logs for static file errors
5. [ ] Redeploy: `vercel --prod`

### If Admin Won't Load

1. [ ] Check if you can load home page (DB connection works?)
2. [ ] Try creating superuser with Aiven `DATABASE_URL` set
3. [ ] Check `vercel logs` for authentication errors
4. [ ] Clear browser cookies and try again

### If Need to Rollback

```powershell
# Go back to previous commit
git revert HEAD~1  # or reset to previous version

# Push to git
git push origin main

# Vercel will auto-redeploy with previous code
# Or manually redeploy: vercel --prod
```

---

## Success Indicators

You're done when:

✅ Local development works with SQLite  
✅ Can set `$env:DATABASE_URL` and migrations work  
✅ Vercel deployment completes without build errors  
✅ Production URL loads home page  
✅ Admin login works with production credentials  
✅ Static files load correctly  
✅ `vercel logs` shows no critical errors  
✅ All items in this checklist are checked

---

## Maintenance Going Forward

### Daily
- [ ] Monitor `vercel logs --tail` for errors
- [ ] Check admin for unexpected data issues

### Weekly
- [ ] Review Aiven backup status
- [ ] Check Vercel analytics
- [ ] Update dependencies if security updates available

### Monthly
- [ ] Run `pip list --outdated` to check for updates
- [ ] Review security advisories
- [ ] Test database backup/restore procedures
- [ ] Review access logs

---

**Date Deployed:** _______________  
**Deployed By:** _______________  
**Notes:** _______________

---

*End of Pre-Launch Checklist*
