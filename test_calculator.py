import pytest
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide
from calculator import square

def test_add():
  assert add(2, 3) == 5
  assert add(-1 , 1) == 0

def test_subtract():
  assert subtract(5, 3) == 2
  assert subtract(0, 0) == 0

def test_multiply():
  assert multiply(2, 3) == 6
  assert multiply(-1, 1) == -1

def test_divide():
  assert divide(6, 3) == 2.0
  assert divide(5, 2) == 2.5

def test_divide_by_zero():
  with pytest.raises(ValueError):
    divide(5, 0)

def test_square():
  assert abs(square(2) - 1.4142) < 0.001  # √2 ≈ 1.4142
  assert abs(square(9) - 3.0) < 0.001