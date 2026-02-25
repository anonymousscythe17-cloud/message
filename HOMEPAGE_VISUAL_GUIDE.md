# 🎨 CiTea Coolers - Homepage Visual Guide

## 📱 What It Looks Like

### **Mobile View (Primary)**

```
┌─────────────────────────────┐
│  🍵 CiTea Coolers           │  ← Header with location
│  📍 Matnog, Sorsogon   👤   │     and profile button
├─────────────────────────────┤
│  🔍 Search food...          │  ← Search bar
├─────────────────────────────┤
│                             │
│  ┌───────────────────────┐  │
│  │ 🍵 Premium Drinks     │  │  ← Hero Banner
│  │ Enjoy the finest tea  │  │
│  │ [Shop Now]            │  │
│  └───────────────────────┘  │
│                             │
│ 📂 Categories        See All│
│ ┌──┬──┬──┬──┐                │
│ │🍵│☕│🥤│🧋│               │  ← Category buttons
│ │All│Hot│Cold│Tea│          │
│ └──┴──┴──┴──┘                │
│                             │
│ ⭐ Featured        See All   │
│ ┌──────────┬──────────┐     │
│ │          │          │     │
│ │ Oolong   │ Matcha   │     │  ← Product cards
│ │ Tea      │ Latte    │     │     (2 per row)
│ │ ₱120     │ ₱150     │     │
│ │    [+]   │    [+]   │     │
│ └──────────┴──────────┘     │
│ ┌──────────┬──────────┐     │
│ │          │          │     │
│ │ Taro     │ Brown    │     │
│ │ Drink    │ Sugar    │     │
│ │ ₱130     │ ₱110     │     │
│ │    [+]   │    [+]   │     │
│ └──────────┴──────────┘     │
│                             │
├─────────────────────────────┤
│ 🏠  📜  🛒⓪  💬  👤        │  ← Bottom Navigation
└─────────────────────────────┘
```

---

## 🖥️ Desktop View

```
┌──────────────────────────────────────────────────────────────┐
│ 🍵 CiTea Coolers  🏠 📜 👤 💬  🛒⓪                       │  ← Top Nav
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Products displayed in larger grid                          │
│  ┌──────────┬──────────┬──────────┐                         │
│  │          │          │          │                         │
│  │ Product1 │ Product2 │ Product3 │  ← 3 columns            │
│  │          │          │          │                         │
│  └──────────┴──────────┴──────────┘                         │
│                                                              │
│  ┌──────────┬──────────┬──────────┐                         │
│  │          │          │          │                         │
│  │ Product4 │ Product5 │ Product6 │                         │
│  │          │          │          │                         │
│  └──────────┴──────────┴──────────┘                         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📋 Size Selection Modal

```
┌──────────────────────────────┐
│  Matcha Latte                │  ← Product name
├──────────────────────────────┤
│                              │
│  ☐ Small  ₱120               │  ← Size options
│  ☐ Medium ₱140               │    (radio buttons)
│  ⦿ Large  ₱160               │
│                              │
│  Quantity: [1⬆⬇]             │  ← Qty input
│                              │
│  Total: ₱160.00              │  ← Real-time total
│                              │
│  [Cancel]  [Add to Cart]     │  ← Action buttons
└──────────────────────────────┘
```

---

## 🎯 User Flow

### **Guest User (Not Logged In)**

```
Visit Home (/)
    ↓
See Landing Page
(Old page still shown)
    ↓
Links to Login/Register
```

### **Logged-In User**

```
Visit Home (/)
    ↓
See New Home Page
    ├─ View Featured Products
    ├─ Click Product [+]
    │   ↓
    │   Size Modal Opens
    │   ↓
    │   Select Size
    │   ↓
    │   Choose Quantity
    │   ↓
    │   [Add to Cart]
    │   ↓
    │   Cart Badge Updates ✨
    │
    └─ Click Categories
        ↓
        Filter Products
        ↓
        Or: Click "See All"
        ↓
        Go to Full Menu
```

---

## 🔄 Data Flow

```
┌──────────────────────────────────────────────┐
│           DATABASE                          │
│  ┌──────────────┐  ┌──────────────┐        │
│  │   Products   │  │  Categories  │        │
│  │  - name      │  │  - id        │        │
│  │  - price     │  │  - name      │        │
│  │  - variants  │  │  - desc      │        │
│  │  - image     │  └──────────────┘        │
│  └──────────────┘                          │
└────────────┬─────────────────────────────────┘
             │
             ↓ Query by Flask
┌──────────────────────────────────────────────┐
│         HOME.HTML (Template)                 │
│  - Displays products                         │
│  - Shows categories                          │
│  - Renders modals                            │
│  - Handles clicks                            │
└────────────┬─────────────────────────────────┘
             │
             ↓ JavaScript
┌──────────────────────────────────────────────┐
│      LOCAL STORAGE (Browser)                 │
│  {                                           │
│    "id": 1,                                  │
│    "name": "Matcha",                         │
│    "size": "Large",                          │
│    "price": 160,                             │
│    "quantity": 2                             │
│  }                                           │
└────────────┬─────────────────────────────────┘
             │
             ↓ On Login/Add to Cart
┌──────────────────────────────────────────────┐
│         SERVER (/api/cart)                   │
│  - Saves cart to database                    │
│  - Associates with user_id                   │
│  - Ready for checkout                        │
└──────────────────────────────────────────────┘
```

---

## 🎨 Component Breakdown

### **Header Component**
```html
<header>
  Location Display (📍)
  Search Bar (🔍)
  Profile Icon (👤)
