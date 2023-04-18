lambda_ = 0.99
import numpy as np
import math
X = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]

S = np.std(X)
M = 200
x = np.mean(X)

n = 100

t_lambda_ = abs(((x - M) / S) * math.sqrt(n))

t_critical_ = 2.58

if t_lambda_ <= t_critical_:
    print('Принимаем гипотезу H0')
else:
    print('Принимаем гипотезу H1')