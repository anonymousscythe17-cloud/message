# 🧪 CiTea Coolers - Homepage Testing Guide

## ✅ Test Checklist

Complete the tests below to ensure everything works correctly.

---

## 🚀 Pre-Testing Setup

### **Step 1: Start the Application**
```bash
cd c:\Users\Administrator\Documents\Citea_jm
python run.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### **Step 2: Open Browser**
```
http://localhost:5000/
```

---

## 📋 Test Cases

### **TEST 1: Guest User View (Not Logged In)**

**What to do:**
1. Make sure you're NOT logged in (logout if needed)
2. Visit http://localhost:5000/

**Expected Result:**
- ✅ See the Landing page (old design)
- ✅ See "Login" button in navigation
- ✅ See "Register" button in navigation
- ✅ Can click "Shop Now" → redirects to login page

**If this fails:**
- Clear browser cache (Ctrl+Shift+Del)
- Check browser console (F12) for errors
- Verify session is cleared

---

### **TEST 2: Logged-In User View**

**What to do:**
1. Login to your account
2. Visit http://localhost:5000/

**Expected Result:**
- ✅ See the NEW Home page (modern design)
- ✅ See orange header with location
- ✅ See search bar
- ✅ See hero banner with "Shop Now"
- ✅ See categories section
- ✅ See featured products (4 products)
- ✅ See bottom navigation with cart FAB

**If this fails:**
- Verify you're logged in (check session)
- Clear browser cache
- Check console for JavaScript errors

---

### **TEST 3: Header & Navigation**

**What to do:**
1. Look at the top of the page
2. Check mobile view (< 768px width)

**Expected Result:**
- ✅ See "🍵 CiTea Coolers" logo
- ✅ See location: "📍 Matnog, Sorsogon"
- ✅ See profile icon (👤) on right
- ✅ See search bar with placeholder
- ✅ Search bar is functional (input works)

**Desktop Test:**
- ✅ See top navigation bar instead
- ✅ Navigation links visible: 🏠 📜 👤 💬
- ✅ Cart icon with badge visible

---

### **TEST 4: Hero Banner**

**What to do:**
1. Look at hero banner section
2. Click "Shop Now" button

**Expected Result:**
- ✅ Banner has gradient background with image
- ✅ Title: "🍵 Premium Drinks"
- ✅ Description text visible
- ✅ "Shop Now" button visible
- ✅ Clicking button → goes to /menu

**If banner looks broken:**
- Check if background image loads
- Verify CSS is applied
- Check console for 404 errors

---

### **TEST 5: Categories Section**

**What to do:**
1. Look for "📂 Categories" section
2. Count category buttons
3. Click on different categories

**Expected Result:**
- ✅ Section title visible: "📂 Categories"
- ✅ "See All" link on right
- ✅ Multiple category buttons displayed
- ✅ Clicking category → filters in /menu
- ✅ Category icons visible (if Font Awesome loaded)

**If categories not showing:**
- Verify categories exist in database
- Check if Categories model has data
- Look for SQL errors in console

---

### **TEST 6: Featured Products Display**

**What to do:**
1. Look for "⭐ Featured Products" section
2. Count products shown
3. Check product information

**Expected Result:**
- ✅ Section title visible
- ✅ Exactly 4 products displayed (first 4 from DB)
- ✅ Product images visible (or placeholder emoji)
- ✅ Product names visible
- ✅ Prices visible
- ✅ [+] buttons visible on each product
- ✅ Responsive grid (2 columns on mobile, 3 on tablet)

**If products not showing:**
```python
# Check database has products:
# In Python shell:
from app.models import Product
print(Product.query.all())  # Should show products
```

---

### **TEST 7: Add to Cart - Size Modal**

**What to do:**
1. Click the [+] button on any product

**Expected Result:**
- ✅ Modal appears (centered, semi-transparent background)
- ✅ Modal shows product name as title
- ✅ Size options displayed as radio buttons
- ✅ Each size shows price
- ✅ Quantity input visible
- ✅ Total price calculated and shown
- ✅ "Cancel" and "Add to Cart" buttons visible

**If modal doesn't appear:**
- Check browser console for errors
- Verify Font Awesome CDN loads
- Check CSS for modal styles

---

### **TEST 8: Size Selection & Quantity**

**What to do:**
1. Open size modal (click [+])
2. Try different size options
3. Change quantity

**Expected Result:**
- ✅ Clicking radio button selects size
- ✅ Price updates when size changes
- ✅ Quantity spinner works (up/down)
- ✅ Total price updates: price × quantity
- ✅ Price format is correct (₱XXX.XX)

**Example:**
```
Size: Medium (₱100)
Quantity: 3
Total should be: ₱300.00
```

---

### **TEST 9: Add to Cart Button**

**What to do:**
1. Open modal
2. Select a size
3. Choose quantity (e.g., 2)
4. Click "Add to Cart"

**Expected Result:**
- ✅ Modal closes automatically
- ✅ Alert appears: "Matcha Latte (Large) added to cart!"
- ✅ Cart badge updates with new count
- ✅ Data saved to localStorage (check DevTools)

**Check localStorage:**
1. Press F12 (DevTools)
2. Go to "Application" tab
3. Click "Local Storage"
4. Look for "cart" key
5. Should see JSON array with cart items

---

### **TEST 10: Cart Badge Updates**

**What to do:**
1. Add product to cart (e.g., quantity 2)
2. Check badge numbers

**Expected Result:**
- ✅ Bottom nav cart badge shows "2"
- ✅ Desktop cart icon badge shows "2"
- ✅ Add another product → badge increases
- ✅ Badges stay in sync

**Test multiple additions:**
```
Add 1 item (qty=2) → Badge: 2
Add 1 item (qty=3) → Badge: 5 (2+3)
Add 1 item (qty=1) → Badge: 6 (2+3+1)
```

---

### **TEST 11: Cart Navigation**

**What to do:**
1. Add something to cart
2. Click cart FAB (floating cart button)

**Expected Result:**
- ✅ Cart FAB is orange and floating
- ✅ Cart badge visible on FAB
- ✅ Clicking FAB → navigates to /cart
- ✅ Shopping cart page loads

---

### **TEST 12: Bottom Navigation**

**What to do:**
1. Check bottom of screen on mobile
2. Click different navigation items

**Expected Result:**
- ✅ Bottom nav is fixed (doesn't scroll)
- ✅ 5 icons visible: 🏠 📜 🛒 💬 👤
- ✅ Cart FAB is highlighted/orange
- ✅ Home icon is active (highlighted)
- ✅ Clicking each navigates correctly:
  - 🏠 → Home (current page)
  - 📜 → Menu (/menu)
  - 🛒 → Cart (/cart)
  - 💬 → Chat (/chat)
  - 👤 → Profile (/profile)

---

### **TEST 13: Responsive Design - Mobile**

**What to do:**
1. Open DevTools (F12)
2. Click "Toggle device toolbar" (mobile icon)
3. Select "iPhone 12" or similar

**Expected Result:**
- ✅ Layout responsive (not stretched)
- ✅ Header visible and functional
- ✅ Hero banner visible
- ✅ Products in 2-column grid
- ✅ Categories in 4-column grid
- ✅ Bottom navigation fixed
- ✅ Text readable (not too small)
- ✅ Buttons clickable (44x44px minimum)
- ✅ No horizontal scrollbar

---

### **TEST 14: Responsive Design - Tablet**

**What to do:**
1. Select "iPad" or similar in device toolbar
2. Check layout

**Expected Result:**
- ✅ Product grid shows 3 columns (not 2)
- ✅ Everything else scales appropriately
- ✅ Still responsive

---

### **TEST 15: Responsive Design - Desktop**

**What to do:**
1. Resize browser to > 1024px wide
2. Check layout

**Expected Result:**
- ✅ Bottom navigation HIDDEN
- ✅ Desktop top navigation VISIBLE
- ✅ Traditional layout shown
- ✅ Product grid appropriate width

---

### **TEST 16: Search Bar**

**What to do:**
1. Type in search bar
2. Press Enter or type

**Expected Result:**
- ✅ Search bar accepts input
- ✅ Placeholder text visible
- ✅ Input is cleared when needed

**Note:** Search filtering not yet implemented (can be added)

---

### **TEST 17: Menu Navigation**

**What to do:**
1. Click "See All" links (Categories or Products)
2. Click "📜" in bottom nav

**Expected Result:**
- ✅ Both navigate to /menu
- ✅ Full menu page loads with all products
- ✅ Categories filters visible

---

### **TEST 18: Multiple Add to Cart**

**What to do:**
1. Add product A (quantity 2)
2. Add product B (quantity 1)
3. Add product A again (different size)

**Expected Result:**
- ✅ All items in cart
- ✅ Badge shows total: 4 (or correct count)
- ✅ Check localStorage shows all items
- ✅ Going to cart shows all items

---

### **TEST 19: Server Sync (Logged-In)**

**What to do:**
1. Add item to cart
2. Refresh page (F5)

**Expected Result:**
- ✅ Cart items persist (from localStorage)
- ✅ Badge updates correctly
- ✅ No 404 or error in console

**Note:** If you have `/api/cart` endpoint, it should sync

---

### **TEST 20: Browser Compatibility**

**Test in multiple browsers:**
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Edge

**Expected Result:**
- ✅ Works same in all browsers
- ✅ No console errors
- ✅ Styling consistent

---

## 🐛 Debugging Common Issues

### **Products Not Showing**
```python
# Check in Flask shell:
python
from app.models import Product
Product.query.all()  # Should return products
```

If empty:
- Add products via admin panel first
- Or check database connection

### **Categories Not Showing**
```python
# Check in Flask shell:
from app.models import Categories
Categories.query.all()  # Should return categories
```

### **Modal Won't Open**
- Check browser console (F12) for JavaScript errors
- Verify Font Awesome CDN loads (check Network tab)
- Try hard refresh (Ctrl+Shift+R)

### **Cart Badge Not Updating**
- Open DevTools → Application → LocalStorage
- Check if cart key exists
- Verify JSON format is correct

### **Responsive Issues**
- Check viewport meta tag in HTML <head>
- Clear browser cache
- Try different browser
- Check if custom CSS overrides

---

## 📊 Performance Testing

### **Page Load Time**
```
Target: < 2 seconds
Method:
1. Open DevTools
2. Go to Network tab
3. Reload page
4. Check "Finish" time
```

### **Lighthouse Score**
```
Target: 90+
Method:
1. Open DevTools
2. Go to Lighthouse tab
3. Click "Generate report"
4. Check score
```

---

## ✨ Final Verification

After all tests, verify:

- [ ] Home page shows for logged-in users
- [ ] Landing page shows for guests
- [ ] Add to cart works
- [ ] Cart syncs correctly
- [ ] Navigation works
- [ ] Responsive on all devices
- [ ] No console errors
- [ ] No database errors
- [ ] Colors match brand
- [ ] All images load

---

## 📝 Test Report Template

```
Date: ________________
Tester: ______________
Browser: _____________
Device: ______________

