import numpy as np
import matplotlib.pyplot as plt
from keygen import *

N = 500
W, H = N, N
TUPLE= key_init("goodboy", W, H)

total = np.zeros(max(W,H))
degree= int(3.5*W*H)

a = TUPLE
b = TUPLE

for j in range(degree):
    a=b
    b= next_tuple(a)
    L = len(a)
    for i in range(L):
        a1, a2 = a[i][0]%H, a[i][1]%W
        b1, b2 = b[i][0]%H, b[i][1]%W
        total[a1]= total[a1]+1
        total[a2]= total[a2]+1
        total[b1]= total[b1]+1
        total[b2]= total[b2]+1
        # print(a1,a2,b1,b2)

plt.plot(list(range(N)), total)
plt.show()
