# Buy Now Feature - Visual Guide & Flow Diagram

## 🎯 User Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   CUSTOMER JOURNEY                              │
└─────────────────────────────────────────────────────────────────┘

1. MENU PAGE (GET /menu)
   ├─ View all products
   ├─ See prices and variants
   └─ Click [Buy Now] or [Add to Cart]
      │
      ├─→ Add to Cart: Goes to cart (localhost:5000/cart)
      │
      └─→ Buy Now: ↓↓↓

2. LOGIN CHECK
   ├─ If logged in: Proceed
   └─ If not logged in: Redirect to /login

3. SIZE/VARIANT MODAL (on Menu.html)
   ├─ Product name displayed
   ├─ Select size from radio buttons
   │  └─ Regular - ₱250.00
   │  └─ Large - ₱350.00
   ├─ Select quantity (spinbox)
   ├─ Show total price
   └─ Click [Proceed to Checkout] ↓↓↓

4. CHECKOUT PAGE (GET /checkout)
   ├─ Product summary shows in right panel
   ├─ Left panel: Billing Information form
   │  ├─ Full Name (required)
   │  ├─ Email Address (required)
   │  ├─ Contact Number (required)
   │  ├─ Delivery Address (required)
   │  └─ Payment Method (required)
   │     ├─ Cash on Delivery (COD)
   │     ├─ Online Transfer
   │     └─ Credit Card
   └─ Click [Complete Order] ↓↓↓

5. PROCESS ORDER (POST /checkout)
   ├─ Validate all fields filled
   ├─ Create Order record(s) in database
   ├─ CREATE NOTIFICATION for Admin ⭐
   │  └─ Notification includes:
   │     ├─ Customer name
   │     ├─ All items ordered
   │     ├─ Quantities
   │     ├─ Total amount
   │     ├─ Contact number
   │     ├─ Delivery address
   │     └─ Payment method
   └─ Redirect to /order-success ↓↓↓

6. ORDER SUCCESS PAGE
   ├─ Show order confirmation
   ├─ Display order details
   └─ Option to continue shopping


┌─────────────────────────────────────────────────────────────────┐
│                    ADMIN DASHBOARD                              │
└─────────────────────────────────────────────────────────────────┘

1. ADMIN RECEIVES NOTIFICATION (Real-time)
   ├─ Notification bell (🔔) shows unread count badge
   ├─ Auto-refreshes every 5 seconds
   └─ Click bell to open dropdown

2. NOTIFICATION DROPDOWN
   ├─ Shows:
   │  ├─ 📦 New Order from [Customer Name]
   │  ├─ Full order details
   │  ├─ Timestamp
   │  └─ [Click to view in Orders page]
   │
   └─ Different colors for:
      ├─ 🟢 Green: Orders
      └─ 🔵 Blue: Messages

3. ADMIN ACTIONS
   ├─ Click notification → Go to Orders page
   ├─ View order details
   ├─ Update order status (Pending → Completed/Cancelled)
   └─ Respond to customer if needed
```

---

## 📲 Screen Layouts

### BEFORE: Menu Page
```
┌──────────────────────────────────────┐
│  🍵 CiTea Coolers  [Home] [Menu] ... │ ← Navigation
├──────────────────────────────────────┤
│                                      │
│  ☕ Full Menu                         │
│  [All Categories] [Tea] [Coffee] ... │ ← Filters
│                                      │
│  ┌──────────┐  ┌──────────┐          │
│  │  🍵      │  │  ☕      │          │
│  │ Oolong   │  │ Espresso │   ...    │
│  │ ₱250.00  │  │ ₱300.00  │          │
│  │ [BUY NOW]│  │ [BUY NOW]│          │ ← NEW!
│  │ [ADD CAR]│  │ [ADD CAR]│          │
│  └──────────┘  └──────────┘          │
│                                      │
└──────────────────────────────────────┘
```

### Variant Selection Modal (NEW!)
```
┌────────────────────────────────────┐
│           Oolong Tea               │
├────────────────────────────────────┤
│                                    │
│ ○ Regular - ₱250.00               │
│ ● Large - ₱350.00                 │ (selected)
│                                    │
│ Quantity: [2]  ↑↓                  │
│                                    │
│ Total: ₱700.00                     │
│                                    │
│          [Cancel] [Proceed]        │
│                                    │
└────────────────────────────────────┘
```

### Checkout Page
```
┌────────────────────────────────────────────────────┐
│  💳 Checkout                                       │
├────────────┬─────────────────────────────────────┤
│ 📋 Billing │ 📦 Order Summary                    │
│ Information│                                      │
├────────────┤ Oolong Tea (Large) x2               │
│            │ ₱700.00                             │
│ Full Name* │                                      │
│ [________] │ Total Amount: ₱700.00               │
│            │                                      │
│ Email*     │ 💳 Payment Method *                 │
│ [________] │ [Select payment method]             │
│            │ - Cash on Delivery (COD)            │
│ Contact*   │ - Online Transfer                   │
│ [________] │ - Credit Card                       │
│            │                                      │
│ Address*   │ [Complete Order]                    │
│ [________] │ [Back to Cart]                      │
│ [________] │                                      │
│            │                                      │
└────────────┴─────────────────────────────────────┘
```

### Order Success Page
```
┌──────────────────────────────────────┐
│  ✅ Order Success!                   │
├──────────────────────────────────────┤
│                                      │
│  Your order has been confirmed       │
│                                      │
│  Order ID: #12345                    │
│  Customer: John Doe                  │
│  Items: 2                            │
│  Total: ₱700.00                      │
│  Status: Pending                     │
│                                      │
│  Thank you for your order!           │
│                                      │
│  [Continue Shopping] [View Orders]   │
│                                      │
└──────────────────────────────────────┘
```

### Admin Notification Bell
```
┌──────────────────────────────┐
│  Dashboard  Orders  Messages  │ ← Top Navigation
│                              │
│         🔔 3  ← NEW COUNT    │ (top-right corner)
│                              │
└──────────────────────────────┘

