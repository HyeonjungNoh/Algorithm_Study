def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

divisors = find_divisors(24)
print(divisors)  # [1, 2, 3, 4, 6, 12]
