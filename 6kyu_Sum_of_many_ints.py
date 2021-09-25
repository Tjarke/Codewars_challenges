"""
Write this function

f(n,m) = sum i to n  from ( i%m )

for i from 1 to n, do i % m and return the sum

f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)

You'll need to get a little clever with performance, since n can be a very large number


"""


def f(n, m):
    if m > n:
        return n * (n + 1) / 2
    until_m = (m - 1) * ((m - 1) + 1) / 2
    number_of_times = n // m
    rest = n % m
    return until_m * number_of_times + rest * (rest + 1) / 2
