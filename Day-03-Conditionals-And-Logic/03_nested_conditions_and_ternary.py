# Day 03: Lesson 3 - Nested Conditions, Ternary Operator & Membership Checks

# 1. Nested If Statements: ATM Cash Withdrawal Simulation
account_pin = "1234"
entered_pin = "1234"
is_card_active = True
account_balance = 25000.0
withdrawal_amount = 5000.0

print("--- 1. ATM Simulation (Nested If-Else) ---")
if entered_pin == account_pin:
    if is_card_active:
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"Transaction Successful! Dispensed: PKR {withdrawal_amount:,.2f}")
            print(f"Remaining Balance: PKR {account_balance:,.2f}")
        else:
            print("Transaction Declined: Insufficient balance.")
    else:
        print("Card is blocked. Please contact your bank.")
else:
    print("Security Alert: Invalid PIN entered!")

# 2. Python Ternary Operator (Conditional Expression)
# Syntax: value_if_true if condition else value_if_false
print("\n--- 2. Ternary Operator (One-line if-else) ---")
user_age = 19
access_status = "Access Granted" if user_age >= 18 else "Access Denied (Underage)"
print(f"Age: {user_age} -> Result: {access_status}")

# 3. Membership Operator: 'in' and 'not in' with Conditionals
print("\n--- 3. Membership Operator in Conditions ---")
blocked_emails = ["spam@mail.com", "hacker@test.com", "bot@service.net"]
incoming_email = "hammad@developer.com"

if incoming_email not in blocked_emails:
    print(f"Email '{incoming_email}' is clean and allowed.")
else:
    print(f"Warning: Email '{incoming_email}' is in the blocked blacklist!")
