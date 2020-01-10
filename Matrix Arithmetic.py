import numpy as np
import time

# 10,000 guassian variables in an array with random values
a = np.random.rand(10000)
b = np.random.rand(10000)

# timer value before statement
tic = time.time()

# vectorized way of matrix multiplication 
c = np.dot(a,b)

# timer value after statement
toc = time.time()

# output Matrix multiplication 
print(c)

# output time difference
print(str(1000*(toc - tic)))

c = 0
# timer value before statement
tic = time.time()

# matrix multiplication without vectorization
for i in range(10000):
    c += a[i] * b[i]

# timer value after statement
toc = time.time()


# output Matrix multiplication 
print(c)

# output time difference
print(str(1000*(toc - tic)))
