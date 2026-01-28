# WAP to Find the sum of all the primes below two million.

limit = 2000000
prime_sum = 0
print("Calculating the sum of all primes below", limit)
for num in range(2, limit):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num
print(prime_sum)
# WAP to By considering the terms in the Fibonacci sequence whose values do not exceed four million

fib1, fib2 = 1, 2
sum = 0


# while fib1 <= 4000000:
    