import math

def largest_prime_factor(n):
    marked = set()
    for i in range(2, int(math.sqrt(math.sqrt((n))))+1):
        if i not in marked:
            print(i)
            j = i*i
            while j <= math.sqrt(n):
                marked.add(j)
                j += i
    for num in reversed(range(2, int(math.sqrt(n))+1)):
        if num not in marked and not n % num:
            return num
        
print(largest_prime_factor((600851475143)))