# Recursive brute force
def fib(n):
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)
print(fib(int(input())))

# Time Complexity = O(n), Space Complexity = O(1) Code.
n = int(input())

x, y = 0, 1

for i in range(0, n):
    x, y = y, x + y
print(x)
