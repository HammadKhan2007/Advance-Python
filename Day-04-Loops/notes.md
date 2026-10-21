# 📝 Day 04 Notes: Loops & Iteration

## 1. What is a Loop?
A loop is used when you want to repeat a block of code multiple times without writing it again and again.

Python main 2 important loops hotay hain:
- `for` loop
- `while` loop

---

## 2. For Loop
`for` loop sequence ke har item ke liye repeat hota hai.

```python
for item in [1, 2, 3, 4]:
    print(item)
```

Common uses:
- List iteration
- String character iteration
- Range iteration
- Repeating tasks a fixed number of times

---

## 3. `range()` Function
`range(start, stop, step)` ka use repeated numbers generate karne ke liye hota hai.

```python
for i in range(1, 11):
    print(i)
```

Important points:
- `stop` value include nahi hoti.
- `range(5)` -> `0, 1, 2, 3, 4`
- `range(1, 6)` -> `1, 2, 3, 4, 5`
- `range(2, 11, 2)` -> `2, 4, 6, 8, 10`

---

## 4. While Loop
`while` loop tab tak chalta hai jab condition `True` ho.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

Note:
- `while` loop ka condition carefully set karna zaroori hota hai.
- Agar condition kabhi `False` nahi hoti to infinite loop ban sakta hai.

---

## 5. `break` and `continue`
### `break`
Loop ko immediately stop kar deta hai.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

### `continue`
Current iteration skip kar deta hai aur agla iteration chalta hai.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

---

## 6. Nested Loops
Loop ke andar doosra loop use karna bhi mumkin hai.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Yeh pattern tables, patterns, grids, matrices ke liye useful hota hai.

---

## 7. `enumerate()`
Agar aapko index aur value dono chahiyein to `enumerate()` use hota hai.

```python
fruits = ["Apple", "Mango", "Banana"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

---

## 8. Day 04 Target / What to Practice
Aaj ka goal simple aur practical hona chahiye:

### Must Do
1. `for` loop basics samjho
2. `range()` ke examples practice karo
3. `while` loop syntax aur logic samjho
4. `break` aur `continue` ke difference ko samjho
5. 3-5 mini exercises banao
6. nested loop ka basic concept samjho

### Recommended Practice Questions
- 1 se 10 tak numbers print karna
- Even/odd numbers print karna
- Sum of numbers from 1 to 100
- Countdown timer with `while`
- Multiplication table generate karni
- Factorial ya password loop ka mini program

---

## 9. Day 04 Daily Goal
Aaj ke liye kam yeh hona chahiye:
- 30-45 minutes coding
- 10-15 small examples
- 2-3 mini projects
- concepts properly practice karo, sirf notes nahi dekhna

Agar tum daily 1 file ko complete kar loge, to Day 04 ka concept clear ho jayega.

---

## 10. Quick Example Summary
```python
# For loop
for i in range(1, 6):
    print(i)

# While loop
count = 1
while count <= 5:
    print(count)
    count += 1
```

Yeh Day 04 ka core concept hai. In par focus karo aur practice karo.
