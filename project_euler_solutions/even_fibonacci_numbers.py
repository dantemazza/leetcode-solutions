fib = [1, 2]
res = 0
while fib[1] < 4e6:
    if not fib[1] % 2:
        res += fib[1]
    temp = sum(fib)
    fib = [fib[1], temp]

print(res)
