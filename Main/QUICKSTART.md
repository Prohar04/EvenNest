# EventNest - Quick Start Guide

Get EventNest up and running in 5 minutes!

## 🚀 Local Setup (5 minutes)

### 1. Install Dependencies
```bash
cd D:\EventNest\Main
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Load Sample Data
```bash
python manage.py loaddata fixtures/initial_products.json
```

### 4. Create Admin User
```bash
python manage.py createsuperuser
```

### 5. Start Server
```bash
python manage.py runserver
```

Visit **http://localhost:8000** 🎉

## 📖 What You Get

### Public Pages
- **Home**: Hero section, service showcase, featured products
- **Services**: Browse all professional services
- **Service Detail**: Service information and booking
- **Store**: Shop for event essentials
- **Authentication**: Login and sign up

### Admin Features (at `/admin/`)
- Manage services and categories
- Manage store inventory
- View orders and bookings
- User management

## 🎨 Design Highlights

- **Black Theme** (#0a0e27) - Elegant and professional
- **Purple Accent** (#6366f1) - Modern and vibrant
- **Fully Responsive** - Works on all devices
- **Smooth Animations** - Professional interactions

## 📁 Key Files

| File | Purpose |
|------|---------|
| `core/static/css/theme.css` | Design system & styles |
| `core/templates/base_new.html` | Main layout |
| `core/templates/home_new.html` | Home page |
| `core/views.py` | Business logic |
| `core/models.py` | Database models |

## 🔧 Customization

### Change Colors
Edit `core/static/css/theme.css`:
```css
--color-accent: #6366f1;  /* Change this color */
--color-black: #0a0e27;   /* Background color */
```

### Add Services
1. Go to `/admin/`
2. Click "Services" → "Add Service"
3. Fill in details and upload image
4. Click "Save"

### Add Store Items
1. Go to `/admin/`
2. Click "Store Items" → "Add Store Item"
3. Fill in details and upload image
4. Click "Save"

## 🌐 Deploy to Vercel

### Quick Deploy
```bash
git add -A
git commit -m "Ready for deployment"
git push origin main
```

Then:
1. Go to https://vercel.com/new
2. Select EventNest repository
3. Add environment variables
4. Click "Deploy"

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

## 📝 Environment Variables

Create `.env` file:
```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

For production, use `.env.production` with MySQL database URL.

## 🆘 Common Issues

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Error
```bash
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## 📚 Documentation

- **Full README**: `README.md`
- **Deployment Guide**: `DEPLOYMENT_GUIDE.md`
- **Django Docs**: https://docs.djangoproject.com

## 🎯 Next Steps

1. ✅ Run locally
2. ✅ Customize colors and content
3. ✅ Add your services and products
4. ✅ Deploy to Vercel
5. ✅ Configure custom domain
6. ✅ Set up email notifications
7. ✅ Add payment processing

## 💡 Tips

- Use Django admin to manage content
- Enable caching for better performance
- Regular database backups for production
- Monitor error logs weekly
- Test on mobile devices

## 🎉 You're All Set!

Your EventNest platform is ready to go. Start adding services and products, then deploy to production!

Need help? Check the `README.md` or `DEPLOYMENT_GUIDE.md` for more details.

---

Happy coding! 🚀
