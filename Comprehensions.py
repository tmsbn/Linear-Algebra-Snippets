__author__ = 'tmsbn'


# Format for conditional = [Expression for item in lists if conditional]

S = [45, 23, 12, -23]
print [x for x in S if x >= 0]

# All numbers for a particular range
print [x for x in range(30)]

# All even numbers
print [x for x in range(0, 11) if x % 2 == 0]

# All squares
print [x ** 2 for x in range(0, 10)]

# Pythogorean triplets
print [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]

# Extract all numbers from a string
print [x for x in "Hello 123, how are you doing?," if x.isdigit()]


# Prime numbers
def is_prime(x):
    return [y for y in range(2, x) if x % y == 0]

print [x for x in range(2, 100) if not is_prime(x)]

print [(x, x*2) for x in range(1, 100)]









