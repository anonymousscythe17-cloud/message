# 🚀 Quick Start - Testing Buy Now Feature

## ⚡ 5-Minute Setup & Test

### Step 1: Database Setup (1 min)
```bash
# Delete old database (if exists)
del instance\site.db

# Run application to create new database
python run.py
```

The application will create all tables including the new `Notification` table.

---

### Step 2: Create Test Data (1 min)

**Option A: Automatic**
- Register a new customer account at `http://localhost:5000/register`
- Login with the new account

**Option B: Manual (using admin or existing account)**
- Use any existing customer account or create one via registration

---

### Step 3: Test Buy Now (3 min)

#### Open Menu Page:
```
http://localhost:5000/menu
```

#### Click "Buy Now" on Any Product:
You should see:
- ✅ Size/Variant selection modal appears
- ✅ Radio buttons for different sizes
- ✅ Quantity selector
- ✅ Price displays total
- ✅ Button says "Proceed to Checkout"

#### Fill Out Checkout Form:
```
Full Name:        John Doe
Email:            john@example.com
Contact Number:   09123456789
Delivery Address: 123 Main Street, City
Payment Method:   Cash on Delivery
```

#### Click "Complete Order":
You should see:
- ✅ Redirect to `/order-success` page
- ✅ Order confirmation displayed
- ✅ Order created in database

---

### Step 4: Test Admin Notification (1 min)

#### In Same Browser:
```
http://localhost:5000/admin/dashboard
```

#### Check Notification Bell:
- ✅ Top-right corner shows bell (🔔)
- ✅ Red badge shows "1" (one unread notification)

#### Click Notification Bell:
You should see:
- ✅ Dropdown panel opens
- ✅ Shows "New Order from John Doe"
- ✅ Display full order details:
  - Items ordered
  - Quantities
  - Total amount
  - Customer contact info
  - Delivery address
  - Payment method

#### Click on Notification:
- ✅ Navigates to `/admin/order`
- ✅ Your order is visible in the list with status "Pending"

---

## 🎯 Expected Results

### Customer Side:
| Action | Expected Result |
|--------|-----------------|
| Click "Buy Now" | Variant modal appears |
| Select Size | Price updates correctly |
| Change Quantity | Total price updates |
| Click "Proceed" | Redirects to checkout |
| Fill Form | All fields validate |
| Click "Complete Order" | Success page shown |

### Admin Side:
| Action | Expected Result |
|--------|-----------------|
| Visit Dashboard | Notification bell visible |
| New Order Created | Badge count increases |
| Click Bell | Dropdown shows order |
| Click Notification | Goes to Orders page |
| Order Visible | Shows as "Pending" status |

---

## ✅ Verification Checklist

- [ ] Database created successfully (instance/site.db exists)
- [ ] Menu page loads without errors
- [ ] "Buy Now" button visible on products (green button)
- [ ] Clicking "Buy Now" requires login (redirects if not logged in)
- [ ] Variant modal displays correctly with sizes
- [ ] Checkout page loads with cart items
- [ ] All form fields are required
- [ ] "Complete Order" creates order in database
- [ ] Order Success page displays
- [ ] Admin notification bell appears
- [ ] Notification count badge shows correct number
- [ ] Notification dropdown shows full order details
- [ ] Clicking notification goes to Orders page
- [ ] Order appears in admin Orders list

---

## 🔧 Common Issues & Fixes

### Issue: "ModuleNotFoundError: No module named 'Notification'"
**Fix:** Delete `instance/site.db` and rerun `python run.py`

### Issue: Notification bell doesn't show
**Fix:** 
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
- Check browser console for errors (F12)
- Verify `/admin/api/notifications` endpoint works

### Issue: "Buy Now" button missing
**Fix:** Menu page may not be loading correctly - check browser console

### Issue: Can't proceed to checkout
**Fix:** Make sure you're logged in - Buy Now requires authentication

