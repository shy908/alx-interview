def minOperations(n):
    if n <= 1:
        return n

    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    min_ops = 0
    for factor in factors:
        min_ops += factor

    return min_ops

# Example usage:
n = 9
result = minOperations(n)
print(f"Min number of operations to reach {n} characters: {result}")
