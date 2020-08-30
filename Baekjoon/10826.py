# Time Complexity = O(n), Space Complexity = O(1) Code.
n = int(input())

x, y = 0, 1

for i in range(0, n):
    x, y = y, x + y
print(x)