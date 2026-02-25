# 🍵 CiTea Coolers - Messaging & Profile Updates

## ✨ New Features Implemented

### 1. **Improved Messaging System (Facebook Messenger-like Interface)**

#### What's New:
- ✅ **Modern Chat UI** - Clean, intuitive interface similar to Facebook Messenger
- ✅ **Real-time Message Updates** - Auto-refreshes every 2 seconds
- ✅ **Message Timestamps** - Relative time display (e.g., "5m ago", "2h ago")
- ✅ **Message Type Support** - Different styling for regular messages and order notifications
- ✅ **Order Notifications** - Special green notification bubbles for order status updates
- ✅ **Admin Indicator** - Shows which messages are from the admin
- ✅ **Rounded Message Bubbles** - Modern design with proper message attribution
- ✅ **Auto-scroll** - Automatically scrolls to latest message
- ✅ **Read Status** - Tracks which messages have been read

#### Key Features:
```
Message Types:
- Regular text messages
- Order status notifications (green background)
- Completion alerts

Display Features:
- Admin responses show "ADMIN" badge
- Timestamps in human-readable format
- Auto-scroll to bottom
- Empty state with friendly message
```

---

### 2. **Profile Picture Upload**

#### What's New:
- ✅ **Click-to-Upload Avatar** - Click profile picture to upload
- ✅ **Image Preview** - Displays uploaded profile picture
- ✅ **File Validation** - Only PNG, JPG, GIF files allowed
- ✅ **Size Limit** - Maximum 5MB file size
- ✅ **Success/Error Messages** - Real-time feedback on upload status
- ✅ **Profile Picture Display** - Shows on chat messages and profile
- ✅ **Persistent Storage** - Profile picture saved to `/static/uploads/profile_pics/`

#### How to Use:
1. Go to **Profile** page
2. Click on the avatar (profile picture circle)
3. Select an image file (PNG, JPG, or GIF)
4. See the success message appear
5. Picture updates instantly

#### Accepted Formats:
- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- Maximum size: 5MB

---

### 3. **Order Status Notifications**

#### What's New:
- ✅ **Automatic Order Notifications** - Customers receive messages when orders are updated
- ✅ **Status Types** - Confirmed, Shipped, Completed, Cancelled
- ✅ **Special Styling** - Order notifications in green with special formatting
- ✅ **Real-time Delivery** - Customers see notifications immediately in chat

#### Order Status Messages:
```
✔️ Order Confirmed: "Your order has been confirmed and is being prepared."
🚚 Order Shipped: "Your order has been shipped! It will arrive soon."
✅ Order Completed: "Your order has been completed! It's ready for delivery."
❌ Order Cancelled: "Your order has been cancelled."
```

#### Admin Usage:
To send an order notification to a customer, use:
```
POST /api/notify-order-status/<order_id>/<status>
```

Example:
```
POST /api/notify-order-status/1/completed
POST /api/notify-order-status/2/shipped
```

---

### 4. **Enhanced Database Models**

#### User Model Updates:
```python
- profile_pic (NEW) - File path to profile picture
- created_at (NEW) - Account creation timestamp
```

#### Message Model Updates:
```python
- recipient_id (NEW) - Track who message is sent to
- message_type (NEW) - Type of message (text, order_notification, etc.)
```

---

## 📱 API Endpoints

### Messaging Endpoints:

#### Send Message
```
POST /api/send-message
{
    "message": "Your message text",
    "message_type": "text" (or "order_notification")
}
Response: {
    "success": true,
    "message_id": 1,
    "conversation_id": "user_1"
}
```

#### Get Messages
```
GET /api/messages
Response: [
    {
        "id": 1,
        "content": "Message text",
        "sender_name": "Username",
        "sender_type": "customer" or "admin",
        "sender_profile_pic": "/static/uploads/profile_pics/...",
        "created_at": "2026-01-31T10:30:00",
        "is_read": true,
        "message_type": "text"
    }
]
```

#### Get Unread Count
```
GET /api/unread-count
Response: {
    "unread_count": 3
}
```

### Profile Endpoints:

#### Get User Info
```
GET /api/user-info
Response: {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "profile_pic": "/static/uploads/profile_pics/user_1_1234567.jpg"
}
```

