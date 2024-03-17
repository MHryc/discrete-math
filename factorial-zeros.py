import numpy as np
import matplotlib.pyplot as plt
import math
import sys

sys.set_int_max_str_digits(10000)

n_range_str = input('Input the upper limit of n: ')
n_range = int(n_range_str) + 1

factorials = []
for A in range(5, n_range):
    int_factorial = math.factorial(A)
    s_factorial = str(int_factorial)
    factorials.append(s_factorial)

factorial_zeros = []
for B in range(n_range - 5):
    fact_str = factorials[B]
    n = -1
    while fact_str[n] == '0':
        n = n - 1
    else:
        number_of_zeros = -(n) - 1
        factorial_zeros.append(number_of_zeros)

factorial_length = []
for C in range(n_range - 5):
    factorial_n = factorials[C]
    fact_len = len(factorial_n)
    factorial_length.append(fact_len)

fact_ratio = []
for D in range(n_range - 5):
    ratio = factorial_zeros[D] / factorial_length[D]
    rounded_ratio = round(ratio, 3)
    fact_ratio.append(rounded_ratio)

print(factorial_length)
print(factorial_zeros)
print(fact_ratio)

X = range(n_range - 5)
plt.plot(X, fact_ratio)
plt.plot(X, factorial_zeros)
plt.plot(X, factorial_length)
plt.xlabel('Consecutive natural numbers ≥ 5')
plt.ylabel('Ratio')
plt.grid(True)
plt.show()
