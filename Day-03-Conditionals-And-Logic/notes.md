# 📝 Day 03 Notes: Conditionals & Logical Operators

## 1. Indentation in Python
- C++ ya Java mein curly braces `{}` use hote hain, lekin Python mein **Indentation** (4 spaces) se block of code tay hota hai.
- Hamesha colon `:` ke baad agli line 4 spaces aage shuru hoti hai:
  ```python
  if condition:
      # indented block
      statement
  ```

## 2. Comparison Operators
- `==` Equal value check karta hai (assignment `=` se mukhtalif hai)
- `!=` Not equal to
- `>`, `<`, `>=`, `<=` Greater than, Less than, etc.

## 3. Logical Operators
- `and`: Dono conditions ka `True` hona lazmi hai.
- `or`: Dono mein se kisi ek ka bhi `True` hona kafi hai.
- `not`: Boolean result ko invert kar deta hai (`not True` -> `False`).

## 4. Truthy vs Falsy
Python mein yeh tamam values **Falsy** (False) maani jati hain:
- `0`, `0.0`
- Khali strings: `""`
- `None`
- Khali collections: `[]`, `()`, `{}`
In ke ilawa baki tamam values **Truthy** (True) hoti hain.

## 5. Ternary Operator (Single-line if-else)
Python mein chote conditions ke liye compact syntax:
```python
result = "Pass" if marks >= 50 else "Fail"
```

## 6. Membership Checks
- `in` aur `not in` operators list ya string ke andar item dhoondne ke liye conditions mein use hote hain:
  ```python
  if "admin" in roles:
      ...
  ```
