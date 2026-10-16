def isPerfect_no(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return n > 1 and total == n

n = int(input("Enter number: "))
print(isPerfect_no(n))