</header>
```

### **Hero Banner Component**
```html
<div class="hero-banner">
  Title: "🍵 Premium Drinks"
  Description: "Enjoy the finest quality tea..."
  Button: "Shop Now" → Links to /menu
</div>
```

### **Categories Component**
```html
<div class="category-grid">
  Multiple category buttons (4 per row)
  Each category clickable
  Shows as: Icon + Name
</div>
```

### **Product Card Component**
```html
<div class="food-card">
  Product Image
  Product Name
  Price (or first variant price)
  [+] Add Button → Opens Modal
</div>
```

### **Bottom Navigation Component**
```html
<nav class="bottom-nav">
  Home (🏠) - Active
  Menu (📜)
  Cart FAB (🛒) - Floating, Highlighted
  Chat (💬)
  Profile (👤)
</nav>
```

---

## 🎯 Interactive Elements

### **Clickable Elements:**

| Element | Action | Result |
|---------|--------|--------|
| Category Button | Click | Navigate to /menu with filter |
| Product [+] | Click | Open size modal |
| Size Option | Select | Update price calculation |
| Quantity Input | Change | Update total price |
| Add to Cart | Click | Save to localStorage + update badge |
| Shop Now | Click | Go to /menu |
| Cart FAB | Click | Navigate to /cart |
| Menu Button | Click | Navigate to /menu |
| Profile Icon | Click | Navigate to /profile |
| Chat Button | Click | Navigate to /chat |

---

## 📐 Responsive Breakpoints

```
Mobile (< 768px)
├─ Single column header
├─ Bottom navigation visible
├─ 2-column product grid
└─ 4-column category grid

Tablet (768px - 1024px)
├─ Same mobile layout
├─ 3-column product grid
└─ Bottom navigation visible

Desktop (> 1024px)
├─ Top navigation only
├─ 3+ column product grid
├─ No bottom navigation
└─ No hero banner (homepage only shown to logged-in)
```

---

## 🎨 Color Palette

```
Primary Orange      #D35400  ← Main brand color
  ├─ Buttons
  ├─ Links
  ├─ Highlights
  └─ Cart FAB

Dark Brown          #5D2906  ← Dark accents
  ├─ Header
  ├─ Cancel buttons
  └─ Secondary text

Light Orange        #FFF7ED  ← Light background
  ├─ Category backgrounds
  └─ Hover states

Text Colors:
  ├─ Dark text      #333    ← Main text
  ├─ Gray text      #888    ← Secondary text
  └─ White          #fff    ← On dark backgrounds

Alerts:
  ├─ Success        #2e7d32 ← Green
  ├─ Error          #d32f2f ← Red
  └─ Neutral        #666    ← Gray
```

---

## 📱 Mobile Optimization

### **Touch Targets**
- Minimum 44x44px for buttons ✅
- Proper spacing between clickable elements ✅
- No hover-required interactions ✅

### **Performance**
- No lazy loading (yet - could be added)
- Minimal JavaScript ✅
- CSS Grid for layout ✅
- LocalStorage for quick access ✅

### **Accessibility**
- Semantic HTML ✅
- ARIA labels ready ✅
- Font sizes readable ✅
- Color contrast sufficient ✅

---

## 🔄 State Management

### **Cart State**
```javascript
Cart = [
  {
    id: 1,
    name: "Matcha Latte",
    size: "Large",
    price: 160,
    quantity: 2
  },
  {
    id: 2,
    name: "Oolong Tea",
    size: "Medium",
    price: 120,
    quantity: 1
  }
]
```

### **Modal State**
```javascript
Modal = {
  isOpen: true/false,
  productId: null,
  productName: "",
  variants: [],
  selectedSize: 0,
  quantity: 1,
  total: 0
}
```

### **User State**
```javascript
User = {
  isLoggedIn: true/false,
  userId: null,
  username: "",
  profileUrl: ""
}
```

---

## 🚀 Animation Effects

```
Component                   Animation
─────────────────────────────────────────
Product Cards              Hover: slide up + shadow
Category Buttons           Hover: color change
Navigation Icons           Hover: color change
Cart FAB                   Hover: scale up
Modals                     Fade in/out
Buttons                    Click: brief scale
Badges                     Update: color pulse
```

---

## 📊 Navigation Hierarchy

```
Level 1: Home Page
  ├─ Featured Products
  ├─ Categories
  └─ Modals

Level 2: Navigation Destinations
  ├─ /menu (Full Menu)
  ├─ /cart (Shopping Cart)
  ├─ /chat (Messages)
  ├─ /profile (User Profile)
  ├─ /login (Login)
  └─ /register (Register)

Level 3: Forms
  ├─ Size Selection
  ├─ Quantity Input
  └─ Checkout
```

---

## ✨ Summary

The homepage is a **beautiful, modern mobile-first interface** that:

- 🎯 Shows relevant products immediately
- 🛒 Makes adding to cart super easy
- 📱 Works perfectly on all devices
- ⚡ Loads fast and feels smooth
- 🔐 Respects user login status
- 🎨 Uses your brand colors perfectly

**Visual, functional, and ready to use!** 🎉

---

*Design Pattern: Mobile-First Responsive*  
*Color Scheme: Orange & Brown (Brand Colors)*  
*Framework: Pure HTML5 + CSS3 + Vanilla JavaScript*  
*Mobile Optimized: ✅*  
*Responsive: ✅*  
*Accessible: ✅*
