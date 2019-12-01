"""
procedure karatsuba(num1, num2)
  if (num1 < 10) or (num2 < 10)
    return num1 * num2

  /* Calculates the size of the numbers. */
  m = min(size_base10(num1), size_base10(num2))
  m2 = floor(m / 2)
  /*m2 = ceil(m / 2) will also work */

  /* Split the digit sequences in the middle. */
  high1, low1 = split_at(num1, m2)
  high2, low2 = split_at(num2, m2)

  /* 3 calls made to numbers approximately half the size. */
  z0 = karatsuba(low1, low2)
  z1 = karatsuba((low1 + high1), (low2 + high2))
  z2 = karatsuba(high1, high2)

  return (z2 * 10 ^ (m2 * 2)) + ((z1 - z2 - z0) * 10 ^ m2) + z0
"""

from math import log10, floor


def km(a, b):
    if a < 10 or b < 10:
        return a*b
    m = min(base10_size(a), base10_size(b))
    m2 = floor(m/2)

    a1, a0 = split_at(a, m2)
    b1, b0 = split_at(b, m2)

    z0 = km(a0, b0)
    z1 = km((a0 + a1), (b0 + b1))
    z2 = km(a1, b1)

    return (z2 * (10**(m2*2))) + ((z1 - z2 - z0) * (10**m2)) + z0


def base10_size(n):
    return int(log10(n)) + 1


def split_at(n, b):
    n1 = int(n/(b*10))
    n0 = n - (n1*(b*10))
    return n1, n0


assert 99813 == km(343, 291)
assert 1628457 == km(543, 2999)

# whatever python uses is substantially faster possibly a different algo or just c/c++ speed
assert km(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627) == 2718281828459045235360287471352662497757247093699959574966967627*3141592653589793238462643383279502884197169399375105820974944592
print(km(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
