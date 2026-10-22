# Day 06: Tuples and Sets

print("=" * 60)
print("DAY 06 - LESSON 2: TUPLES & SETS")
print("=" * 60)

# 1. Tuple basics
print("\n--- 1. Tuple Creation ---")
colors = ("red", "green", "blue")
print("Colors tuple:", colors)

single_value_tuple = (5,)
print("Single value tuple:", single_value_tuple)

# 2. Tuple indexing
print("\n--- 2. Tuple Indexing ---")
print("First color:", colors[0])
print("Last color:", colors[-1])

# 3. Tuple immutability
print("\n--- 3. Tuple Immutability ---")
print("Tuple cannot be changed after creation.")
print("Example: colors[0] = 'yellow'  # This would raise TypeError")

# 4. Set basics and uniqueness
print("\n--- 4. Set Creation & Uniqueness ---")
nums = {1, 2, 2, 3, 4, 4, 5}
print("Set removes duplicates:", nums)

# 5. Common set operations
print("\n--- 5. Set Operations ---")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# 6. Set methods
print("\n--- 6. Set Methods ---")
set_a.add(10)
print("After add:", set_a)

set_a.remove(2)
print("After remove:", set_a)

set_a.discard(100)
print("After discard(100):", set_a)

print("\nTuple & Set lesson complete!")
print("=" * 60)
