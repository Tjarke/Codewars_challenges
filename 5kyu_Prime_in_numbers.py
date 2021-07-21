"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


"""
import gmpy2


def prime_factors(n):
    nums = []
    i = 0
    q = 2
    
    while True:
        if n % q == 0:
            n = n / q
            nums.append(q)
        elif n == 1:
            break
        else:
            q = gmpy2.next_prime(q)

    ans = ""
    for i in sorted(list(set(nums))):
        a = nums.count(i)
        if a == 1:
            ans += f"({i})"
        else:
            ans += f"({i}**{a})"
    return ans

# The way prime number decomposition works, You dont need to find the prime numbers!
# If you iterate through 2,3 etc you already exclude non primes such as 4 , 9 etc ...
