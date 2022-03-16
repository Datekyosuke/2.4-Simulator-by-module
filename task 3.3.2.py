import numpy as np
r_array = np.array(input().split(), dtype=float)
i_array = np.array(input().split(), dtype=float)
R_1 = [1/r_array]
R = 1 / np.sum(R_1)
I = np.sum(i_array)
U = I * R
print("R = %6.3f Ом, I = %6.3f А, U = %6.3f В" % (R, I, U))