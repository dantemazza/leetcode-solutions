from collections import defaultdict
primes = [2,3,5,7,11,13,17,19]

def smallest_multiple(n):
    prime_map = defaultdict(int)
    for i in range(2, n+1):
        curr_map = defaultdict(int)
        j = i
        while j != 1:
            for prime in primes:
                while not j % prime:
                    curr_map[prime] += 1
                    j //= prime
        for key in curr_map:
            prime_map[key] = max(prime_map[key], curr_map[key])
    res = 1
    for k, v in prime_map.items():
        res *= pow(k, v)
    return res

print(smallest_multiple(20))