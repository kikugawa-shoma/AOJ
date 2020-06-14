n = int(input())
memo = [-1]*(n+1)
memo[0] = 1
memo[1] = 1

def fib(n):
    if memo[n] != -1:
        return memo[n]
    else:
        ans = fib(n-1)+fib(n-2)
        memo[n] = ans
        return ans

print(fib(n))