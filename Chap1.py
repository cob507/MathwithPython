# Addition and subtraction

print (1 + 2)
print (1 + 3.5)
print (-1 + 2.5)
print (100 - 45)
print (-1.1 + 5)

# Multiplication

print (3 * 2)
print (3.5 * 1.5)

# Division (with decimal place)

print (3 / 2)
print (4 / 2)

# Division (Just integers)

print (3 // 2)
print (-3 // 2)

# Division (Just the remainder)

print (9 % 2)

# ** Means Exponent

print (2 ** 2)
print (2 ** 10)
print (1 ** 10)

# We can also use the exponential symbol to calculate powers less than 1.
# For example, the square root of a number n can be expressed as n^1/2
# and the cube root as n^1/3:

print (8 ** (1/3))

# you can use parentheses to combine mathematical operations into
# more complicated expressions. Python will evaluate the expression
# following the standard PEMDAS rule for the order of
# calculations-parentheses, exponents, multiplication, division, addition,
# and subtraction. Consider the following two expressions-one without
# parentheses and one with:

print (5 + 5 * 5)
print ((5 + 5) * 5)

# As we start designing more complex Python programs,
# we'll assign names to numbers -at times for convenience,
# but mostly out of necessity. Here's a simple example:

a = 3
print (a + 1)
a = 5
print (a + 1)

print (type(3))
print (type(3.5))
print (type(3.0))
print (int(3.8))
print (int(3.0))
print (float(3))

from fractions import Fraction
f = Fraction(3, 4)
print (f)
print (Fraction(3, 4) + 1 + 1.5)
print (Fraction(3, 4) + 1 + Fraction(1/4))

a = 2 + 3j
print (type(a))
a = complex(2, 3)
print (a)
b = 3 + 3j
print (a + b)
print (a - b)
print (a * b)
print (a / b)
