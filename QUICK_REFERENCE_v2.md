# 🚀 Quick Reference Guide - CiTea Coolers v2.0

**Last Updated**: February 2, 2026  

---

## 📍 Application URLs

### Customer Portal
- **Home**: http://localhost:5000/
- **Login**: http://localhost:5000/login
- **Register**: http://localhost:5000/register
- **Menu**: http://localhost:5000/menu
- **Cart**: http://localhost:5000/cart
- **Checkout**: http://localhost:5000/checkout
- **Profile**: http://localhost:5000/profile
- **Chat**: http://localhost:5000/chat

### Admin Panel
- **Dashboard**: http://localhost:5000/admin/dashboard
- **Products**: http://localhost:5000/admin/products
- **Categories**: http://localhost:5000/admin/categories
- **Orders**: http://localhost:5000/admin/order
- **Messages**: http://localhost:5000/admin/messages

---

## ⚡ Quick Start (3 Steps)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Initialize database
python init_db.py

# 3. Run application
python run.py
```

---

## 🎯 Main Features

### For Customers ✅
- ✅ Register & Login
- ✅ Browse Products & Menu
- ✅ Add to Cart
- ✅ Buy Now (Direct Checkout)
- ✅ Checkout & Order
- ✅ View Order History
- ✅ Chat with Admin
- ✅ Upload Profile Picture

### For Admin ✅
- ✅ Product Management
- ✅ Category Management
- ✅ Order Management
- ✅ Customer Messages
- ✅ View Customer Profiles
- ✅ Analytics Dashboard

---

## 🔐 Access Control

| Feature | Public | Login Required |
|---------|--------|---|
| Home | ✅ | ✅ (limited) |
| Menu | ❌ | ✅ |
| Cart | ❌ | ✅ |
| Checkout | ❌ | ✅ |
| Profile | ❌ | ✅ |
| Chat | ❌ | ✅ |

---

## 📋 System Requirements

- **Python**: 3.7+
- **RAM**: 512 MB minimum
- **Storage**: 100 MB
- **Browser**: Chrome, Firefox, Safari, Edge

---

## 🎨 Color Scheme

```
Primary Dark:  #5D2906 (Dark Brown)
Primary:       #D35400 (Orange)
Accent:        #FFD700 (Gold)
Background:    #f8f8f8 (Light Gray)
```

---

## 📁 Key Files

```
app/
├── models.py           # Database models
├── user_routes.py      # Customer routes
├── admin_routes.py     # Admin routes
├── product_routes.py   # Product routes
└── categories_routes.py # Category routes

templates/
├── templates/          # Customer pages
│   ├── Index.html
│   ├── Menu.html
│   ├── Chat.html
│   └── ...
└── admin/              # Admin pages
    ├── dashboard.html
    ├── message.html
    └── ...

config.py              # Configuration
init_db.py            # Database setup
run.py                # Entry point
site.db               # Database
```

---

## 💻 Common Commands

```bash
# Start app
python run.py

# Initialize database
python init_db.py

# Install packages
pip install -r requirements.txt

# Create backup
cp site.db site.db.backup

# Restore backup
cp site.db.backup site.db

# Change port (edit run.py)
# Change: port=5000 to port=5001
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 in use | Change port in run.py to 5001 |
| Database not found | Run: python init_db.py |
| Can't upload images | Check app/static/uploads/ folder |
| Cart not saving | Enable browser LocalStorage |
| Login fails | Verify user exists, check password |

---

## 📊 Database Tables

1. **user** - Customer accounts
2. **product** - Product listings
3. **order** - Customer orders
4. **message** - Chat messages
5. **categories** - Product categories
6. **cart** - Shopping carts
7. **cartitem** - Cart items

---

## 🔄 Workflow

### Customer Journey
```
Register → Login → Browse Menu → 
Add to Cart (or Buy Now) → Checkout → 
Order Confirmation → Chat with Admin
```

### Order Notification
```
Customer Places Order → 
Admin Receives Message Notification → 
Admin Updates Order Status → 
Customer Notified
```

---

## 📞 Documentation Files

- **SETUP_GUIDE_NEW.md** - Complete setup
- **SYSTEM_LIMITATIONS.md** - Limitations & workarounds
- **FEATURES_GUIDE.md** - All features & roadmap
- **DEPLOYMENT_CHECKLIST_NEW.md** - Deployment guide

---

## ✅ What's New in v2.0

- ✅ Buy Now direct checkout
- ✅ Order notifications to admin
- ✅ Customer profile viewing
- ✅ Homepage access restriction
- ✅ Logout functionality
- ✅ Improved documentation

---

## 🚀 Ready to Deploy?

1. ✅ Check all features working
2. ✅ Backup database
3. ✅ Set DEBUG=False in config
4. ✅ Change SECRET_KEY
5. ✅ Deploy to production
6. ✅ Monitor for errors

See **DEPLOYMENT_CHECKLIST_NEW.md** for details.

---

## 🤝 Support

Having issues?
1. Check error message
2. Review documentation
3. Check database integrity
4. Clear browser cache
5. Restart application

---

**Version**: 2.0  
**Status**: ✅ Production Ready  
**Last Updated**: February 2, 2026
