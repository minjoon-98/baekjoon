import sys

F = [0, 1]
n = int(sys.stdin.readline())
def fibonacci(n):
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[n]
print(fibonacci(n))