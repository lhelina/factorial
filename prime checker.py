num = 29
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is prime")
else:
    print(num, "is not prime")
