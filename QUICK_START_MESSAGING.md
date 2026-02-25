# 🚀 Quick Start: New Messaging & Profile Features

## What's Changed?

Your CiTea Coolers app now has:
1. ✨ **Facebook Messenger-style Chat**
2. 📸 **Profile Picture Upload**
3. 📢 **Order Status Notifications**

---

## ⚡ Quick Setup

### Step 1: Delete Old Database (if updating existing app)
```bash
# Delete the old database to apply new schema
del site.db
```

### Step 2: Run the App
```bash
python run.py
```

The app will automatically create new database tables with the updated schema.

### Step 3: Register a Test Account
- Go to http://localhost:5000/register
- Create a new user account

### Step 4: Test Profile Picture Upload
1. Go to http://localhost:5000/profile
2. Click on the avatar (profile picture circle)
3. Select an image file
4. See success message appear

### Step 5: Test Messaging
1. Go to http://localhost:5000/chat
2. Type a message and press Enter
3. Message appears with timestamp
4. Auto-refreshes every 2 seconds

---

## 📸 Profile Picture Upload

**How it works:**
- Click on the avatar in your profile
- Select a PNG, JPG, or GIF image (max 5MB)
- Picture updates instantly
- Picture displays in chat if admin replies

**Storage location:**
- Files saved to: `app/static/uploads/profile_pics/`
- Old picture is automatically deleted

---

## 💬 Messaging System

**Features:**
- Modern chat interface
- Auto-refresh every 2 seconds
- Timestamps on all messages
- Admin messages show "ADMIN" badge
- Order status notifications in green

**Message Types:**
1. Regular messages (text)
2. Order notifications (special green styling)

---

## 📢 Order Notifications (Admin Feature)

### Send an order notification:

**Via API:**
```
POST /api/notify-order-status/1/completed
```

**Possible statuses:**
- `confirmed` - Order is confirmed
- `shipped` - Order shipped
- `completed` - Order done
- `cancelled` - Order cancelled

**Example responses:**
```
✔️ Order confirmed
🚚 Order shipped
✅ Order completed
❌ Order cancelled
```

---

## 🔧 File Structure

New/Modified files:
```
app/
  models.py (UPDATED - User.profile_pic, Message fields)
  user_routes.py (UPDATED - new endpoints)
  static/
    uploads/
      profile_pics/ (NEW FOLDER - created automatically)

templates/
  templates/
    Chat.html (UPDATED - new messenger UI)
    Profile.html (UPDATED - picture upload)

MESSAGING_PROFILE_UPDATES.md (NEW - detailed docs)
```

---

## 🧪 Test the Features

### Test 1: Upload Profile Picture
```
1. Go to /profile
2. Click avatar
3. Select image
4. Confirm success message
```

### Test 2: Send Messages
```
1. Go to /chat
2. Type: "Hello!"
3. Press Enter
4. Message appears on right
5. Auto-refreshes every 2 seconds
```

### Test 3: Order Notification
```
1. Open admin terminal/tool
2. Run: curl -X POST http://localhost:5000/api/notify-order-status/1/completed
3. Check chat in customer account
4. See green notification message
```

---

## 🎨 New UI Features

### Chat Interface:
- **Left sidebar**: (Prepared for future - conversations list)
- **Main chat**: Messages with timestamps
- **Header**: Admin status indicator
- **Input**: Rounded message input box

### Profile Page:
- **Avatar**: Click to upload picture
- **Hover effect**: Shows camera icon hint
- **Success message**: Appears when upload completes
- **Image display**: Shows uploaded picture immediately

---

## 📱 API Reference

### Get all messages:
```
GET /api/messages
```

### Send message:
```
POST /api/send-message
{
  "message": "Hello!",
  "message_type": "text"
}
```

### Get unread count:
```
GET /api/unread-count
```

### Get user info:
```
GET /api/user-info
```

### Upload profile picture:
```
POST /upload-profile-pic
[multipart form data with profile_pic file]
```

### Send order notification:
```
POST /api/notify-order-status/<order_id>/<status>
```

---

## ⚙️ Configuration

### Change message refresh rate:
In `Chat.html`, find:
```javascript
setInterval(loadMessages, 2000); // 2 seconds
```
Change `2000` to desired milliseconds.

### Change file upload limit:
In `user_routes.py`, find:
```python
if file.size > 5 * 1024 * 1024:  # 5MB
```
Change `5` to desired size in MB.

### Change allowed image types:
In `user_routes.py`, find:
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
```
Add or remove extensions as needed.

---

## 🐛 Troubleshooting

### Profile picture not uploading?
- Check file size (max 5MB)
- Check file type (PNG, JPG, GIF only)
- Check if `app/static/uploads/profile_pics/` folder exists
- Check browser console for errors

### Messages not showing?
- Refresh the page
- Check if user is logged in
- Check if conversation_id matches user ID

### Chat not auto-refreshing?
- Check if JavaScript is enabled
- Check browser console for errors
- Check if server is running

### Order notification not sent?
- Check if order exists
- Check if customer username is correct
- Check API endpoint syntax

---

## 📞 Support Features Added

The new messaging system includes:
- Real-time chat with support team
- Order status tracking via messages
- Profile customization with pictures
- Message history preservation
- Auto-scroll to latest messages
- Relative time formatting

---

## 🎯 Next Steps

1. Test all features with test data
2. Customize message templates in `notify_order_status()`
3. Add admin endpoints for sending notifications
4. Deploy to production
5. Monitor message database growth

---

**Last Updated:** January 31, 2026
**Version:** 2.0