### Issue: Form validation shows error
**Fix:** Ensure all fields are filled:
- Full Name (text)
- Email (valid email format)
- Contact Number (phone number)
- Delivery Address (text)
- Payment Method (dropdown selection)

---

## 📱 What Each Page Shows

### Menu Page (`/menu`)
```
Products displayed with:
- Product image
- Product name
- Price(s) with variants
- [Buy Now] button (green) ← NEW!
- [Add to Cart] button (orange)
```

### Variant Modal (when "Buy Now" clicked)
```
Product Name
- [ ] Regular - ₱250.00
- [✓] Large - ₱350.00 (selected)

Quantity: [2] ↑↓

Total: ₱700.00

[Cancel] [Proceed to Checkout]
```

### Checkout Page (`/checkout`)
```
LEFT COLUMN                RIGHT COLUMN
Full Name                  Order Summary
[________________]         Oolong (Large) x2
                          ₱700.00
Email                     
[________________]         Payment Method *
                          [Cash on Delivery]
Contact
[________________]         [Complete Order]
                          [Back to Cart]
Address
[________________]
```

### Order Success Page (`/order-success`)
```
✅ Order Successful!

Order ID: #12345
Customer: John Doe
Total: ₱700.00
Status: Pending

[Continue Shopping] [View Profile]
```

### Admin Dashboard - Notifications
```
🔔 1 ← Badge with count
   ↓
   ┌─────────────────────────────────┐
   │ Notifications                   │
   ├─────────────────────────────────┤
   │ 📦 New Order from John Doe      │
   │ Items: 2, Total: ₱700.00        │
   │ 10:30 AM                        │
   ├─────────────────────────────────┤
   │ [Click to view orders]          │
   └─────────────────────────────────┘
```

---

## 🔍 Database Verification

After creating an order, verify in database:

### Check Orders Table:
```sql
SELECT * FROM "order" WHERE customer_name = 'John Doe';
```
Should show:
- Order ID
- Customer name
- Product name with size
- Quantity
- Total price
- Status: "Pending"
- Order date/time

### Check Notifications Table:
```sql
SELECT * FROM notification WHERE type = 'new_order';
```
Should show:
- Notification ID
- Type: "new_order"
- Title: "New Order from John Doe"
- Complete order message
- Customer name
- Order ID (linked)
- is_read: False
- Created timestamp

---

## 🎓 Technical Details

### API Endpoint Test:
Open in browser or curl:
```
http://localhost:5000/admin/api/notifications
```

Returns JSON like:
```json
[
  {
    "id": 1,
    "type": "order",
    "title": "New Order from John Doe",
    "message": "Complete order details...",
    "customer_name": "John Doe",
    "created_at": "2026-02-02T10:30:00",
    "link": "/admin/order",
    "is_read": false
  }
]
```

### Form Data POST:
When "Complete Order" is clicked, sends:
```
fullName: "John Doe"
email: "john@example.com"
contactNumber: "09123456789"
deliveryAddress: "123 Main St, City"
paymentMethod: "Cash on Delivery"
cart_data: '[{"id":1,"name":"Oolong","size":"Large","price":350,"quantity":2}]'
```

---

## 📊 Success Metrics

After testing, you should be able to verify:

✅ **User Flow Working:**
- Menu → Buy Now → Modal → Checkout → Success

✅ **Data Persistence:**
- Order saved in database
- Notification saved in database
- All details preserved

✅ **Admin Alerts:**
- Notification appears immediately
- All order details visible
- One-click navigation works

✅ **No Errors:**
- No console errors (F12)
- No server errors (terminal output)
- All redirects work correctly

---

## 🎉 You're Done!

Once all verification items are checked, the Buy Now feature is fully operational:

1. ✅ Customers can buy directly from menu
2. ✅ Orders are created with full details
3. ✅ Admins get real-time notifications
4. ✅ All information is preserved in database

**Congratulations! The feature is ready for production.** 🚀

---

**Last Updated:** February 2, 2026
