"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def isPrime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True

num = 0
sum = 5
while num + 7 < 2000000:
    num += 6
    if(isPrime(num - 1)):
        sum += (num - 1)
    if (isPrime(num + 1)):
        sum += (num + 1)
print(num)
print(sum)
    