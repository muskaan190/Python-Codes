# Given an integer n, calculate n-th fibonacci number
# This is recursive algorithm to find n-th fibonacci number.


def fibonacci(n):
	fib = [0, 1]
	for i in range(2, n+1):
		fib.append(fib[i-1] + fib[i-2])
	return fib[n]

n=int(input())
print(fibonacci(n))
