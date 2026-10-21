# 📝 Day 05 Notes: Functions & Scope

## 1. What is a Function?
A function is a reusable block of code that performs a specific task.

Instead of writing the same logic again and again, you define it once and call it whenever needed.

```python
def greet():
    print("Hello, Python!")

greet()
```

---

## 2. Why Use Functions?
Functions help us:
- avoid repeated code
- make code cleaner
- make programs easier to debug
- reuse logic multiple times

---

## 3. Function Syntax
```python
def function_name(parameters):
    # body
    return result
```

### Example
```python
def add(a, b):
    return a + b

print(add(3, 5))
```

---

## 4. Parameters and Arguments
- Parameter: function definition mein jo variable use hota hai
- Argument: function call ke waqt diya gaya value

```python
def square(num):
    return num * num

print(square(4))
```

---

## 5. Return vs Print
### `print()`
- Output show karta hai
- Value ko store nahi karta

### `return`
- Function se value return karta hai
- Use future operations ke liye hota hai

```python
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)
```

---

## 6. Default Parameters
Agar argument na die jaye to default value use ho sakti hai.

```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Hammad")
```

---

## 7. Scope of Variables
Variable ka scope determine karta hai ke wo variable kaha accessible hai.

### Local Variable
Function ke andar define hota hai, sirf us function mein accessible hota hai.

```python
def demo():
    x = 10
    print(x)
```

### Global Variable
Function ke bahar define hota hai aur poore program mein accessible hota hai.

```python
name = "Python"

def print_name():
    print(name)
```

---

## 8. Global vs Local Variable Rule
Agar function ke andar same naam ka variable define ho to local variable priority leta hai.

```python
value = 50

def show():
    value = 20
    print(value)

show()
print(value)
```

---

## 9. Built-in Functions You Must Know
Some common built-ins:
- `print()`
- `len()`
- `sum()`
- `max()`
- `min()`
- `type()`
- `input()`

---

## 10. Day 05 Practice Goals
Aaj ka focus yeh hai:

### Must do:
1. Function definition syntax samjho
2. Parameter aur argument difference samjho
3. `return` aur `print()` difference
4. Default arguments practice karo
5. Local aur global scope ko understand karo
6. 4-6 mini tasks complete karo

### Recommended questions:
- 2 numbers ke sum ka function banao
- Even/odd checker function
- Factorial function
- Greeting function with name parameter
- Calculator function
- Area of rectangle function

---

## 11. Daily Study Rule for Advanced Python Prep
Aaj ka kaam simple rahega:
- 30-45 mins coding
- 10-15 mins notes revision
- 3-5 practical functions
- concepts ko repeat karo

Agar tum har din ek topic ko properly practice karoge, to Python advance level me progression smooth hoga.

---

## 12. Quick Summary
```python
def add(a, b):
    return a + b

print(add(2, 3))
```

Function ka core concept yahi hai: logic ko reusable aur organized way mein rakho.
