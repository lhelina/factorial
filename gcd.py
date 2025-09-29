

def gcd(a, b):
    while b != 0:        
        a, b = b, a % b 
    return a


x = 36
y = 60
print("GCD of", x, "and", y, "is:", gcd(x, y))