#### Upload Profile Picture
```
POST /upload-profile-pic
Content-Type: multipart/form-data
Body: {
    "profile_pic": <file>
}
Response: {
    "success": true,
    "profile_pic": "/static/uploads/profile_pics/user_1_1234567.jpg"
}
```

### Order Notification Endpoints:

#### Send Order Status Notification
```
POST /api/notify-order-status/<order_id>/<status>
Response: {
    "success": true,
    "message": "✅ Your order has been completed!..."
}
```

Status options: `confirmed`, `shipped`, `completed`, `cancelled`

---

## 🎨 Styling & Design

### Message Bubble Colors:
- **Customer messages**: Orange (#D35400) background, white text
- **Admin messages**: Light gray (#e5e5ea) background, black text
- **Order notifications**: Green (#c8e6c9) background, dark green text

### Chat Interface:
- Clean, minimal design
- Rounded message bubbles (radius: 18px)
- Smooth animations for new messages
- Admin status indicator
- Profile avatars in header

---

## 🔧 Technical Details

### File Upload Configuration:
- **Upload Directory**: `app/static/uploads/profile_pics/`
- **Filename Format**: `user_{user_id}_{timestamp}.{extension}`
- **Auto-created**: Directory created automatically if not exists

### Database Migrations Needed:
If updating existing database, run:
```python
from app import app, db
with app.app_context():
    db.create_all()
```

This will add new columns to existing tables.

### JavaScript Features:
- Auto-refresh messages every 2 seconds
- Smart time formatting (Just now, 5m ago, 2h ago, etc.)
- HTML escaping for security
- Image upload validation
- Responsive design

---

## ✅ Testing Checklist

- [ ] Upload profile picture - should display on profile
- [ ] Send message in chat - should appear with correct styling
- [ ] Receive admin message - should show admin badge
- [ ] Order notification arrives - should show green styling
- [ ] Auto-refresh - messages update every 2 seconds
- [ ] Profile picture displays in chat - if available
- [ ] File size validation - rejects files > 5MB
- [ ] File type validation - rejects non-image files
- [ ] Mobile responsive - works on small screens
- [ ] Unread count - shows pending messages

---

## 🚀 How to Test

### Test Profile Picture Upload:
1. Navigate to `/profile`
2. Click on the avatar
3. Select an image file
4. See success message
5. Refresh page - picture persists

### Test Messaging:
1. Go to `/chat`
2. Send a message
3. Message appears on right (orange bubble)
4. Auto-refreshes show any admin responses

### Test Order Notifications:
1. As admin, send: `POST /api/notify-order-status/1/completed`
2. Customer should see green notification in chat
3. Message includes order ID

---

## 📝 Code Example: Admin Sending Order Notification

```python
# In admin routes (you can add this)
from datetime import datetime
from app.models import db, Message, Order, User

@admin_route.route("/api/notify-customer/<int:order_id>", methods=["POST"])
def notify_customer(order_id):
    order = Order.query.get(order_id)
    user = User.query.filter_by(username=order.customer_name).first()
    
    if order and user:
        message = Message(
            conversation_id=f"user_{user.id}",
            sender_name="CiTea Support",
            sender_type="admin",
            content=f"✅ Order #{order.id} completed!",
            message_type="order_notification",
            created_at=datetime.now(),
            is_read=False
        )
        db.session.add(message)
        db.session.commit()
        return {"success": True}
```

---

## 🎯 Future Enhancement Ideas

1. **Typing Indicators** - Show when admin is typing
2. **Message Search** - Search past conversations
3. **Attachment Support** - Send images in messages
4. **Message Reactions** - Like, love, etc. reactions
5. **Voice Messages** - Send audio messages
6. **Video Chat** - Direct video support
7. **Chatbot Integration** - AI responses for common questions
8. **Message Groups** - Group conversations
9. **Auto-replies** - Set status messages when offline
10. **Archive Chats** - Hide old conversations

---

## ⚠️ Important Notes

- Profile pictures are stored in `app/static/uploads/profile_pics/`
- Old profile pictures are automatically deleted when new one is uploaded
- Messages are stored in database with full chat history
- Auto-refresh happens every 2 seconds (customizable in JavaScript)
- File size limit is 5MB (customizable in `upload_profile_pic()`)

---

**Updated**: January 31, 2026
**Version**: 2.0
**Status**: ✅ Ready for Production
