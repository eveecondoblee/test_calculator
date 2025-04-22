def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

def square(n, i=100):
  if n < 0:
    raise ValueError("Cannot calculate square root of negative number")
  approx = n
  for _ in range(i):
    approx = 0.5 * (approx + n / approx)
  return approx

def exponential(x, i=100):
  result = 1.0
  term = 1.0
  for n in range(1, i):
    term *= x / n
    result += term
    if abs(term) < 0.001:
      break
  return result