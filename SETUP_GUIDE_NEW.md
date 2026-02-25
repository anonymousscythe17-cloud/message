# 🍵 CiTea Coolers - Complete Setup Guide

**Status**: ✅ PRODUCTION READY  
**Version**: 2.0  
**Last Updated**: February 2, 2026

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [System Requirements](#system-requirements)
3. [Installation Steps](#installation-steps)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [Troubleshooting](#troubleshooting)
7. [Support](#support)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- SQLite3 (included with Python)

### Installation (3 steps)

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Initialize database
python init_db.py

# Step 3: Run the application
python run.py
```

Then open your browser to: **http://localhost:5000**

---

## 💻 System Requirements

### Minimum Requirements
- **CPU**: 1 GHz processor
- **RAM**: 512 MB
- **Storage**: 100 MB free space
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Internet**: Required for uploads and messaging

### Recommended
- **CPU**: 2+ GHz processor
- **RAM**: 2 GB
- **Storage**: 500 MB free space
- **Connection**: Broadband (5+ Mbps)

### Supported Operating Systems
- ✅ Windows (7, 10, 11)
- ✅ macOS (10.14+)
- ✅ Linux (Ubuntu 18.04+)

---

## 🔧 Installation Steps

### Step 1: Clone or Download Project

```bash
# Option A: Using git
git clone [repository-url]
cd Citea_messenger

# Option B: Manual download
# Extract the ZIP file to your desired location
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask (web framework)
- Flask-SQLAlchemy (database ORM)
- Werkzeug (security utilities)

### Step 3: Initialize Database

```bash
python init_db.py
```

This creates:
- `site.db` (SQLite database file)
- Database tables for users, products, orders, messages, etc.

### Step 4: Create Upload Directories

```bash
# Directories are auto-created by the app, but you can verify:
# app/static/uploads/profile_pics/
# app/static/uploads/message_images/
# app/static/uploads/products/
```

---

## ⚙️ Configuration

### Database Configuration (config.py)

#### SQLite (Default - Recommended for Development)
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
```

#### PostgreSQL (Production)
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/citea_db'
```

#### MySQL (Production)
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/citea_db'
```

### Application Settings (config.py)

```python
# Debug mode (set to False in production)
DEBUG = True

# Secret key for session management
SECRET_KEY = 'your-secret-key-here'

# Maximum file upload size (in bytes)
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB

# Upload folder settings
UPLOAD_FOLDER = 'app/static/uploads/'
```

### Port Configuration (run.py)

```python
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
```

Change `port=5000` to use a different port if 5000 is already in use.

---

## ▶️ Running the Application

### Development Mode

```bash
python run.py
```

**Features**:
- Auto-reload on file changes
- Debug mode enabled
- Detailed error messages
- Logging to console

**Access**:
- User Portal: http://localhost:5000/
- Admin Panel: http://localhost:5000/admin/dashboard

### Production Mode

```python
# In run.py, change:
app.run(debug=False, port=5000)
```

Or use a production server:

```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app

# Using uWSGI
pip install uwsgi
uwsgi --http :5000 --wsgi-file run.py --callable app
```

---

## 🌐 Application URLs

### Customer Portal

| Page | URL | Access |
|------|-----|--------|
| Home | http://localhost:5000/ | Public (Login required for menu) |
| Login | http://localhost:5000/login | Public |
| Register | http://localhost:5000/register | Public |
| Menu | http://localhost:5000/menu | Logged-in users only |
| Cart | http://localhost:5000/cart | Logged-in users only |
| Checkout | http://localhost:5000/checkout | Logged-in users only |
| Profile | http://localhost:5000/profile | Logged-in users only |
| Chat | http://localhost:5000/chat | Logged-in users only |

### Admin Panel

| Page | URL | Access |
|------|-----|--------|
| Dashboard | http://localhost:5000/admin/dashboard | Admin only |
| Products | http://localhost:5000/admin/products | Admin only |
| Add Product | http://localhost:5000/admin/product/add | Admin only |
| Categories | http://localhost:5000/admin/categories | Admin only |
| Orders | http://localhost:5000/admin/order | Admin only |
| Messages | http://localhost:5000/admin/messages | Admin only |

---

## 🗄️ Database Schema

### Users Table
```
id (Integer, Primary Key)
username (String, Unique)
email (String, Unique)
password (String, Hashed)
profile_pic (String, Optional)
created_at (DateTime)
```

### Products Table
```
id (Integer, Primary Key)
name (String)
price (Float)
image (String)
variants (JSON)
category_id (Integer, Foreign Key)
```

### Orders Table
```
id (Integer, Primary Key)
customer_name (String)
product_name (String)
quantity (Integer)
total_price (Float)
order_date (DateTime)
status (String: Pending/Completed/Cancelled)
```

### Messages Table
```
id (Integer, Primary Key)
conversation_id (String)
sender_id (Integer)
sender_name (String)
sender_type (String: user/admin)
content (Text)
message_type (String: text/image/order_notification)
created_at (DateTime)
is_read (Boolean)
```

### Categories Table
```
id (Integer, Primary Key)
name (String)
description (String)
```

---

## 📁 Project Structure

```
Citea_messenger/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── user_routes.py       # User/customer routes
│   ├── admin_routes.py      # Admin routes
│   ├── product_routes.py    # Product management routes
│   ├── categories_routes.py # Category management routes
│   ├── froms.py             # Forms (if any)
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── uploads/
│   │       ├── profile_pics/
│   │       ├── message_images/
│   │       └── products/
│   └── __init__.py
├── templates/
│   ├── templates/           # Customer pages
│   │   ├── Index.html
│   │   ├── Login.html
│   │   ├── Register.html
│   │   ├── Menu.html
│   │   ├── Add to cart.html
│   │   ├── Check out.html
│   │   ├── Order succes.html
│   │   ├── Profile.html
│   │   └── Chat.html
│   └── admin/               # Admin pages
│       ├── base.html
│       ├── dashboard.html
│       ├── products.html
│       ├── categories.html
│       ├── order.html
│       ├── message.html
│       └── user-profile.html
├── config.py                # Configuration
├── init_db.py               # Database initialization
├── run.py                   # Entry point
├── requirements.txt         # Python dependencies
└── site.db                  # SQLite database (auto-created)
```

---

## 🎨 Customization

### Brand Colors

Edit in CSS files:
```css
/* Primary colors */
--primary-dark: #5D2906;    /* Dark brown */
--primary: #D35400;         /* Orange */
--accent: #FFD700;          /* Gold */
--light: #f8f8f8;           /* Light gray */
```

### Application Name

Update in templates:
```html
<div class="nav-brand">🍵 Your Store Name</div>
```

### Contact Information

Update in `templates/templates/Index.html`:
```html
<div class="info-item">
    <strong>📍 Location</strong><br><br>
    Your City, Province - Branch Name
</div>
```

---

## 🐛 Troubleshooting

### Issue: "Address already in use" error

**Problem**: Port 5000 is already being used

**Solution**:
```bash
# Option 1: Kill the process using port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID [PID] /F

# Option 2: Use a different port
# Edit run.py and change port=5000 to port=5001
```

### Issue: Database not found or tables missing

**Problem**: Database hasn't been initialized

**Solution**:
```bash
python init_db.py
```

### Issue: Images not loading

**Problem**: Images uploaded but not displaying

**Solution**:
1. Verify `app/static/uploads/` directories exist
2. Check file permissions
3. Verify image path in database: `SELECT * FROM user;`

### Issue: Cart not persisting

**Problem**: Items disappear when page reloads

**Solution**:
1. Check browser LocalStorage is enabled
2. Check if private/incognito mode is enabled
3. Clear browser cache: `Ctrl+Shift+Delete`

### Issue: Login/Registration not working

**Problem**: "Invalid credentials" or "User already exists"

**Solution**:
1. Verify database tables were created
2. Check username doesn't already exist
3. Verify password matches confirm password
4. Check for typos in email

### Issue: Admin routes not accessible

**Problem**: 404 error on admin pages

**Solution**:
1. Verify admin_routes.py is imported in `app/__init__.py`
2. Check admin blueprint is registered
3. Verify database has admin data

---

## 📊 Performance Tips

### Optimize Database
```python
# Create indexes for frequently searched fields
# In models.py, add to User model:
__table_args__ = (db.Index('idx_username', 'username'),)
```

### Cache Static Files
```python
# In config.py
SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year
```

### Limit API Responses
```python
# In user_routes.py
MESSAGES_PER_PAGE = 50
PRODUCTS_PER_PAGE = 20
```

---

## 🔒 Security Checklist

- [ ] Set `DEBUG = False` in production
- [ ] Change `SECRET_KEY` to a random value
- [ ] Use HTTPS in production
- [ ] Validate all user inputs
- [ ] Sanitize database queries
- [ ] Keep dependencies updated: `pip install --upgrade pip -r requirements.txt`
- [ ] Use strong passwords
- [ ] Enable CSRF protection
- [ ] Regularly backup database

---

## 📞 Support & Troubleshooting

### Getting Help

1. **Check error messages** - Flask provides detailed error messages in debug mode
2. **Review logs** - Check console output for error details
3. **Check documentation** - Refer to feature-specific guides
4. **Database verification** - Use SQLite browser to inspect database

### Common Commands

```bash
# Create fresh database
python init_db.py

# Run in debug mode
python run.py

# Install specific version
pip install Flask==2.0.0

# Create backup
cp site.db site.db.backup
```

---

## 📝 Version History

### Version 2.0 (February 2, 2026)
- ✅ Buy Now checkout flow
- ✅ Order notifications to admin
- ✅ User profile viewing from admin
- ✅ Homepage restricted access for non-logged-in users
- ✅ Message system improvements
- ✅ Product search functionality

### Version 1.0 (January 28, 2026)
- ✅ User authentication
- ✅ Product management
- ✅ Shopping cart
- ✅ Order management
- ✅ Messaging system
- ✅ Profile management

---

## 📄 License & Credits

**Project**: CiTea Coolers - Messenger Application  
**Created**: January 28, 2026  
**Status**: Production Ready  

**Built with**:
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- HTML5/CSS3 (Frontend)
- JavaScript (Frontend Logic)

---

**For questions or support, please refer to the SYSTEM_LIMITATIONS.md and FEATURES_GUIDE.md files.**
