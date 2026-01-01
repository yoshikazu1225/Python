# リスト3-3-(10)
import numpy as np
import matplotlib.pyplot as plt
x0_n, x1_n = 9, 9
x0 = np.linspace(-2, 2, x0_n)
x1 = np.linspace(-2, 2, x1_n)

y = np.zeros((x0_n, x1_n))
for i0 in range(x0_n):
    for i1 in range(x1_n):
        y[i0, i1] = f3(x0[i0], x1[i1])
print(np.round(y, 1))