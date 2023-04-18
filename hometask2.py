lambda_ = 0.95
import math
D = 4
S = math.sqrt(4)
M = 17
x = 17.5
n = 100
t_lambda_ = ((x - M) / S) * math.sqrt(n)

t_critical_ = 1.645

if t_lambda_ <= t_critical_:
    print('Принимаем гипотезу H0')
else:
    print('Принимаем гипотезу H1')