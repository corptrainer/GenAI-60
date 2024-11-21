# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operations:")
print(f"{a} + {b} = {a + b}")     # Addition
print(f"{a} - {b} = {a - b}")     # Subtraction
print(f"{a} * {b} = {a * b}")     # Multiplication
print(f"{a} / {b} = {a / b}")     # Division
print(f"{a} % {b} = {a % b}")     # Modulus
print(f"{a} ** {b} = {a ** b}")   # Exponentiation
print(f"{a} // {b} = {a // b}")   # Floor Division

# Comparison Operators
print("\nComparison Operations:")
print(f"{a} == {b}: {a == b}")    # Equal to
print(f"{a} != {b}: {a != b}")    # Not equal to
print(f"{a} < {b}: {a < b}")      # Less than
print(f"{a} <= {b}: {a <= b}")    # Less than or equal to
print(f"{a} > {b}: {a > b}")      # Greater than
print(f"{a} >= {b}: {a >= b}")    # Greater than or equal to

# Logical Operators
x = True
y = False

print("\nLogical Operations:")
print(f"x and y: {x and y}")      # AND
print(f"x or y: {x or y}")        # OR
print(f"not x: {not x}")          # NOT

# Bitwise Operators
c = 5   # (binary: 0101)
d = 3   # (binary: 0011)

print("\nBitwise Operations:")
print(f"c & d = {c & d}")         # Bitwise AND
print(f"c | d = {c | d}")         # Bitwise OR
print(f"c ^ d = {c ^ d}")         # Bitwise XOR
print(f"~c = {~c}")                # Bitwise NOT (inverts bits)
print(f"c << 1 = {c << 1}")       # Left Shift
print(f"c >> 1 = {c >> 1}")       # Right Shift

# Assignment Operators
e = 10

print("\nAssignment Operations:")
e += 5   # Equivalent to e = e + 5
print(f"e after += 5 : {e}")

e -= 3   # Equivalent to e = e - 3
print(f"e after -= 3 : {e}")

# Identity Operators
f = [1, 2, 3]
g = f

print("\nIdentity Operations:")
print(f"f is g : {f is g}")       # True, both refer to same object

h = f[:]
print(f"f is h : {f is h}")       # False, h is a copy of f

# Membership Operators
list1 = [1, 2, 3, 4]

print("\nMembership Operations:")
print("2 in list1:", 2 in list1)      # True, as 2 is in list1
print("5 not in list1:", 5 not in list1)  # True, as 5 is not in list1