Dropdown when clicked (350px wide):
┌──────────────────────────────┐
│ 🔔 Notifications             │
├──────────────────────────────┤
│ 📦 New Order from John Doe   │ ← Green border
│ Order: 2 Oolong Tea          │
│ Total: ₱700.00               │
│ 10:30 AM                     │
│                              │
│ 📦 New Order from Jane Smith │
│ Order: 1 Espresso            │
│ Total: ₱300.00               │
│ 10:28 AM                     │
│                              │
│ 💬 New Message from John     │ ← Blue border
│ From John: Please check... │
│ 10:20 AM                     │
├──────────────────────────────┤
```

---

## 🔄 Data Flow Diagram

```
CUSTOMER SIDE:
┌──────────────┐
│ Menu Page    │
│ (Products)   │
└────────┬─────┘
         │ Click "Buy Now"
         ↓
   ┌──────────────────┐
   │ Check if logged  │
   │ in (session)     │
   └────┬────────┬────┘
        │ NO     │ YES
        │        │
        ↓        ↓
    [Login]  ┌──────────────────┐
            │ Size Modal Opens  │
            │ (Menu.html JS)    │
            └────────┬──────────┘
                     │ Select size/qty
                     ↓
              ┌──────────────────────┐
              │ Save to localStorage │
              │ (cart object)        │
              └────────┬─────────────┘
                       │ Redirect
                       ↓
              ┌──────────────────────┐
              │ Checkout Page        │
              │ (/checkout GET)      │
              │ - Loads from storage │
              └────────┬─────────────┘
                       │ Fill form + submit
                       ↓
              ┌──────────────────────┐
              │ POST /checkout       │
              │ Validate fields      │
              └────────┬─────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ↓              ↓              ↓
     ERROR      CREATE ORDER    [ADMIN NOTIFICATION]  ← KEY PART
   [Show msg]   in DB              Created here! ⭐
                                    │
                                    ↓
                              ┌───────────────────┐
                              │ Notification      │
                              │ Model saved in    │
                              │ Database          │
                              └───────────────────┘


ADMIN SIDE:
┌───────────────────────┐
│ Admin Dashboard       │
│ (Auto-checks every 5s)│
└──────────┬────────────┘
           │ fetch /admin/api/notifications
           ↓
    ┌──────────────────┐
    │ Notification API │
    │ Returns list of: │
    │ - Orders (from   │
    │   Notification   │
    │   model)         │
    │ - Messages       │
    └──────────┬───────┘
               │
               ↓
        ┌─────────────────┐
        │ Update UI:      │
        │ - Bell badge    │
        │ - Dropdown list │
        └─────────────────┘
```

---

## 📊 Database Table Relationships

```
CUSTOMERS          ORDERS              NOTIFICATIONS
┌────────┐        ┌────────┐          ┌──────────┐
│ id     │───┐    │ id     │──┐       │ id       │
│ username│  │    │ customer_│ └──────│ order_id │
│ email  │  │    │ name   │           │ title    │
└────────┘  │    │ product│           │ message  │
            │    │ _name  │           │ type     │
            │    │ qty    │           │ is_read  │
            │    │ price  │           │ created_ │
            │    │ status │           │ at       │
            │    │ order_ │           └──────────┘
            │    │ date   │
            └────│ (no fk)│
                 └────────┘

When order is created:
Order → Notification (1-to-1 optional)
(Each order can have a notification)
```

---

## 🎨 Color Legend

| Color | Usage | Code |
|-------|-------|------|
| 🟤 Brown | Primary | #5D2906 |
| 🟠 Orange | Secondary | #D35400 |
| 🟡 Gold | Accent | #FFD700 |
| 🟢 Green | Buy Now | #28a745 |
| 🟢 Green | Order Notif | #4CAF50 |
| 🔵 Blue | Message Notif | #2196F3 |
| 🔴 Red | Badge | #ff4444 |

---

## 🚀 Quick Start Testing

### Test Buy Now:
```
1. http://localhost:5000/menu
2. Click "Buy Now" on any product
3. Select size and quantity
4. Click "Proceed to Checkout"
5. Fill form (name, email, phone, address, payment)
6. Click "Complete Order"
7. Should see "Order Success" page
```

### Test Admin Notification:
```
1. Open http://localhost:5000/admin/dashboard in new tab
2. Complete a "Buy Now" order (steps above)
3. Notification bell should show "1" badge
4. Click bell to see dropdown
5. Should see "New Order from [Customer Name]"
6. Click to go to Orders page
```

---

## 📝 Notification Message Format

When admin clicks on a new order notification, they see:

```
📦 New Order Received!

Customer: John Doe
Contact: 09123456789
Delivery Address: House 1, Maple St, City

Items Ordered:
- Oolong Tea (Large) x2 = ₱700.00
- Espresso x1 = ₱300.00

Total Amount: ₱1,000.00

Items: 3
```

---

**Created:** February 2, 2026  
**Status:** ✅ Production Ready
