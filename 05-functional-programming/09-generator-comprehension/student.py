from itertools import count

def is_prime(n):
    return n >= 2 and all(n % k != 0 for k in range(2, n))

def primes():
    return (n for n in count(0) if is_prime(n))

# print(is_prime(0))
# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(9))
# print(is_prime(10))
# ps = primes()
# print(ps)
# print(next(ps))
# print(next(ps))
# print(next(ps))
# print(next(ps))
# print(next(ps))
# print(next(ps))
# print(next(ps))