# Day 03: Practical Exercises & Real-World Projects

print("=" * 60)
print("DAY 03: CONDITIONALS & LOGICAL OPERATORS PROJECTS")
print("=" * 60)

# -------------------------------------------------------------
# Project 1: Smart E-Commerce Discount & Free Shipping Engine
# -------------------------------------------------------------
print("\n--- Project 1: Smart E-Commerce Checkout Engine ---")
cart_subtotal = 6500.00
is_premium_member = True

# Discount tiers:
# > 10,000 PKR -> 20% discount
# > 5,000 PKR  -> 10% discount
# Otherwise    -> 0% discount
if cart_subtotal >= 10000:
    discount_pct = 20
elif cart_subtotal >= 5000:
    discount_pct = 10
else:
    discount_pct = 0

# Premium member perk: extra 5% discount
if is_premium_member:
    discount_pct += 5

discount_val = (cart_subtotal * discount_pct) / 100
discounted_subtotal = cart_subtotal - discount_val

# Shipping policy: Free shipping if discounted_subtotal > 3000 or premium member
if discounted_subtotal > 3000 or is_premium_member:
    shipping_fee = 0.0
else:
    shipping_fee = 250.0

final_payable = discounted_subtotal + shipping_fee

print(f"Cart Subtotal   : PKR {cart_subtotal:,.2f}")
print(f"Discount Applied: {discount_pct}% (-PKR {discount_val:,.2f})")
print(f"Shipping Cost   : PKR {shipping_fee:,.2f} ({'FREE Shipping Applied!' if shipping_fee == 0 else 'Standard Delivery'})")
print(f"Total Payable   : PKR {final_payable:,.2f}")

# -------------------------------------------------------------
# Project 2: Leap Year Checker Algorithm
# -------------------------------------------------------------
print("\n--- Project 2: Leap Year Algorithm ---")
year = 2024

# Rule: A year is a leap year if:
# Divisible by 4 AND (NOT divisible by 100 OR divisible by 400)
is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap:
    print(f"Year {year} is a LEAP year (366 days, Feb has 29 days).")
else:
    print(f"Year {year} is a REGULAR year (365 days, Feb has 28 days).")

# -------------------------------------------------------------
# Project 3: Role-Based Access Control (RBAC) System
# -------------------------------------------------------------
print("\n--- Project 3: Role-Based Authorization System ---")
user_role = "editor"   # Can be: 'admin', 'editor', 'viewer'
is_authenticated = True

if not is_authenticated:
    print("Action Prohibited: Please login first.")
else:
    if user_role == "admin":
        print("Permissions: Full Access (Create, Read, Update, Delete, Manage Users).")
    elif user_role == "editor":
        print("Permissions: Editor Access (Create, Read, Update Content).")
    elif user_role == "viewer":
        print("Permissions: Read-Only Access (View Published Content).")
    else:
        print("Access Error: Unrecognized user role assigned.")
