
def isPalindrome(num):
    s = str(num)
    return s == s[::-1]

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i*j
        if isPalindrome(product):
            largest = max(largest, product)
print(largest)