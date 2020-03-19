# long = int(input())

prime_list = [2, 3]


def isPrime(n):
    if n <= 3:
        return True
    for i in prime_list:
        if n > i and n % i == 0:
            return False
    prime_list.append(n)
    return True


def get_prime(num):
    primes = []
    tmp = num
    cur = 2
    while tmp > 0:
        for i in range(cur, tmp + 1):
            if isPrime(i) and tmp % i == 0:
                primes.append(i)
                cur = i
                break
        tmp = int(tmp / cur)
    return primes


long = 180
primes = get_prime(long)
for i in primes:
    print(i, end=' ')
