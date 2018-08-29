#program-for-nth-fibonacci-number
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):

    if n==0:
        return 0
    if n == 1 :
        return 1
    else:
        return fib(n-2) + fib(n-1)

for i in range(100):
    print(fib(i))