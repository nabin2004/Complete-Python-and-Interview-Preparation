import math

n = int(input("Enter a positive whole number greater than 2: "))

is_prime = True

for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        is_prime = False
        print(f"The divisors of {n} are:")
        for j in range(2, n):
            if n % j == 0:
                print("This number is divisor",j)
        break

if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"This number is divisor {n}")
    print(f"{n} is not a prime number.")