✅ = PASS
❌ = FAIL
⚠️  = WARNING

TEST RESULTS:
─────────────────────────────────────────
TEST 1: Guest View         [✅ ❌ ⚠️]
TEST 2: Logged-In View     [✅ ❌ ⚠️]
TEST 3: Header             [✅ ❌ ⚠️]
TEST 4: Hero Banner        [✅ ❌ ⚠️]
TEST 5: Categories         [✅ ❌ ⚠️]
TEST 6: Products           [✅ ❌ ⚠️]
TEST 7: Size Modal         [✅ ❌ ⚠️]
TEST 8: Size Selection     [✅ ❌ ⚠️]
TEST 9: Add to Cart        [✅ ❌ ⚠️]
TEST 10: Badge Updates     [✅ ❌ ⚠️]
TEST 11: Cart Navigation   [✅ ❌ ⚠️]
TEST 12: Bottom Nav        [✅ ❌ ⚠️]
TEST 13: Mobile Responsive [✅ ❌ ⚠️]
TEST 14: Tablet Responsive [✅ ❌ ⚠️]
TEST 15: Desktop Responsive[✅ ❌ ⚠️]
TEST 16: Search Bar        [✅ ❌ ⚠️]
TEST 17: Menu Nav          [✅ ❌ ⚠️]
TEST 18: Multi Add         [✅ ❌ ⚠️]
TEST 19: Server Sync       [✅ ❌ ⚠️]
TEST 20: Browser Compat    [✅ ❌ ⚠️]

ISSUES FOUND:
─────────────────────────────────────────
1. [Description of issue]
2. [Description of issue]
3. [Description of issue]

OVERALL RESULT: ✅ PASS / ❌ FAIL
```

---

## 🎯 Quick Test (5 Minutes)

If you just want a quick verification:

1. **Login** to your account
2. **Visit** http://localhost:5000/
3. **Check** you see the new home page (orange header, hero banner)
4. **Click** the [+] on a product
5. **Click** "Add to Cart"
6. **Verify** cart badge shows "1"
7. **Click** cart FAB
8. **Verify** item appears in cart

**✅ If all above works, homepage is good!**

---

## 🚀 You're Ready!

All tests passing? Great! Your new homepage is:

✅ Fully functional  
✅ Responsive  
✅ Integrated with database  
✅ Connected to cart  
✅ Ready for users  

**Enjoy your new modern design!** 🎉

---

*Testing Guide for CiTea Coolers Homepage*  
*Created: Feb 9, 2026*  
*Total Tests: 20*  
*Quick Test Time: 5 minutes*  
*Full Test Time: 30 minutes*
