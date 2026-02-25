# 🎉 CiTea Coolers v2.0 - START HERE

**Status**: ✅ PRODUCTION READY  
**Version**: 2.0  
**Last Updated**: February 2, 2026

---

## ⚡ 30-Second Quick Start

```bash
# Step 1: Install dependencies (first time only)
pip install -r requirements.txt

# Step 2: Initialize database (first time only)
python init_db.py

# Step 3: Run the application
python run.py
```

Then open: **http://localhost:5000**

---

## 📋 Documentation Guide

### 🚀 **Ready to Run?**
👉 Go to [README.md](README.md) - Complete project overview

### 🛠️ **Need Setup Help?**
👉 Go to [SETUP_GUIDE_NEW.md](SETUP_GUIDE_NEW.md) - Detailed installation guide

### 📚 **Want Quick Reference?**
👉 Go to [QUICK_REFERENCE_v2.md](QUICK_REFERENCE_v2.md) - URLs, commands, features

### 🎨 **Curious About Features?**
👉 Go to [FEATURES_GUIDE.md](FEATURES_GUIDE.md) - Complete feature list

### ⚠️ **What's Not Available?**
👉 Go to [SYSTEM_LIMITATIONS.md](SYSTEM_LIMITATIONS.md) - Known limitations

### 📦 **Deploying to Production?**
👉 Go to [DEPLOYMENT_CHECKLIST_NEW.md](DEPLOYMENT_CHECKLIST_NEW.md) - Deployment guide

### ✨ **What's New in v2.0?**
👉 Go to [IMPLEMENTATION_SUMMARY_v2.md](IMPLEMENTATION_SUMMARY_v2.md) - Latest updates

---

## 🎯 What is CiTea Coolers?

A complete e-commerce and messaging platform for beverage retailers featuring:

### For Customers 👥
- 📝 User registration and authentication
- 🍵 Browse products and menu
- 🛒 Shopping cart system
- 🚀 Direct "Buy Now" checkout
- 💬 Real-time chat with admin
- 👤 Profile management with photo upload
- 📦 Order tracking

### For Admin 🛠️
- 📊 Sales dashboard
- 📦 Product and category management
- 📥 Order management and status updates
- 💬 Customer messaging
- 👤 View customer profiles and history
- 🔔 Real-time order notifications

---

## 🌐 Quick Links

### Customer Portal
| Feature | URL |
|---------|-----|
| Home | http://localhost:5000/ |
| Menu | http://localhost:5000/menu |
| Cart | http://localhost:5000/cart |
| Checkout | http://localhost:5000/checkout |
| Profile | http://localhost:5000/profile |
| Chat | http://localhost:5000/chat |

### Admin Panel
| Feature | URL |
|---------|-----|
| Dashboard | http://localhost:5000/admin/dashboard |
| Products | http://localhost:5000/admin/products |
| Categories | http://localhost:5000/admin/categories |
| Orders | http://localhost:5000/admin/order |
| Messages | http://localhost:5000/admin/messages |

---

## ✅ Verification Checklist

After running the app, verify:

- [ ] App starts at http://localhost:5000
- [ ] Can register new account
- [ ] Can login successfully
- [ ] Can view menu and products
- [ ] Can use "Buy Now" checkout
- [ ] Can complete order
- [ ] Can access profile
- [ ] Can upload profile picture
- [ ] Can chat with admin
- [ ] Admin can see user profile picture
- [ ] Enter key sends messages in admin chat

---

## 🔧 Requirements

- **Python**: 3.7 or higher
- **RAM**: 512 MB minimum (2 GB recommended)
- **Storage**: 100 MB free space
- **Browser**: Chrome, Firefox, Safari, or Edge (latest)
- **Internet**: Required for uploads and messaging

---

## 🆕 What's New in v2.0?

✨ **Latest Features**:
- ✅ Profile picture uploads
- ✅ Enter key to send messages in admin chat
- ✅ Admin can see user profile pictures in conversations
- ✅ Completed orders removed from notification bell
- ✅ No order notifications cluttering admin messages
- ✅ Cleaner homepage for non-logged-in users
- ✅ Direct "Buy Now" checkout flow
- ✅ Real-time order notifications

---

## 🐛 Troubleshooting

### Port 5000 already in use?
Edit `run.py` and change port to `5001` (or another available port)

### Database not creating?
Run: `python init_db.py`

### Images not loading?
Verify `app/static/uploads/` directories exist

### Cart not persisting?
Enable LocalStorage in browser (disable private/incognito mode)

For more help, see the relevant documentation file or [README.md](README.md)

---

## 📚 Full Documentation

All documentation is organized in separate files:

1. **[README.md](README.md)** - Main project overview
2. **[SETUP_GUIDE_NEW.md](SETUP_GUIDE_NEW.md)** - Installation & configuration
3. **[QUICK_REFERENCE_v2.md](QUICK_REFERENCE_v2.md)** - Quick reference card
4. **[FEATURES_GUIDE.md](FEATURES_GUIDE.md)** - Complete feature list
5. **[SYSTEM_LIMITATIONS.md](SYSTEM_LIMITATIONS.md)** - Known limitations
6. **[DEPLOYMENT_CHECKLIST_NEW.md](DEPLOYMENT_CHECKLIST_NEW.md)** - Production deployment
7. **[IMPLEMENTATION_SUMMARY_v2.md](IMPLEMENTATION_SUMMARY_v2.md)** - What's new

---

## 🚀 Next Steps

1. **Run the app** (see Quick Start above)
2. **Choose a guide** from the Documentation Guide section
3. **Test features** using the Verification Checklist
4. **Review limitations** before deploying
5. **Deploy to production** when ready

---

## 💡 Pro Tips

- 💾 **Database Backup**: Copy `site.db` before major updates
- 🔑 **Admin Access**: See docs for creating admin accounts
- 📱 **Mobile Friendly**: App is responsive and works on mobile
- 🎨 **Customizable**: Change colors and branding in CSS files
- ⚡ **Fast**: Optimized for performance

---

## 🎉 Ready?

Everything is set up and ready to go!

👉 **Run** `python run.py` **and start exploring!**

For detailed help, choose your guide from the Documentation Guide section above.

---

**CiTea Coolers v2.0 - Your Complete E-Commerce & Messaging Solution**

Last Updated: February 2, 2026 ✅
